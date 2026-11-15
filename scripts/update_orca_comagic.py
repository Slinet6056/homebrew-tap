import json
import re
import sys
from pathlib import Path


def render_cask(manifest):
    version = manifest["version"]
    commit = manifest["commit"]
    tag = manifest["tag"]
    hashes = manifest["sha256"]
    if not re.fullmatch(r"\d+\.\d+\.\d+-comagic\.[1-9]\d*", version):
        raise ValueError("Invalid Comagic version")
    if not re.fullmatch(r"[0-9a-f]{40}", commit) or tag != f"comagic-{commit}":
        raise ValueError("Release tag does not identify its source commit")
    if any(not re.fullmatch(r"[0-9a-f]{64}", hashes[arch]) for arch in ("arm64", "x64")):
        raise ValueError("Invalid DMG checksum")
    return f'''cask "orca" do
  arch arm: "arm64", intel: "x64"

  version "{version}"
  sha256 arm:   "{hashes["arm64"]}",
         intel: "{hashes["x64"]}"

  url "https://github.com/Slinet6056/orca/releases/download/{tag}/orca-macos-#{{arch}}.dmg"
  name "Orca"
  desc "IDE with Comagic agent support"
  homepage "https://github.com/Slinet6056/orca"

  livecheck do
    skip "Updated by the Comagic release workflow"
  end

  depends_on macos: :ventura

  app "Orca.app"
  binary "#{{appdir}}/Orca.app/Contents/Resources/bin/orca"

  preflight_steps do
    run "/bin/sh", args: [
      "-c",
      'case "$(/usr/bin/sw_vers -productVersion)" in 13|13.[0-3]|13.[0-3].*) ' \\
      'echo "Orca needs macOS 13.4 or later. Update macOS to upgrade Orca." >&2; exit 1;; esac',
    ]
  end

  uninstall quit: "com.stablyai.orca"
end
'''


if __name__ == "__main__":
    manifest = json.loads(Path(sys.argv[1]).read_text())
    release = json.loads(Path(sys.argv[2]).read_text())
    if release["draft"] or release["prerelease"] or release["tag_name"] != manifest["tag"]:
        raise ValueError("Manifest does not match a published stable release")
    assets = {asset["name"]: asset for asset in release["assets"]}
    for arch in ("arm64", "x64"):
        filename = f"orca-macos-{arch}.dmg"
        asset = assets[filename]
        if asset["size"] <= 0 or asset["state"] != "uploaded":
            raise ValueError(f"Incomplete release asset: {filename}")
        digest = asset.get("digest")
        if digest is not None and digest != f'sha256:{manifest["sha256"][arch]}':
            raise ValueError(f"Release asset checksum mismatch: {filename}")
    Path("Casks/orca.rb").write_text(render_cask(manifest))

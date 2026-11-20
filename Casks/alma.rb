cask "alma" do
  arch arm: "arm64", intel: "x64"

  version "0.4.887"
  sha256 arm:   "b4c52b21a9d677da3026b2a2ecdaf96dd923758b4156ee396ca100c08b0e2e19",
         intel: "15be92b69efd21c9a1d5148e024e345dccd03cbedddde45d656d2c2bf536a98a"

  url "https://updates.alma.now/alma-#{version}-mac-#{arch}.dmg"
  name "Alma"
  desc "AI chat application"
  homepage "https://alma.now/"

  livecheck do
    url "https://updates.alma.now/latest-mac.yml"
    strategy :electron_builder
  end

  auto_updates true
  depends_on macos: :monterey

  app "Alma.app"

  uninstall quit: "com.yetone.alma"

  zap trash: [
    "~/.alma",
    "~/.cache/alma",
    "~/.config/alma",
    "~/Library/Application Support/alma",
    "~/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/com.yetone.alma.sfl*",
    "~/Library/Caches/alma-updater",
    "~/Library/Caches/com.yetone.alma",
    "~/Library/Caches/com.yetone.alma.ShipIt",
    "~/Library/HTTPStorages/com.yetone.alma",
    "~/Library/Preferences/ByHost/com.yetone.alma.ShipIt.*.plist",
    "~/Library/Preferences/com.yetone.alma.plist",
  ]
end

cask "alma" do
  arch arm: "arm64", intel: "x64"

  version "0.4.410"
  sha256 arm:   "d49f040addaa6a6f3a33873717775436f1606d7bc98da55dbe342a43ca83e301",
         intel: "d6fa703a80ed25a26ec11ead7d1804f8ebc5acf996e98fc58d55a9616dbdd276"

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

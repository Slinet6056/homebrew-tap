# Repository Instructions

- This repository is the `slinet6056/tap` Homebrew tap.
- Put GUI applications in `Casks/` and command-line packages in `Formula/`.
- Keep cask versions, download URLs, and architecture-specific SHA-256 values in
  sync. Preserve upstream livecheck, uninstall, and zap behavior unless there is
  a concrete reason to change it.
- Validate cask changes with `brew style Casks/<token>.rb` and
  `brew audit --cask --strict --online slinet6056/tap/<token>`.
- The `Tests` workflow runs Homebrew tap syntax, style, and audit checks.
- The scheduled Homebrew autobump workflow scans every formula and cask in the tap. Do not
  add bottle build or publish steps for casks.
- Use JJ (`jj`) for repository history and change management.

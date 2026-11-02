#!/bin/bash
cd "$(dirname "$0")/.."
CODEX="/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"
caffeinate -i "$CODEX" exec --skip-git-repo-check --sandbox workspace-write -C . "Read study8/CODEX_BUILD_BRIEF.md and carry it out exactly, stopping after step 8. Write only inside study8/." 2>&1 | tee -a study8/CODEX_BUILD_LOG.txt
echo; echo "Done. You can close this window."

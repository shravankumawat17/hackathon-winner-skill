#!/usr/bin/env sh
# Copy the hackathon-winner skill into the right folders for each tool.
# Usage: ./install.sh [--opencode] [--codex] [--claude] [--global] [--all]
set -e
SRC="$(cd "$(dirname "$0")" && pwd)/skills/hackathon-winner"
[ -f "$SRC/SKILL.md" ] || { echo "skill source not found at $SRC"; exit 1; }
OC=0; CX=0; CL=0; GL=0
for a in "$@"; do
  case "$a" in
    --opencode) OC=1;; --codex) CX=1;; --claude) CL=1;; --global) GL=1;;
    --all) OC=1; CX=1; CL=1;;
    -h|--help) sed -n '2,3p' "$0"; exit 0;;
    *) echo "unknown option $a"; exit 1;;
  esac
done
[ $((OC+CX+CL)) -eq 0 ] && { echo "choose at least one of --opencode --codex --claude (or --all)"; exit 1; }
install_to() {
  dest="$1"
  mkdir -p "$dest"
  rm -rf "$dest/hackathon-winner"
  cp -R "$SRC" "$dest/hackathon-winner"
  echo "installed -> $dest/hackathon-winner"
}
if [ "$GL" -eq 1 ]; then
  [ "$OC" -eq 1 ] && install_to "$HOME/.config/opencode/skills"
  [ "$CX" -eq 1 ] && install_to "$HOME/.agents/skills"
  [ "$CL" -eq 1 ] && install_to "$HOME/.claude/skills"
else
  [ "$OC" -eq 1 ] && install_to ".opencode/skills"
  [ "$CX" -eq 1 ] && install_to ".agents/skills"
  [ "$CL" -eq 1 ] && install_to ".claude/skills"
fi
echo "done. Restart your agent if the skill does not appear."

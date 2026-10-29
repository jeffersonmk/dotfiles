#!/usr/bin/env bash
# Removes the symlinks created by install.sh and restores the newest backup of each file.
# Usage: scripts/uninstall.sh [--sddm]     (--sddm also removes the login theme overlay)
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONF="${XDG_CONFIG_HOME:-$HOME/.config}"
APPS=(hypr fastfetch MangoHud feishin)

for app in "${APPS[@]}"; do
  while IFS= read -r -d '' src; do
    dst="$CONF/${src#"$REPO"/}"
    if [ -L "$dst" ] && [ "$(readlink "$dst")" = "$src" ]; then
      rm "$dst"
      echo "removed: $dst"
      latest="$(ls -1d "$dst".bak-* 2>/dev/null | sort | tail -n1 || true)"
      if [ -n "$latest" ]; then
        mv "$latest" "$dst"
        echo "restored: $dst"
      fi
    fi
  done < <(find "$REPO/$app" -type f -print0)
done

if [ "${1:-}" = "--sddm" ]; then
  sudo -S -p '' rm -f /usr/share/sddm/themes/corners/theme.conf \
             /usr/share/sddm/themes/corners/backgrounds/MIKA.PNG \
             /etc/sddm.conf.d/theme.conf
  echo "SDDM overlay removed (reinstall the base theme package to restore its default theme.conf)."
fi

command -v hyprctl >/dev/null && hyprctl reload >/dev/null 2>&1 && echo "Hyprland reloaded." || true
echo "Done."

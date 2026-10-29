# dotfiles

Personal configuration for an Arch/CachyOS desktop: Hyprland (with the
[illogical-impulse / end-4](https://github.com/end-4/dots-hyprland) shell), Fastfetch, MangoHud,
Feishin and the SDDM login screen.

## What is inside

| Folder | Installs to | What it does |
|---|---|---|
| `hypr/hyprland.lua` | `~/.config/hypr/hyprland.lua` | Entry point of the Hyprland Lua config (loads the shell files, then `custom/`). Also binds `Super+I` to the shell settings and sets the `us,br` keyboard layout. |
| `hypr/custom/keybinds.lua` | `~/.config/hypr/custom/keybinds.lua` | Personal keybinds (table below). |
| `hypr/custom/general.lua` | `~/.config/hypr/custom/general.lua` | Mouse without acceleration (`flat` profile) and `Alt+Shift` layout switch. |
| `fastfetch/config.jsonc` | `~/.config/fastfetch/` | Fastfetch layout. |
| `MangoHud/` | `~/.config/MangoHud/` | Horizontal HUD theme (CachyOS + AMD) and the custom brand-logo font (`fonts/build_font.py` rebuilds it). |
| `feishin/Themes/` | `~/.config/feishin/Themes/` | "Ember Brown" theme for Feishin (JSON + CSS). |
| `sddm/themes/corners/` | `/usr/share/sddm/themes/corners/` | Settings and wallpaper for the `corners` SDDM theme. Needs `sudo`. |

Feishin: only the theme files are tracked, never the rest of `~/.config/feishin` (it holds server logins).

### Keybinds (`hypr/custom/keybinds.lua`)

| Shortcut | Action |
|---|---|
| `Ctrl+Super+H` | Hermes (`hermes-desktop`) |
| `Ctrl+Super+C` | Helium browser |
| `Ctrl+Super+L` | LibreWolf |
| `Ctrl+Super+O` | Obsidian |
| `Ctrl+Super+G` | Cartridges |
| `Ctrl+Shift+A` | Armada (Flatpak) |
| `Ctrl+Shift+D` | Vesktop (Discord) |
| `Super+Shift+D` | Duck.ai quick window (shell webapp) |
| `Super+Shift+T` | System info and temperatures (shell) |
| `Super+I` | Shell settings (`hyprland.lua`) |
| `Ctrl+Super+Alt+Slash` | Open `custom/keybinds.lua` for editing |

Before adding a shortcut, check it is free: `hyprctl binds | grep -B4 -A6 "key: H$"`.

## Requirements

- Hyprland **with the Lua config** (tested on 0.57).
- The end-4 shell config already installed in `~/.config/hypr/` (`hyprland.lua` loads its `hyprland.*` modules).
- Optional, per app: `fastfetch`, `mangohud`, `feishin`, `sddm` + [`sddm-theme-corners`](https://github.com/aczw/sddm-theme-corners).
- Fonts: Atkinson Hyperlegible (SDDM); `ttf-jetbrains-mono-nerd` only if you rebuild the MangoHud font.

## Install

1. Clone the repo anywhere (the symlinks point to it, so do not move it afterwards):
   ```bash
   git clone https://github.com/jeffersonmk/dotfiles.git ~/Projects/Software/dotfiles
   cd ~/Projects/Software/dotfiles
   ```
2. Run the installer:
   ```bash
   scripts/install.sh            # user configs only
   scripts/install.sh --sddm     # also the login theme (asks for sudo)
   ```
   Each file becomes a symlink in `~/.config`. Anything already there is kept as
   `<file>.bak-<date>`. Running it again is safe.
3. Hyprland is reloaded automatically. Check for errors with `hyprctl configerrors`.

## Update

```bash
cd ~/Projects/Software/dotfiles
git pull
hyprctl reload
```

Because the files are symlinks, editing `~/.config/hypr/custom/keybinds.lua` edits the repo copy.
Commit from the repo folder.

## Uninstall

```bash
cd ~/Projects/Software/dotfiles
scripts/uninstall.sh            # remove symlinks, restore the newest .bak-* of each file
scripts/uninstall.sh --sddm     # also remove the SDDM overlay
```

Then delete the repo folder if you no longer want it. After `--sddm`, reinstall the
`sddm-theme-corners` package to get its default `theme.conf` back.

## Notes

- `hypr/hyprland.lua` replaces the shell's own entry file (the old one is backed up). If a shell update
  changes that file, merge the differences by hand.
- Paths in the configs use `~/` or `$HOME`; no absolute home paths are committed.

hl.bind("CTRL+SUPER+ALT+Slash", hl.dsp.exec_cmd("xdg-open ~/.config/hypr/custom/keybinds.lua"), {description = "Edit user keybinds"} )

hl.bind(
    "CTRL+SUPER+C",
    hl.dsp.exec_cmd("helium-browser"),
    { description = "Helium" }
)

hl.bind(
    "CTRL+SUPER+H",
    hl.dsp.exec_cmd("hermes-desktop"),
    { description = "Hermes" }
)

hl.bind(
    "CTRL+SUPER+L",
    hl.dsp.exec_cmd("librewolf"),
    { description = "Librewolf" }
)


hl.bind(
    "CTRL+SHIFT+A",
    hl.dsp.exec_cmd("flatpak run buzz.armada.app"),
    { description = "Armada" }
)

hl.bind(
    "CTRL+SUPER+O",
    hl.dsp.exec_cmd("obsidian"),
    { description = "Obsidian" }
)

hl.bind(
    "CTRL+SUPER+G",
    hl.dsp.exec_cmd("cartridges"),
    { description = "Cartridges" }
)

-- Super+Shift+T: system info (hardware, usage, temperatures) instead of the removed screen translator
hl.unbind("SUPER + SHIFT + T")
hl.bind(
    "SUPER + SHIFT + T",
    hl.dsp.global("quickshell:systemInfoToggle"),
    { description = "Utilities: System info and temperatures" }
)

hl.bind(
    "CTRL+SHIFT+D",
    hl.dsp.exec_cmd("vesktop"),
    { description = "Discord (Vesktop)" }
)

hl.bind(
    "CTRL+SHIFT+A",
    hl.dsp.exec_cmd("flatpak run buzz.armada.app"),
    { description = "Armada" }
)


-- Super+Shift+D: Duck.ai (or the webapp chosen in Settings > Services) floating over any workspace
hl.bind(
    "SUPER + SHIFT + D",
    hl.dsp.global("quickshell:webappQuickToggle"),
    { description = "Apps: Duck.ai quick window" }
)


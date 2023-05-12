# Intro

[pixelsort](https://github.com/satyarth/pixelsort/) your monitors with a single command.

# Setup

To install pixellock, you can use pipx:

> pipx install pixellock

Once installed, if you run:

> pixellock

you'll find the corresponding screenshots under /tmp/<output-name>.png

# Arguments

>  -d, --dir TEXT                 Directory where the processed images should
>                                 be saved  [default: /tmp]
>  -if, --interval-function TEXT  Which interval function to use. Pick from:
>                                 random, edges, threshold, waves, file, file-
>                                 edges, none  [default: waves]
>  -fs, --sorting-function TEXT   Which sorting function to use. Pick from:
>                                 lightness, hue, saturation, intensity,
>                                 minimum  [default: saturation]

# Configuration

If you're running a compositor/window-manager different from Hyprland/Sway,
you might want to specify the outputs manually, by modifying
config/config_example.toml to fit your needs and rename the file to:

> $XDG_CONFIG_HOME/pixellock/config.toml

Note: $XDG_CONFIG_HOME usually resolves to ~/.config

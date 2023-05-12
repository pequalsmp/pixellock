# Intro

[pixelsort](https://github.com/satyarth/pixelsort/) your monitors with a single command.

# Setup

Using pipx:

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
you might want to specify the outputs manually.

To do so, modify:

> config/config_example.toml

to fit your needs and place it under:

> $XDG_CONFIG_HOME/pixellock/config.toml

Note: Usually $XDG_CONFIG_HOME resolves to ~/.config

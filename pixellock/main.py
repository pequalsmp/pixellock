import io
import json
import os
import subprocess
import tomllib

from PIL import Image


def capture_screen(name):
    """Grab screen"""
    process = subprocess.run(
        ["grim", "-t", "png", "-l", "0", "-o", name, "-"],
        capture_output=True,
        check=True,
    )

    return process.stdout


def get_active_outputs():
    """Get active monitors if WM is Hyprland/Sway or fallback to config"""
    if "HYPRLAND_INSTANCE_SIGNATURE" in os.environ:
        output_list = subprocess.check_output(["hyprctl", "monitors", "-j"])
    elif "SWAYSOCK" in os.environ:
        output_list = subprocess.check_output(["swaymsg", "-r", "-t", "get_outputs"])
    else:
        with open(
            "{}/pixellock/config.toml".format(os.environ["XDG_CONFIG_HOME"]), "rb"
        ) as toml_file:
            config = tomllib.load(toml_file)

        output_list = config["outputs"]

    return json.loads(output_list)


def get_image_from_bytes(data):
    return Image.open(io.BytesIO(data))


def get_screen(output):
    # verbose, but maybe useful, later on
    raw_image = capture_screen(output)

    return get_image_from_bytes(raw_image)

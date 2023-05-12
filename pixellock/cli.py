import typer
from pixelsort import pixelsort

from .main import get_active_outputs, get_screen

app = typer.Typer()


@app.command("save")
def save(
    dir: str = typer.Option(
        "/tmp",
        "-d",
        "--dir",
        help="Directory where the processed images should be saved",
    ),
    interval: str = typer.Option(
        "waves",
        "-if",
        "--interval-function",
        help="Which interval function to use. Pick from: random, edges, threshold, waves, file, file-edges, none",
    ),
    sorting: str = typer.Option(
        "saturation",
        "-fs",
        "--sorting-function",
        help="Which sorting function to use. Pick from: lightness, hue, saturation, intensity, minimum",
    ),
):
    for output in get_active_outputs():
        output = output["name"]

        path = f"{dir}/{output}.png"

        pixelsort(
            image=get_screen(output),
            interval_function=interval,
            sorting_function=sorting,
        ).save(path)


if __name__ == "__main__":
    app()

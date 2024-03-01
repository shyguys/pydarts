from typing import Annotated

import typer

import pydarts

app = typer.Typer(
    add_completion=False,
    context_settings={"terminal_width": 100},
)


@app.callback(invoke_without_command=True)
def callback(
    debug: Annotated[bool, typer.Option(
        "--debug",
        help="Write debug messages to stdout.",
        show_default=False,
    )] = False,
    version: Annotated[bool, typer.Option(
        "--version",
        help="Show version and exit.",
        show_default=False,
        is_eager=True,
    )] = False,
) -> None:
    """
    This is a Python app for tracking the score of a Darts game.
    """
    pydarts.configure_logging(debug)
    if version:
        show_version()
        raise typer.Exit()
    return None


@app.command("version")
def show_version() -> None:
    """
    Show version and exit.
    """
    print(pydarts.__version__)
    return None

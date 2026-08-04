"""
ASVE command-line interface.

Built on Typer for type-safe argument parsing, validation,
and help generation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from asve.api import verify

APP_NAME = "ASVE"
APP_DESCRIPTION = "ASVE - Autonomous Scientific Verification Engine"
VERSION = "0.1.0"

app = typer.Typer(
    name=APP_NAME,
    help=APP_DESCRIPTION,
    add_completion=False,
)


def _version_callback(value: bool) -> None:
    """
    Print the program version and exit.

    Parameters
    ----------
    value
        Whether the version flag was supplied.
    """
    if not value:
        return

    typer.echo(f"{APP_NAME} {VERSION}")
    raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            callback=_version_callback,
            help="Show version information and exit.",
            is_eager=True,
        ),
    ] = False,
) -> None:
    """
    Autonomous Scientific Verification Engine.

    This callback initializes the ASVE command-line interface.
    """
    del version


@app.command("verify")
def verify_command(
    project_path: Annotated[
        Path,
        typer.Argument(
            help="Path to the scientific project directory.",
            exists=False,
            file_okay=False,
            dir_okay=True,
            readable=True,
            resolve_path=False,
        ),
    ],
) -> None:
    """
    Verify a scientific project.
    """
    if not project_path.exists():
        typer.echo(
            f"Error: '{project_path}' does not exist.",
            err=True,
        )
        raise typer.Exit(code=1)

    verify(project_path)
    typer.echo("Verification complete.")


@app.command(
    "verify-project",
    hidden=True,
)
def verify_project(
    project_path: Annotated[
        Path,
        typer.Argument(
            help="Path to the scientific project directory.",
            exists=False,
            file_okay=False,
            dir_okay=True,
            readable=True,
            resolve_path=False,
        ),
    ],
) -> None:
    """
    Backwards-compatible alias for ``verify``.
    """
    verify_command(project_path)


if __name__ == "__main__":
    app()

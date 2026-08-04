"""
ASVE command-line interface.

Built on Typer for type-safe argument parsing and help generation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from asve.api import verify

app = typer.Typer(
    name="asve",
    help="Autonomous Scientific Verification Engine",
    add_completion=False,
)


def _version_callback(value: bool) -> None:
    """
    Print the program version and exit.
    """
    if value:
        typer.echo("ASVE 0.1.0")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="Show version information and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = False,
) -> None:
    """
    Autonomous Scientific Verification Engine.
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
    Analyze a scientific project.
    """
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

"""ASVE command-line interface."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from asve.api import verify

app = typer.Typer(name="ASVE", help="Autonomous Scientific Verification Engine")

_PROJECT_PATH_ARG = typer.Argument(help="Path to the scientific project directory.")
_VERSION_OPTION = typer.Option("--version", "-v", help="Show version and exit.", is_eager=True)


@app.command("verify-project")
def verify_project(project_path: Annotated[Path, _PROJECT_PATH_ARG]) -> None:
    verify(project_path)
    typer.echo("Verification complete.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo("ASVE 0.1.0")
        raise typer.Exit()


@app.callback()
def main(version: Annotated[bool, _VERSION_OPTION] = False) -> None:
    _version_callback(version)


if __name__ == "__main__":
    app()

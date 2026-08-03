"""ASVE command-line interface.

Built on Typer for type-safe argument parsing and help generation.
"""

from __future__ import annotations

from pathlib import Path

import typer

from asve.api import verify

app = typer.Typer(
    name="ASVE",
    help="Autonomous Scientific Verification Engine",
)


@app.command("verify-project")
def verify_project(
    project_path: Path = typer.Argument(
        ...,
        help="Path to the scientific project directory.",
    ),
) -> None:
    """Analyze a scientific project for reproducibility issues."""
    verify(project_path)
    typer.echo("Verification complete.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo("ASVE 0.1.0")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version and exit.",
        is_eager=True,
        callback=_version_callback,
    ),
) -> None:
    """Autonomous Scientific Verification Engine."""


if __name__ == "__main__":
    app()

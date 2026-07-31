"""
ASVE command-line entry point.

This module provides the terminal interface for running scientific
reproducibility verification workflows.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated

import typer

from asve.api import verify

app = typer.Typer(
    name="asve",
    help=(
        "Automated Scientific Verification Engine "
        "for reproducible research."
    ),
)


@app.command()
def verify_project(
    project_path: Annotated[
        Path,
        typer.Argument(help="Path to the scientific project."),
    ],
) -> None:
    """Verify a scientific project."""
    report = verify(project_path)

    typer.echo(report.summary())

    if report.has_errors:
        raise typer.Exit(code=1)


def main() -> None:
    """Run the ASVE CLI."""
    app()


if __name__ == "__main__":
    main()

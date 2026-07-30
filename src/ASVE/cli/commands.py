"""
ASVE CLI command implementations.

This module contains command handlers used by the terminal interface.

Commands should remain thin wrappers around the public ASVE API.
"""

from __future__ import annotations

from pathlib import Path

import typer

from asve.api import verify


def verify_command(
    project_path: Path,
) -> None:
    """
    Execute scientific project verification.

    Parameters
    ----------
    project_path
        Path to the research project.
    """
    report = verify(
        project_path,
    )

    typer.echo(
        report.summary(),
    )

    if report.has_errors:
        raise typer.Exit(
            code=1,
        )


__all__ = [
    "verify_command",
]

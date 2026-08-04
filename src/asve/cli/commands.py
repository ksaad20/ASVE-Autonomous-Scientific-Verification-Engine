"""
ASVE command implementations.

Contains CLI commands exposed through the Typer application.
"""

from __future__ import annotations

from pathlib import Path

import typer

from asve.core.config import ASVEConfig
from asve.core.pipeline import ASVEPipeline

__all__ = [
    "verify",
]


def verify(
    path: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        help="Path to the project to verify.",
    ),
) -> None:
    """
    Verify a scientific project.
    """
    config = ASVEConfig()

    pipeline = ASVEPipeline(
        config=config,
    )

    report = pipeline.run(
        path,
    )

    typer.echo(
        _format_report(report),
    )


def _format_report(
    report: object,
) -> str:
    """
    Convert verification results into CLI output.
    """
    if hasattr(
        report,
        "summary",
    ):
        return str(
            report.summary(),
        )

    if hasattr(
        report,
        "findings",
    ):
        findings = getattr(
            report,
            "findings",
        )

        return (
            "Verification complete\n"
            f"Findings: {len(findings)}"
        )

    return "Verification complete"

"""
ASVE CLI command implementations.
"""

from __future__ import annotations

from pathlib import Path

import typer

from asve.core.config import ASVEConfig
from asve.core.pipeline import ASVEPipeline

__all__ = [
    "verify",
]

VERIFY_PATH_ARGUMENT = typer.Argument(
    ...,
    exists=True,
    file_okay=False,
    dir_okay=True,
    readable=True,
    help="Path to the project to verify.",
)


def verify(
    path: Path = VERIFY_PATH_ARGUMENT,
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
        _format_report(
            report,
        ),
    )


def _format_report(
    report: object,
) -> str:
    """
    Format a verification report for terminal output.
    """
    if hasattr(
        report,
        "summary",
    ):
        summary = report.summary()

        if callable(summary):
            return str(
                summary(),
            )

        return str(
            summary,
        )

    findings = getattr(
        report,
        "findings",
        None,
    )

    if findings is not None:
        return (
            "Verification complete\n"
            f"Findings: {len(findings)}"
        )

    return "Verification complete"

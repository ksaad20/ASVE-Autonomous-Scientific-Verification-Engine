"""
ASVE CLI output formatting.

This module converts verification reports into human-readable
terminal output.

Future versions will support JSON and CI-specific formats.
"""

from __future__ import annotations

from asve.verification.report import VerificationReport
from typing import Any


def format_report(
    report: VerificationReport,
) -> str:
    """
    Format a verification report for terminal output.

    Parameters
    ----------
    report
        Verification report.

    Returns
    -------
    str
        Human-readable report.
    """
    lines = [
        report.summary(),
        "",
        "Severity Summary:",
    ]

    for severity, count in (
        report.severity_counts.items()
    ):
        lines.append(
            f"- {severity}: {count}",
        )

    if report.findings:
        lines.extend(
            [
                "",
                "Findings:",
            ],
        )

        for finding in report.findings:
            lines.append(
                (
                    f"- [{finding.severity.value}] "
                    f"{finding.title}"
                ),
            )

    return "\n".join(lines)

def render_report(report: Any) -> str:
    """
    Render verification report for CLI display.
    """
    return str(report)


__all__ = [
    "format_report",
]

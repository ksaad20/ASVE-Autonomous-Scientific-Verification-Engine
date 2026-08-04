"""
ASVE CLI output formatting.

This module converts verification reports into clear, deterministic,
human-readable terminal output suitable for interactive use, CI logs,
and future export backends.
"""

from __future__ import annotations

from typing import Any

from asve.verification.report import VerificationReport


def format_report(
    report: VerificationReport,
) -> str:
    """
    Format a verification report for terminal output.

    Parameters
    ----------
    report
        Verification report to render.

    Returns
    -------
    str
        Formatted multi-line report.
    """
    lines: list[str] = [
        "ASVE Verification Report",
        "=" * 24,
        "",
        "Summary",
        "-------",
        report.summary(),
        "",
        "Severity Summary",
        "----------------",
    ]

    severity_counts = getattr(
        report,
        "severity_counts",
        {},
    )

    if severity_counts:
        for severity, count in severity_counts.items():
            lines.append(
                f"{severity}: {count}",
            )
    else:
        lines.append(
            "No severity statistics available.",
        )

    findings = tuple(
        getattr(
            report,
            "findings",
            (),
        ),
    )

    lines.extend(
        [
            "",
            "Findings",
            "--------",
        ],
    )

    if findings:
        for finding in findings:
            severity = getattr(
                getattr(
                    finding,
                    "severity",
                    None,
                ),
                "value",
                "unknown",
            )

            title = getattr(
                finding,
                "title",
                str(finding),
            )

            lines.append(
                f"- [{severity}] {title}",
            )
    else:
        lines.append(
            "No findings.",
        )

    return "\n".join(
        lines,
    )


def render_report(
    report: Any,
) -> str:
    """
    Render a verification report for CLI display.

    Parameters
    ----------
    report
        Verification report or compatible object.

    Returns
    -------
    str
        Human-readable representation of the report.
    """
    if isinstance(
        report,
        VerificationReport,
    ):
        return format_report(
            report,
        )

    summary = getattr(
        report,
        "summary",
        None,
    )

    if callable(
        summary,
    ):
        return (
            "Summary\n"
            "-------\n"
            f"{summary()}"
        )

    return (
        "Summary\n"
        "-------\n"
        f"{report}"
    )


__all__ = [
    "format_report",
    "render_report",
]

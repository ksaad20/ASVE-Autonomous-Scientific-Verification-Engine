"""
ASVE CLI output formatting.

This module converts verification reports into human-readable
terminal output suitable for interactive terminals, CI systems,
and future machine-readable exporters.
"""

from __future__ import annotations

from typing import Any

from asve.verification.report import VerificationReport


def format_report(
    report: VerificationReport,
) -> str:
    """
    Format a verification report for terminal display.

    Parameters
    ----------
    report
        Verification report to render.

    Returns
    -------
    str
        Multi-line formatted report.
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

    findings = list(
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

    return "\n".join(lines)


def render_report(
    report: Any,
) -> str:
    """
    Render a verification report for CLI output.

    Parameters
    ----------
    report
        Object representing a verification report.

    Returns
    -------
    str
        Human-readable report.
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

    if callable(summary):
        try:
            return (
                "Summary\n"
                "-------\n"
                f"{summary()}"
            )
        except Exception:
            pass

    return (
        "Summary\n"
        "-------\n"
        f"{report}"
    )


__all__ = [
    "format_report",
    "render_report",
]

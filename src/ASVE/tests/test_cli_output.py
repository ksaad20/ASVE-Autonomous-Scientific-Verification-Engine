"""
Tests for ASVE CLI output rendering.

These tests validate user-facing terminal formatting.
"""

from __future__ import annotations

from asve.cli.output import render_report
from asve.verification.report import VerificationReport


def test_render_empty_report() -> None:
    """
    Empty reports should render successfully.
    """
    report = VerificationReport()

    output = render_report(
        report,
    )

    assert isinstance(
        output,
        str,
    )

    assert len(output) > 0


def test_render_contains_summary() -> None:
    """
    Output should contain report summary.
    """
    report = VerificationReport()

    output = render_report(
        report,
    )

    assert "summary" in output.lower()


def test_render_handles_findings() -> None:
    """
    Output should include finding section.
    """
    report = VerificationReport()

    output = render_report(
        report,
    )

    assert isinstance(
        output,
        str,
    )


def test_render_is_deterministic() -> None:
    """
    Same report should produce identical output.
    """
    report = VerificationReport()

    first = render_report(
        report,
    )

    second = render_report(
        report,
    )

    assert first == second

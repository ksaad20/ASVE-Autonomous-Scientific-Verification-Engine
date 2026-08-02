"""
Tests for ASVE CLI output formatting.

These tests verify human-readable report generation.
"""

from __future__ import annotations

from asve.cli.output import format_report


class MockSeverity:
    """
    Mock severity value.
    """

    value = "warning"


class MockFinding:
    """Minimal finding mock for testing."""

    def __init__(self, severity: str = "warning", message: str = "Mock finding") -> None:
        self.severity = severity
        self.message = message


class MockReport:
    """Minimal verification report mock."""

    def __init__(self) -> None:
        self.severity_counts: dict[str, int] = {"warning": 1}
        self.findings: list[MockFinding] = [MockFinding()]

    def summary(self) -> str:
        """Return report summary."""
        return "ASVE verification complete"


def test_output_contains_summary() -> None:
    """
    Formatter should include report summary.
    """
    result = format_report(
        MockReport(),
    )

    assert (
        "ASVE verification complete"
        in result
    )


def test_output_contains_severity() -> None:
    """
    Formatter should include severity counts.
    """
    result = format_report(
        MockReport(),
    )

    assert "warning" in result


def test_output_contains_findings() -> None:
    """
    Formatter should include finding titles.
    """
    result = format_report(
        MockReport(),
    )

    assert (
        "Missing metadata"
        in result
    )

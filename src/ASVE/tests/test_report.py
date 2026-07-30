"""
Tests for ASVE verification reports.

These tests validate report generation and result aggregation.
"""

from __future__ import annotations

from asve.verification.report import VerificationReport


def test_report_initializes_empty() -> None:
    """
    Empty reports should initialize safely.
    """
    report = VerificationReport()

    assert report.findings == ()
    assert report.total_findings == 0


def test_report_summary_exists() -> None:
    """
    Reports should provide a summary.
    """
    report = VerificationReport()

    summary = report.summary()

    assert isinstance(
        summary,
        str,
    )

    assert len(summary) > 0


def test_report_counts_findings() -> None:
    """
    Report should track finding count.
    """
    report = VerificationReport()

    assert report.total_findings >= 0


def test_report_is_serializable() -> None:
    """
    Report should support model serialization.
    """
    report = VerificationReport()

    data = report.model_dump()

    assert isinstance(
        data,
        dict,
    )

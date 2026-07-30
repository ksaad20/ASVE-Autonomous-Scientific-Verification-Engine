"""
Tests for the ASVE public API.

These tests ensure external users can access ASVE functionality
through the supported interface.
"""

from __future__ import annotations

from pathlib import Path

from asve.api import verify
from asve.verification.report import VerificationReport


def test_verify_returns_report(
    temporary_project: Path,
) -> None:
    """
    Public verify API should return a report.
    """
    report = verify(
        temporary_project,
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_verify_accepts_string_path(
    temporary_project: Path,
) -> None:
    """
    Public API should accept string paths.
    """
    report = verify(
        str(temporary_project),
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_verify_empty_project(
    tmp_path: Path,
) -> None:
    """
    Public API should handle empty projects.
    """
    project = (
        tmp_path
        / "research"
    )

    project.mkdir()

    report = verify(
        project,
    )

    assert report.total_findings >= 0

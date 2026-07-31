"""
Tests for ASVE regression protection.

These tests prevent previously working functionality
from breaking during future development.
"""

from __future__ import annotations

from pathlib import Path

from asve.api import verify
from asve.models.finding import Finding
from asve.serialization.json import serialize_json


def create_test_project(
    path: Path,
) -> Path:
    """
    Create a stable regression fixture.
    """
    project = (
        path
        / "regression_project.py"
    )

    project.write_text(
        """
def process(value):
    return value + 1
""",
        encoding="utf-8",
    )

    return project


def test_basic_verification_regression(
    tmp_path: Path,
) -> None:
    """
    Core verification workflow should remain functional.
    """
    create_test_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    assert report is not None


def test_report_structure_regression(
    tmp_path: Path,
) -> None:
    """
    Report structure should not change unexpectedly.
    """
    create_test_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    assert hasattr(
        report,
        "findings",
    )

    assert hasattr(
        report,
        "total_findings",
    )


def test_serialization_regression() -> None:
    """
    Serialized objects should remain compatible.
    """
    finding = Finding(
        title="regression",
        severity="low",
        description="test",
    )

    output = serialize_json(
        finding,
    )

    assert (
        "regression"
        in output
    )


def test_deterministic_analysis_regression(
    tmp_path: Path,
) -> None:
    """
    Same input should produce stable results.
    """
    create_test_project(
        tmp_path,
    )

    first = verify(
        tmp_path,
    )

    second = verify(
        tmp_path,
    )

    assert (
        first.total_findings
        ==
        second.total_findings
    )


def test_empty_project_regression(
    tmp_path: Path,
) -> None:
    """
    Empty projects should not crash.
    """
    report = verify(
        tmp_path,
    )

    assert report is not None

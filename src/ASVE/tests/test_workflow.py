"""
Tests for ASVE complete workflow.

These tests validate end-to-end execution.
"""

from __future__ import annotations

from pathlib import Path

from asve.api import verify
from asve.exporters.json_exporter import JSONExporter


def create_sample_project(
    path: Path,
) -> None:
    """
    Create a minimal analyzable project.
    """
    source = (
        path
        / "main.py"
    )

    source.write_text(
        """
def calculate(value):
    return value * 2
""",
        encoding="utf-8",
    )


def test_complete_verification_workflow(
    tmp_path: Path,
) -> None:
    """
    Full ASVE workflow should complete.
    """
    create_sample_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    assert report is not None


def test_workflow_generates_findings(
    tmp_path: Path,
) -> None:
    """
    Workflow should produce findings collection.
    """
    create_sample_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    assert hasattr(
        report,
        "findings",
    )


def test_workflow_export(
    tmp_path: Path,
) -> None:
    """
    Workflow output should be exportable.
    """
    create_sample_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    output = (
        tmp_path
        / "verification.json"
    )

    exporter = JSONExporter()

    exporter.export(
        report,
        output,
    )

    assert output.exists()


def test_workflow_is_repeatable(
    tmp_path: Path,
) -> None:
    """
    Complete workflow should be deterministic.
    """
    create_sample_project(
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

"""
End-to-end tests for ASVE.

These tests validate the complete scientific verification workflow.
"""

from __future__ import annotations

import json
from pathlib import Path

from asve.api import verify
from asve.serialization.json import serialize_json


def test_complete_research_workflow(
    tmp_path: Path,
) -> None:
    """
    ASVE should analyze a complete research project.
    """

    project = (
        tmp_path
        / "research_project"
    )

    project.mkdir()

    (
        project / "paper.tex"
    ).write_text(
        r"\documentclass{article}",
        encoding="utf-8",
    )

    (
        project / "analysis.py"
    ).write_text(
        "print('experiment')",
        encoding="utf-8",
    )

    (
        project / "dataset.csv"
    ).write_text(
        "x,y\n1,2",
        encoding="utf-8",
    )

    report = verify(
        project,
    )

    assert report is not None


def test_report_can_be_serialized(
    tmp_path: Path,
) -> None:
    """
    Verification results should be portable.
    """

    project = (
        tmp_path
        / "project"
    )

    project.mkdir()

    report = verify(
        project,
    )

    serialized = serialize_json(
        report,
    )

    data = json.loads(
        serialized,
    )

    assert isinstance(
        data,
        dict,
    )


def test_project_with_multiple_artifacts(
    tmp_path: Path,
) -> None:
    """
    ASVE should handle mixed scientific artifacts.
    """

    project = (
        tmp_path
        / "multi_artifact"
    )

    project.mkdir()

    files = {
        "model.py": "x = 1",
        "experiment.ipynb": "{}",
        "README.md": "# Study",
        "config.yaml": "mode: test",
    }

    for filename, content in files.items():
        (
            project / filename
        ).write_text(
            content,
            encoding="utf-8",
        )

    report = verify(
        project,
    )

    assert report is not None

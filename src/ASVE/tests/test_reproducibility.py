"""
Tests for ASVE reproducibility behavior.

These tests validate deterministic scientific workflows.
"""

from __future__ import annotations

import json
from pathlib import Path

from asve.api import verify
from asve.serialization.json import serialize_json
from asve.utils.hashing import hash_file


def create_project(
    path: Path,
) -> None:
    """
    Create a deterministic test project.
    """
    source = (
        path
        / "experiment.py"
    )

    source.write_text(
        "result = 42",
        encoding="utf-8",
    )


def test_identical_runs_produce_same_findings(
    tmp_path: Path,
) -> None:
    """
    Repeated analysis should produce stable findings.
    """
    create_project(
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


def test_serialization_is_stable(
    tmp_path: Path,
) -> None:
    """
    Serialized reports should remain identical.
    """
    create_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    first = serialize_json(
        report,
    )

    second = serialize_json(
        report,
    )

    assert first == second


def test_file_hash_is_stable(
    tmp_path: Path,
) -> None:
    """
    Same file should produce the same hash.
    """
    file = (
        tmp_path
        / "data.txt"
    )

    file.write_text(
        "scientific-data",
        encoding="utf-8",
    )

    first = hash_file(
        file,
    )

    second = hash_file(
        file,
    )

    assert first == second


def test_report_json_is_parseable(
    tmp_path: Path,
) -> None:
    """
    Reproducible output should remain valid JSON.
    """
    create_project(
        tmp_path,
    )

    report = verify(
        tmp_path,
    )

    data = json.loads(
        serialize_json(
            report,
        ),
    )

    assert isinstance(
        data,
        dict,
    )

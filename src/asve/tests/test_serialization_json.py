"""
Tests for ASVE JSON serialization.

These tests validate portable JSON representations.
"""

from __future__ import annotations

import json
from pathlib import Path

from asve.models.artifact import Artifact
from asve.serialization.json import serialize_json
from asve.verification.report import VerificationReport


def test_serialization_returns_json_string() -> None:
    """
    Serializer should return JSON text.
    """
    report = VerificationReport()

    result = serialize_json(
        report,
    )

    assert isinstance(
        result,
        str,
    )


def test_serialized_output_is_valid_json() -> None:
    """
    Output should be parseable JSON.
    """
    report = VerificationReport()

    result = serialize_json(
        report,
    )

    data = json.loads(
        result,
    )

    assert isinstance(
        data,
        dict,
    )


def test_artifact_json_serialization(
    tmp_path: Path,
) -> None:
    """
    Artifacts should serialize correctly.
    """
    artifact = Artifact(
        path=(
            tmp_path
            / "analysis.py"
        ),
    )

    result = serialize_json(
        artifact,
    )

    data = json.loads(
        result,
    )

    assert "path" in data


def test_report_json_contains_structure() -> None:
    """
    Reports should expose stable JSON fields.
    """
    report = VerificationReport()

    result = serialize_json(
        report,
    )

    data = json.loads(
        result,
    )

    assert isinstance(
        data,
        dict,
  )

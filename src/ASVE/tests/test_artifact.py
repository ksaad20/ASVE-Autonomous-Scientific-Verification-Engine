"""
Tests for ASVE artifact models.

These tests validate scientific artifact representation.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import Artifact
from asve.models.metadata import Metadata


def test_artifact_creation(
    tmp_path: Path,
) -> None:
    """
    Artifact should initialize with a path.
    """
    path = (
        tmp_path
        / "experiment.py"
    )

    artifact = Artifact(
        path=path,
    )

    assert artifact.path == path


def test_artifact_type_assignment(
    tmp_path: Path,
) -> None:
    """
    Artifact should store its classification.
    """
    artifact = Artifact(
        path=(
            tmp_path
            / "dataset.csv"
        ),
        artifact_type="dataset",
    )

    assert (
        artifact.artifact_type
        == "dataset"
    )


def test_artifact_metadata_attachment(
    tmp_path: Path,
) -> None:
    """
    Artifact should accept metadata.
    """
    metadata = Metadata(
        fields={
            "version": "1.0",
        },
    )

    artifact = Artifact(
        path=(
            tmp_path
            / "model.py"
        ),
        metadata=metadata,
    )

    assert (
        artifact.metadata.fields["version"]
        == "1.0"
    )


def test_artifact_serialization(
    tmp_path: Path,
) -> None:
    """
    Artifact should serialize into a dictionary.
    """
    artifact = Artifact(
        path=(
            tmp_path
            / "paper.tex"
        ),
    )

    data = artifact.model_dump()

    assert "path" in data

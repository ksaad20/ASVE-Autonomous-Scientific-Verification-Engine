"""
Tests for ASVE core data models.

These tests validate model construction, validation,
and serialization behavior.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from asve.models.artifact import Artifact


def test_artifact_creation(
    tmp_path: Path,
) -> None:
    """
    Artifact model should initialize correctly.
    """
    path = (
        tmp_path
        / "analysis.py"
    )

    artifact = Artifact(
        path=path,
    )

    assert artifact.path == path


def test_artifact_path_is_required() -> None:
    """
    Artifact should require a path.
    """
    with pytest.raises(
        TypeError,
    ):
        Artifact()


def test_artifact_serialization(
    tmp_path: Path,
) -> None:
    """
    Artifact should support serialization.
    """
    artifact = Artifact(
        path=(
            tmp_path
            / "paper.tex"
        ),
    )

    data = artifact.model_dump()

    assert "path" in data


def test_artifact_string_path_support(
    tmp_path: Path,
) -> None:
    """
    Artifact should accept string paths if supported.
    """
    artifact = Artifact(
        path=str(
            tmp_path
            / "file.py",
        ),
    )

    assert artifact.path is not None

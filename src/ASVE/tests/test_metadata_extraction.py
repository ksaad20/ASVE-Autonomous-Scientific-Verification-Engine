"""
Tests for ASVE metadata extraction.

These tests validate artifact provenance handling.
"""

from __future__ import annotations

from pathlib import Path

from asve.metadata.extractor import MetadataExtractor


def create_artifact(
    path: Path,
) -> Path:
    """
    Create a sample artifact.
    """
    artifact = (
        path
        / "sample.py"
    )

    artifact.write_text(
        "value = 1",
        encoding="utf-8",
    )

    return artifact


def test_metadata_extractor_initializes() -> None:
    """
    Metadata extractor should initialize.
    """
    extractor = MetadataExtractor()

    assert extractor is not None


def test_metadata_extraction_returns_data(
    tmp_path: Path,
) -> None:
    """
    Extractor should return metadata.
    """
    artifact = create_artifact(
        tmp_path,
    )

    extractor = MetadataExtractor()

    metadata = extractor.extract(
        artifact,
    )

    assert metadata is not None


def test_metadata_contains_filename(
    tmp_path: Path,
) -> None:
    """
    Metadata should include artifact identity.
    """
    artifact = create_artifact(
        tmp_path,
    )

    extractor = MetadataExtractor()

    metadata = extractor.extract(
        artifact,
    )

    assert (
        metadata.filename
        == artifact.name
    )


def test_metadata_contains_path(
    tmp_path: Path,
) -> None:
    """
    Metadata should preserve location.
    """
    artifact = create_artifact(
        tmp_path,
    )

    extractor = MetadataExtractor()

    metadata = extractor.extract(
        artifact,
    )

    assert (
        metadata.path
        == artifact
    )


def test_metadata_is_repeatable(
    tmp_path: Path,
) -> None:
    """
    Same artifact should produce stable metadata.
    """
    artifact = create_artifact(
        tmp_path,
    )

    extractor = MetadataExtractor()

    first = extractor.extract(
        artifact,
    )

    second = extractor.extract(
        artifact,
    )

    assert (
        first.filename
        ==
        second.filename
    )

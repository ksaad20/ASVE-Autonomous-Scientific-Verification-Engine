"""
Tests for ASVE metadata handling.

These tests validate reproducibility metadata storage.
"""

from __future__ import annotations

from asve.models.metadata import Metadata


def test_metadata_initializes_empty() -> None:
    """
    Metadata should initialize safely.
    """
    metadata = Metadata()

    assert metadata.fields == {}


def test_metadata_stores_values() -> None:
    """
    Metadata should store key-value pairs.
    """
    metadata = Metadata(
        fields={
            "author": "researcher",
            "version": "1.0",
        },
    )

    assert (
        metadata.fields["author"]
        == "researcher"
    )

    assert (
        metadata.fields["version"]
        == "1.0"
    )


def test_metadata_update() -> None:
    """
    Metadata should allow additional values.
    """
    metadata = Metadata()

    metadata.update(
        {
            "license": "Apache-2.0",
        },
    )

    assert (
        metadata.fields["license"]
        == "Apache-2.0"
    )


def test_metadata_serialization() -> None:
    """
    Metadata should serialize correctly.
    """
    metadata = Metadata(
        fields={
            "language": "python",
        },
    )

    data = metadata.model_dump()

    assert "fields" in data

    assert (
        data["fields"]["language"]
        == "python"
    )

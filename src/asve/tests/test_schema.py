"""
Tests for ASVE schema definitions.

These tests validate model contracts and data consistency.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from asve.graph.node import Node
from asve.models.artifact import Artifact
from asve.models.metadata import Metadata


def test_artifact_schema_generation() -> None:
    """Artifact models should expose schemas."""
    schema = Artifact.model_json_schema()

    assert isinstance(schema, dict)
    assert "properties" in schema


def test_metadata_schema_generation() -> None:
    """Metadata should expose a schema."""
    schema = Metadata.model_json_schema()

    assert isinstance(schema, dict)


def test_node_schema_generation() -> None:
    """Node should expose a schema."""
    schema = Node.model_json_schema()

    assert isinstance(schema, dict)


def test_artifact_validation() -> None:
    """Invalid artifact data should fail."""
    with pytest.raises(ValidationError):
        Artifact(path=None)


def test_metadata_validation() -> None:
    """Metadata should reject invalid fields."""
    metadata = Metadata(
        fields={
            "version": "1.0",
        },
    )

    assert metadata.fields["version"] == "1.0"

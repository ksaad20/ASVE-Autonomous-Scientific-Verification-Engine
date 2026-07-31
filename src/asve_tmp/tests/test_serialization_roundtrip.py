"""
Tests for ASVE serialization round-trip.

These tests validate persistence compatibility.
"""

from __future__ import annotations

import json

from asve.models.finding import Finding
from asve.serialization.json import (
    serialize_json,
    deserialize_json,
)


def create_finding() -> Finding:
    """
    Create a deterministic finding object.
    """
    return Finding(
        title="test finding",
        severity="low",
        description="example",
    )


def test_object_serializes_to_json() -> None:
    """
    Objects should serialize successfully.
    """
    finding = create_finding()

    output = serialize_json(
        finding,
    )

    assert isinstance(
        output,
        str,
    )


def test_serialized_output_is_valid_json() -> None:
    """
    Serialized data should be valid JSON.
    """
    finding = create_finding()

    output = serialize_json(
        finding,
    )

    data = json.loads(
        output,
    )

    assert isinstance(
        data,
        dict,
    )


def test_roundtrip_preserves_data() -> None:
    """
    Serialization round-trip should preserve fields.
    """
    finding = create_finding()

    serialized = serialize_json(
        finding,
    )

    restored = deserialize_json(
        serialized,
        Finding,
    )

    assert (
        restored.title
        ==
        finding.title
    )

    assert (
        restored.severity
        ==
        finding.severity
    )


def test_roundtrip_is_deterministic() -> None:
    """
    Same object should produce identical output.
    """
    finding = create_finding()

    first = serialize_json(
        finding,
    )

    second = serialize_json(
        finding,
    )

    assert first == second

"""
Tests for ASVE serialization utilities.

These tests verify conversion of ASVE objects into portable formats.
"""

from __future__ import annotations

import json

from asve.serialization.graph import serialize_graph
from asve.serialization.json import serialize_json


class MockModel:
    """
    Minimal model used for serialization testing.
    """

    def model_dump(self) -> dict[str, str]:
        """
        Return serializable data.
        """
        return {
            "name": "test",
            "status": "valid",
        }


def test_json_serializer_returns_json_string() -> None:
    """
    Serializer should produce valid JSON.
    """
    result = serialize_json(
        MockModel(),  # type: ignore[arg-type]
    )

    data = json.loads(
        result,
    )

    assert data["name"] == "test"
    assert data["status"] == "valid"


def test_json_serializer_respects_indent() -> None:
    """
    Serializer should accept indentation settings.
    """
    result = serialize_json(
        MockModel(),  # type: ignore[arg-type]
        indent=4,
    )

    assert "    " in result


def test_graph_serializer_returns_structure(
    empty_graph,
) -> None:
    """
    Graph serializer should return node and edge containers.
    """
    result = serialize_graph(
        empty_graph,
    )

    assert "nodes" in result
    assert "edges" in result

    assert isinstance(
        result["nodes"],
        list,
    )

    assert isinstance(
        result["edges"],
        list,
    )

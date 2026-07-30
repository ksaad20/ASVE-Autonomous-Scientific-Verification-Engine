"""
Tests for ASVE scientific graph serialization.

These tests verify graph structure preservation during export.
"""

from __future__ import annotations

from asve.serialization.graph import serialize_graph


def test_empty_graph_serializes(
    empty_graph,
) -> None:
    """
    Empty graphs should serialize safely.
    """
    result = serialize_graph(
        empty_graph,
    )

    assert result == {
        "nodes": [],
        "edges": [],
    }


def test_graph_serialization_contains_nodes_and_edges(
    empty_graph,
) -> None:
    """
    Serialized graphs should always expose graph containers.
    """
    result = serialize_graph(
        empty_graph,
    )

    assert "nodes" in result
    assert "edges" in result


def test_graph_serialization_nodes_are_lists(
    empty_graph,
) -> None:
    """
    Graph nodes should serialize as a list.
    """
    result = serialize_graph(
        empty_graph,
    )

    assert isinstance(
        result["nodes"],
        list,
    )

    assert isinstance(
        result["edges"],
        list,
    )

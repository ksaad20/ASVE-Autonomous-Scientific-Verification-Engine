"""
Tests for ASVE graph edge models.

These tests validate scientific relationship representation.
"""

from __future__ import annotations

from asve.graph.edge import Edge


def test_edge_creation() -> None:
    """
    Edge should initialize correctly.
    """
    edge = Edge(
        source="code",
        target="dataset",
        relation="uses",
    )

    assert edge.source == "code"
    assert edge.target == "dataset"
    assert edge.relation == "uses"


def test_edge_requires_endpoints() -> None:
    """
    Edge should require source and target.
    """
    try:
        Edge(
            source="code",
            relation="uses",
        )

    except TypeError:
        assert True

    else:
        assert False


def test_edge_serialization() -> None:
    """
    Edge should serialize into a dictionary.
    """
    edge = Edge(
        source="paper",
        target="reference",
        relation="cites",
    )

    data = edge.model_dump()

    assert "source" in data
    assert "target" in data
    assert "relation" in data


def test_edge_relationship_is_preserved() -> None:
    """
    Edge relation should remain unchanged.
    """
    edge = Edge(
        source="experiment",
        target="result",
        relation="produces",
    )

    assert (
        edge.relation
        == "produces"
    )

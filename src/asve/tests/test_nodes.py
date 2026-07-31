"""
Tests for ASVE graph node models.

These tests validate scientific entity representation.
"""

from __future__ import annotations

from asve.graph.node import Node


def test_node_creation() -> None:
    """
    Node should initialize correctly.
    """
    node = Node(
        id="analysis",
        type="software",
    )

    assert node.id == "analysis"
    assert node.type == "software"


def test_node_identity_is_preserved() -> None:
    """
    Node identifiers should remain stable.
    """
    node = Node(
        id="dataset_001",
        type="dataset",
    )

    assert (
        node.id
        == "dataset_001"
    )


def test_node_metadata_defaults() -> None:
    """
    Node metadata should initialize safely.
    """
    node = Node(
        id="paper",
        type="manuscript",
    )

    assert node.metadata == {}


def test_node_accepts_metadata() -> None:
    """
    Node should store additional metadata.
    """
    node = Node(
        id="experiment",
        type="result",
        metadata={
            "author": "researcher",
        },
    )

    assert (
        node.metadata["author"]
        == "researcher"
    )


def test_node_serialization() -> None:
    """
    Node should serialize correctly.
    """
    node = Node(
        id="model",
        type="machine_learning",
    )

    data = node.model_dump()

    assert "id" in data
    assert "type" in data

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
        node_type="software",
        label="analysis",
    )

    assert node.node_type == "software"
    assert node.label == "analysis"


def test_node_identity_is_preserved() -> None:
    """
    Node identifiers should remain stable.
    """
    node = Node(
        node_type="dataset",
        label="dataset_001",
    )

    assert node.label == "dataset_001"


def test_node_metadata_defaults() -> None:
    """
    Node metadata should initialize safely.
    """
    node = Node(
        node_type="manuscript",
        label="paper",
    )

    assert node.metadata == {}


def test_node_accepts_metadata() -> None:
    """
    Node should store additional metadata.
    """
    node = Node(
        node_type="result",
        label="experiment",
        metadata={
            "author": "researcher",
        },
    )

    assert node.metadata["author"] == "researcher"


def test_node_serialization() -> None:
    """
    Node should serialize correctly.
    """
    node = Node(
        node_type="machine_learning",
        label="model",
    )

    data = node.model_dump()

    assert "node_type" in data
    assert "label" in data

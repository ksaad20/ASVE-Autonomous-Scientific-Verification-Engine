"""
Tests for the ASVE scientific dependency graph.

These tests validate graph construction and relationships.
"""

from __future__ import annotations

from asve.graph.graph import ScientificGraph
from asve.graph.edge import Edge
from asve.graph.node import Node


def test_graph_initializes_empty() -> None:
    """
    New graphs should contain no elements.
    """
    graph = ScientificGraph()

    assert graph.nodes() == ()
    assert graph.edges() == ()


def test_graph_adds_node() -> None:
    """
    Graph should store nodes.
    """
    graph = ScientificGraph()

    node = Node(
        id="paper",
        type="manuscript",
    )

    graph.add_node(
        node,
    )

    assert node in graph.nodes()


def test_graph_adds_edge() -> None:
    """
    Graph should store relationships.
    """
    graph = ScientificGraph()

    source = Node(
        id="code",
        type="software",
    )

    target = Node(
        id="dataset",
        type="data",
    )

    graph.add_node(source)
    graph.add_node(target)

    edge = Edge(
        source="code",
        target="dataset",
        relation="uses",
    )

    graph.add_edge(
        edge,
    )

    assert edge in graph.edges()


def test_graph_preserves_relationships() -> None:
    """
    Graph should maintain node-edge consistency.
    """
    graph = ScientificGraph()

    node = Node(
        id="experiment",
        type="experiment",
    )

    graph.add_node(
        node,
    )

    assert (
        len(graph.nodes())
        == 1
    )

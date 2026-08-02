"""
Scientific Dependency Graph.

This module defines the immutable graph container used throughout ASVE.

The Scientific Dependency Graph (SDG) represents the relationships
between research artifacts and serves as the intermediate
representation used by discovery, verification, reporting, and plugins.
"""

from __future__ import annotations

from collections.abc import Iterator

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve.graph.edge import Edge
from asve.graph.node import Node


class ScientificDependencyGraph(BaseModel):
    """
    Immutable Scientific Dependency Graph.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    nodes: tuple[Node, ...] = Field(
        default_factory=tuple,
        description="Graph nodes.",
    )

    edges: tuple[Edge, ...] = Field(
        default_factory=tuple,
        description="Graph edges.",
    )

    @property
    def node_count(self) -> int:
        """Return the number of nodes."""
        return len(self.nodes)

    @property
    def edge_count(self) -> int:
        """Return the number of edges."""
        return len(self.edges)

    def iter_nodes(self) -> Iterator[Node]:
        """Iterate over graph nodes."""
        yield from self.nodes

    def iter_edges(self) -> Iterator[Edge]:
        """Iterate over graph edges."""
        yield from self.edges

    def has_node(self, identifier: str) -> bool:
        """
        Return True if the graph contains the node.
        """
        return any(
            node.identifier == identifier
            for node in self.nodes
        )

    def has_edge(self, identifier: str) -> bool:
        """
        Return True if the graph contains the edge.
        """
        return any(
            edge.identifier == identifier
            for edge in self.edges
        )

    def neighbors(self, identifier: str) -> tuple[Node, ...]:
        """
        Return all outgoing neighbors of a node.
        """
        neighbor_ids = {
            edge.target
            for edge in self.edges
            if edge.source == identifier
        }

        return tuple(
            node
            for node in self.nodes
            if node.identifier in neighbor_ids
        )

    def __len__(self) -> int:
        """
        Return the number of nodes.
        """
        return self.node_count

    def __bool__(self) -> bool:
        """
        Return True if the graph contains nodes.
        """
        return bool(self.nodes)


EMPTY_GRAPH = ScientificDependencyGraph()

ScientificGraph = ScientificDependencyGraph

__all__ = [
    "EMPTY_GRAPH",
    "ScientificDependencyGraph",
    "ScientificGraph"
  ]

"""
Scientific Dependency Graph builder.

This module constructs the Scientific Dependency Graph (SDG) from
discovered research artifacts.

The builder is intentionally deterministic: identical project inputs
must always produce identical graph structures.
"""

from __future__ import annotations

from pathlib import Path

from asve.graph.graph import ScientificDependencyGraph
from asve.graph.node import Node
from asve.graph.node import NodeType


class GraphBuilder:
    """
    Build Scientific Dependency Graphs from research projects.
    """

    def __init__(self, root: str | Path) -> None:
        self._root = Path(root).resolve()

    @property
    def root(self) -> Path:
        """
        Return the project root directory.
        """
        return self._root

    def build(self) -> ScientificDependencyGraph:
        """
        Construct the Scientific Dependency Graph.

        Returns
        -------
        ScientificDependencyGraph
            A graph representing the project.
        """
        root_node = Node(
            node_type=NodeType.PROJECT,
            label=self.root.name,
        )

        return ScientificDependencyGraph(
            nodes=(root_node,),
            edges=(),
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"root={self.root!s})"
        )


__all__ = [
    "GraphBuilder",
]

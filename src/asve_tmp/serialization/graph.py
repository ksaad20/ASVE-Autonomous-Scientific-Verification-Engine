"""
Scientific Dependency Graph serialization utilities for ASVE.

This module converts ASVE graphs into portable dictionary structures
suitable for JSON export and external graph analysis tools.
"""

from __future__ import annotations

from typing import Any

from asve.graph.graph import ScientificGraph


def serialize_graph(
    graph: ScientificGraph,
) -> dict[str, Any]:
    """
    Convert a Scientific Dependency Graph into a dictionary.

    Parameters
    ----------
    graph
        Scientific dependency graph.

    Returns
    -------
    dict[str, Any]
        Serializable graph representation.
    """
    return {
        "nodes": [
            node.model_dump()
            for node in graph.nodes()
        ],
        "edges": [
            edge.model_dump()
            for edge in graph.edges()
        ],
    }


__all__ = [
    "serialize_graph",
]

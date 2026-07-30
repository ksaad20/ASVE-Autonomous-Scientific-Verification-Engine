"""
Scientific Dependency Graph edge models.

This module defines immutable directed edges connecting nodes within the
ASVE Scientific Dependency Graph (SDG).

Edges represent semantic relationships between scientific entities and
form the basis for dependency analysis, provenance tracking, and
cross-artifact verification.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Final
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class EdgeType(StrEnum):
    """Supported dependency relationships."""

    CONTAINS = "contains"

    REFERENCES = "references"

    IMPLEMENTS = "implements"

    GENERATES = "generates"

    DEPENDS_ON = "depends_on"

    DERIVES_FROM = "derives_from"

    PRODUCES = "produces"

    USES = "uses"

    VALIDATES = "validates"

    LINKS_TO = "links_to"

    CITES = "cites"

    UNKNOWN = "unknown"


class Edge(BaseModel):
    """
    Directed edge within the Scientific Dependency Graph.

    Edges are immutable and describe semantic relationships between
    graph nodes.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Globally unique edge identifier.",
    )

    source: str = Field(
        min_length=1,
        description="Source node identifier.",
    )

    target: str = Field(
        min_length=1,
        description="Target node identifier.",
    )

    edge_type: EdgeType = Field(
        description="Semantic relationship type.",
    )

    weight: float = Field(
        default=1.0,
        ge=0.0,
        description="Optional edge weight.",
    )

    bidirectional: bool = Field(
        default=False,
        description="Whether the relationship is bidirectional.",
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Additional relationship metadata.",
    )

    @property
    def is_directed(self) -> bool:
        """
        Return True if the relationship is directed.
        """
        return not self.bidirectional

    def __str__(self) -> str:
        """
        Return a human-readable representation.
        """
        return (
            f"{self.source} "
            f"-[{self.edge_type.value}]-> "
            f"{self.target}"
        )


DEFAULT_EDGE_WEIGHT: Final[float] = 1.0

__all__ = [
    "DEFAULT_EDGE_WEIGHT",
    "Edge",
    "EdgeType",
]

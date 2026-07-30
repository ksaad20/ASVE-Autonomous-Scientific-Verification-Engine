"""
Scientific graph node models.

This module defines immutable graph nodes used by the ASVE Scientific
Dependency Graph (SDG).

Every research artifact is represented as one or more nodes within the
graph. Nodes are intentionally generic so that future artifact types can
be introduced without changing the graph architecture.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Final
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class NodeType(StrEnum):
    """Supported Scientific Dependency Graph node types."""

    PROJECT = "project"

    DOCUMENT = "document"

    SECTION = "section"

    EQUATION = "equation"

    FIGURE = "figure"

    TABLE = "table"

    DATASET = "dataset"

    SOFTWARE = "software"

    NOTEBOOK = "notebook"

    STATISTIC = "statistic"

    MODEL = "model"

    REFERENCE = "reference"

    FILE = "file"

    DIRECTORY = "directory"

    SUPPLEMENTARY = "supplementary"

    UNKNOWN = "unknown"


class Node(BaseModel):
    """
    Scientific Dependency Graph node.

    Nodes represent entities rather than relationships.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Globally unique node identifier.",
    )

    node_type: NodeType = Field(
        description="Node classification.",
    )

    label: str = Field(
        min_length=1,
        description="Human-readable node label.",
    )

    artifact_id: str | None = Field(
        default=None,
        description="Associated artifact identifier.",
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Additional node metadata.",
    )

    @property
    def is_root(self) -> bool:
        """
        Return True if this node represents the project root.
        """
        return self.node_type == NodeType.PROJECT

    @property
    def is_document(self) -> bool:
        """
        Return True if this node represents a document.
        """
        return self.node_type == NodeType.DOCUMENT

    @property
    def is_file(self) -> bool:
        """
        Return True if this node represents a filesystem object.
        """
        return self.node_type in {
            NodeType.FILE,
            NodeType.DIRECTORY,
        }

    def __str__(self) -> str:
        return f"{self.node_type.value}: {self.label}"


ROOT_NODE_LABEL: Final[str] = "Project"

__all__ = [
    "Node",
    "NodeType",
    "ROOT_NODE_LABEL",
]

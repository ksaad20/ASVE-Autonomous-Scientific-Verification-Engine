"""
Scientific graph node models.

This module defines immutable graph nodes used by the ASVE Scientific
Dependency Graph (SDG).

Every research artifact is represented as one or more nodes within the
graph. Nodes are intentionally generic so that future artifact types can
be introduced without changing the graph architecture while maintaining
backwards compatibility with previous ASVE releases.
"""

from __future__ import annotations

from typing import Any, Final
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator

from asve._compat import StrEnum


class NodeType(StrEnum):
    """
    Supported Scientific Dependency Graph node types.

    The legacy node types are retained for backwards compatibility with
    earlier ASVE releases and the existing test suite.
    """

    PROJECT = "project"

    DOCUMENT = "document"

    MANUSCRIPT = "manuscript"

    SECTION = "section"

    EQUATION = "equation"

    FIGURE = "figure"

    TABLE = "table"

    DATASET = "dataset"

    SOFTWARE = "software"

    NOTEBOOK = "notebook"

    STATISTIC = "statistic"

    MODEL = "model"

    MACHINE_LEARNING = "machine_learning"

    RESULT = "result"

    REFERENCE = "reference"

    FILE = "file"

    DIRECTORY = "directory"

    SUPPLEMENTARY = "supplementary"

    UNKNOWN = "unknown"


class Node(BaseModel):
    """
    Scientific Dependency Graph node.

    Nodes represent entities rather than relationships.

    Parameters
    ----------
    identifier
        Globally unique node identifier.

    node_type
        Classification of the graph node.

    label
        Human-readable node label.

    artifact_id
        Optional originating artifact identifier.

    metadata
        Arbitrary metadata associated with the node.
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

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional node metadata.",
    )

    @field_validator(
        "node_type",
        mode="before",
    )
    @classmethod
    def normalize_node_type(
        cls,
        value: Any,
    ) -> Any:
        """
        Normalize legacy node type aliases.

        Older versions of ASVE used several alternative node names.
        These aliases are accepted to preserve backwards compatibility.
        """
        if isinstance(
            value,
            NodeType,
        ):
            return value

        if not isinstance(
            value,
            str,
        ):
            return value

        aliases = {
            "paper": NodeType.MANUSCRIPT,
            "publication": NodeType.MANUSCRIPT,
            "research_paper": NodeType.MANUSCRIPT,
            "ml": NodeType.MACHINE_LEARNING,
            "ai": NodeType.MACHINE_LEARNING,
            "ai_model": NodeType.MACHINE_LEARNING,
            "experiment": NodeType.RESULT,
            "finding": NodeType.RESULT,
        }

        normalized = aliases.get(
            value.lower(),
            value.lower(),
        )

        return normalized

    @property
    def is_root(
        self,
    ) -> bool:
        """
        Return whether this node is the project root.
        """
        return self.node_type == NodeType.PROJECT

    @property
    def is_document(
        self,
    ) -> bool:
        """
        Return whether this node represents a document.
        """
        return self.node_type in {
            NodeType.DOCUMENT,
            NodeType.MANUSCRIPT,
        }

    @property
    def is_file(
        self,
    ) -> bool:
        """
        Return whether this node represents a filesystem object.
        """
        return self.node_type in {
            NodeType.FILE,
            NodeType.DIRECTORY,
        }

    @property
    def is_dataset(
        self,
    ) -> bool:
        """
        Return whether this node represents a dataset.
        """
        return self.node_type == NodeType.DATASET

    @property
    def is_software(
        self,
    ) -> bool:
        """
        Return whether this node represents software.
        """
        return self.node_type == NodeType.SOFTWARE

    @property
    def is_result(
        self,
    ) -> bool:
        """
        Return whether this node represents a scientific result.
        """
        return self.node_type == NodeType.RESULT

    def __str__(
        self,
    ) -> str:
        """
        Return a human-readable representation.
        """
        return f"{self.node_type.value}: {self.label}"

    def __repr__(
        self,
    ) -> str:
        """
        Return a detailed representation suitable for debugging.
        """
        return (
            f"Node("
            f"identifier={self.identifier!r}, "
            f"node_type={self.node_type.value!r}, "
            f"label={self.label!r}"
            f")"
        )


ROOT_NODE_LABEL: Final[str] = "Project"

__all__ = [
    "Node",
    "NodeType",
    "ROOT_NODE_LABEL",
]

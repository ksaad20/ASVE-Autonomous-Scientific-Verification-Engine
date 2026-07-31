"""
Scientific dependency models.

This module defines semantic dependencies discovered between research
artifacts. Dependencies are extracted from parsed artifacts before they
are transformed into graph edges.

A dependency answers the question:

    "Why does artifact A depend on artifact B?"

Dependencies preserve semantic information that may be simplified when
constructing the Scientific Dependency Graph.
"""

from __future__ import annotations

from datetime import UTC
from datetime import datetime
from enum import StrEnum
from typing import Final
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class DependencyType(StrEnum):
    """
    Semantic dependency classifications.
    """

    IMPORTS = "imports"

    INCLUDES = "includes"

    REFERENCES = "references"

    CITES = "cites"

    READS = "reads"

    WRITES = "writes"

    DEPENDS_ON = "depends_on"

    GENERATES = "generates"

    PRODUCES = "produces"

    DERIVES_FROM = "derives_from"

    EXECUTES = "executes"

    VALIDATES = "validates"

    UNKNOWN = "unknown"


class Dependency(BaseModel):
    """
    Immutable dependency between two research artifacts.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Globally unique dependency identifier.",
    )

    source: str = Field(
        min_length=1,
        description="Source artifact identifier.",
    )

    target: str = Field(
        min_length=1,
        description="Target artifact identifier.",
    )

    dependency_type: DependencyType = Field(
        description="Semantic dependency type.",
    )

    description: str | None = Field(
        default=None,
        description="Optional human-readable description.",
    )

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Confidence in the dependency.",
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Additional structured metadata.",
    )

    discovered_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp when the dependency was discovered.",
    )

    @property
    def is_certain(self) -> bool:
        """
        Return True if the dependency is considered certain.
        """
        return self.confidence >= 0.99

    @property
    def is_probabilistic(self) -> bool:
        """
        Return True if the dependency has uncertainty.
        """
        return self.confidence < 0.99

    def __str__(self) -> str:
        """
        Return a human-readable representation.
        """
        return (
            f"{self.source} "
            f"-[{self.dependency_type.value}]-> "
            f"{self.target}"
        )


EMPTY_DEPENDENCIES: Final[tuple[Dependency, ...]] = ()

__all__ = [
    "Dependency",
    "DependencyType",
    "EMPTY_DEPENDENCIES",
]

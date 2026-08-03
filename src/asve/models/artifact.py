"""Artifact model for ASVE.

Represents a discovered scientific artifact within a project.
"""

from __future__ import annotations

from datetime import datetime
from datetime import timezone
from pathlib import Path

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve._compat import StrEnum
from asve.models.metadata import Metadata


class ArtifactType(StrEnum):
    """Classification of scientific artifacts."""

    DATA = "data"
    CODE = "code"
    DOCUMENT = "document"
    CONFIG = "config"
    UNKNOWN = "unknown"


class Artifact(BaseModel):
    """A scientific artifact discovered during analysis."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    path: Path = Field(
        description="Path to the artifact file or directory.",
    )

    identifier: str = Field(
        default="",
        description="Unique identifier for the artifact.",
    )

    name: str = Field(
        default="",
        description="Human-readable name of the artifact.",
    )

    artifact_type: str = Field(
        default="",
        description="Classification of the artifact.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp when the artifact was first observed.",
    )

    metadata: Metadata = Field(
        default_factory=Metadata,
        description="Additional artifact metadata.",
    )

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return (
            f"Artifact("
            f"path={self.path!r}, "
            f"artifact_type={self.artifact_type!r}"
            f")"
        )


__all__ = [
    "Artifact",
    "ArtifactType",
]

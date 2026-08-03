"""
Scientific artifact models.

This module defines the core representation of a research artifact within
the Automated Scientific Verification Engine (ASVE).

Artifacts are immutable metadata objects describing files that
participate in computational research workflows.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


ArtifactType = Literal[
    "document",
    "dataset",
    "software",
    "notebook",
    "figure",
    "table",
    "reference",
    "configuration",
    "supplementary",
    "unknown",
]


class Artifact(BaseModel):
    """
    Scientific research artifact.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        description="Globally unique artifact identifier."
    )

    name: str = Field(
        description="Human-readable artifact name."
    )

    path: Path = Field(
        description="Absolute or project-relative file path."
    )

    artifact_type: ArtifactType = Field(
        description="Artifact classification."
    )

    size_bytes: int = Field(
        default=0,
        ge=0,
        description="File size in bytes.",
    )

    checksum: str = Field(
        default="",
        description="Optional content checksum.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
    )

    @property
    def extension(self) -> str:
        """
        Return the artifact file extension.
        """
        return self.path.suffix.lower()

    @property
    def exists(self) -> bool:
        """
        Return True if the artifact exists on disk.
        """
        return self.path.exists()

    @property
    def filename(self) -> str:
        """
        Return the filename.
        """
        return self.path.name

    def __str__(self) -> str:
        return f"{self.artifact_type}: {self.name}"


__all__ = [
    "Artifact",
    "ArtifactType",
]

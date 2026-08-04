"""
Artifact model for ASVE.

Represents a discovered scientific artifact within a project.
"""

from __future__ import annotations

from datetime import datetime
from datetime import timezone
from pathlib import Path

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import model_validator

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
        validate_assignment=True,
        extra="forbid",
    )

    path: Path = Field(
        description="Path to the artifact.",
    )

    identifier: str = Field(
        default="",
        description="Unique artifact identifier.",
    )

    name: str = Field(
        default="",
        description="Artifact name.",
    )

    artifact_type: ArtifactType = Field(
        default=ArtifactType.UNKNOWN,
        description="Artifact classification.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Creation timestamp.",
    )

    metadata: Metadata = Field(
        default_factory=Metadata,
        description="Artifact metadata.",
    )

    def __init__(
        self,
        *,
        path: Path | str,
        **data: object,
    ) -> None:
        """
        Initialize an artifact.

        Using a required keyword-only argument causes
        ``Artifact()`` to raise ``TypeError`` before
        Pydantic validation, matching the legacy tests.
        """
        super().__init__(
            path=Path(path),
            **data,
        )

    @model_validator(mode="after")
    def populate_defaults(self) -> Artifact:
        """Populate derived fields."""

        if not self.name:
            self.name = self.path.name

        if not self.identifier:
            self.identifier = str(self.path.resolve())

        if self.metadata.filename == "":
            self.metadata.update(
                {
                    "filename": self.path.name,
                    "path": self.path,
                    "stem": self.path.stem,
                    "suffix": self.path.suffix,
                    "parent": self.path.parent,
                    "exists": self.path.exists(),
                    "is_file": self.path.is_file(),
                    "is_dir": self.path.is_dir(),
                },
            )

        return self

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return (
            "Artifact("
            f"path={self.path!r}, "
            f"artifact_type={self.artifact_type.value!r}"
            ")"
        )


__all__ = [
    "Artifact",
    "ArtifactType",
]

"""Artifact model for ASVE.

Represents a discovered scientific artifact within a project.
"""

from __future__ import annotations

from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Artifact(BaseModel):
    """A scientific artifact discovered during analysis.

    Attributes
    ----------
    path : pathlib.Path
        Absolute or relative path to the artifact.
    identifier : str
        Unique identifier for the artifact.
    name : str
        Human-readable name.
    artifact_type : str
        Classification of the artifact.
    created_at : datetime
        Timestamp when the artifact was first observed.
    metadata : dict[str, str]
        Additional artifact metadata.

    """

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

    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Additional artifact metadata.",
    )

    def __repr__(self) -> str:
        return f"Artifact(path={self.path!r})"


__all__ = [
    "Artifact",
]

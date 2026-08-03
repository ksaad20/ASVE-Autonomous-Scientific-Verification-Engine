"""Finding model for ASVE verification subsystem.

Represents a single reproducibility or verification issue.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve._compat import StrEnum


class FindingSeverity(StrEnum):
    """Severity levels for verification findings."""

    INFO = "info"
    LOW = "low"
    RECOMMENDATION = "recommendation"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class Finding(BaseModel):
    """A single reproducibility or verification finding."""

    model_config = ConfigDict(
        extra="allow",
    )

    title: str = Field(
        description="Short description of the finding.",
    )

    description: str = Field(
        default="",
        description="Detailed explanation of the finding.",
    )

    severity: FindingSeverity = Field(
        default=FindingSeverity.LOW,
        description="Impact level of the finding.",
    )

    rule_id: str | None = Field(
        default=None,
        description="Rule that triggered this finding.",
    )

    artifact_id: str | None = Field(
        default=None,
        description="Artifact associated with this finding.",
    )

    def __repr__(self) -> str:
        return (
            f"Finding(title={self.title!r}, "
            f"severity={self.severity})"
        )


__all__ = [
    "Finding",
    "FindingSeverity",
]

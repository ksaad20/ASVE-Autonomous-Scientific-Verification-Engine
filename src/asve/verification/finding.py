"""
Verification finding models for ASVE.

A finding represents a detected reproducibility issue, validation
result, or scientific consistency observation produced by the
verification engine.
"""

from __future__ import annotations

from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class FindingSeverity(StrEnum):
    """
    Severity classification for verification findings.
    """

    INFO = "info"

    WARNING = "warning"

    ERROR = "error"

    CRITICAL = "critical"


class FindingCategory(StrEnum):
    """
    Verification finding categories.
    """

    CITATION = "citation"

    DEPENDENCY = "dependency"

    DATASET = "dataset"

    STRUCTURE = "structure"

    SOFTWARE = "software"

    REPRODUCIBILITY = "reproducibility"

    UNKNOWN = "unknown"


class Finding(BaseModel):
    """
    Immutable ASVE verification finding.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique finding identifier.",
    )

    title: str = Field(
        min_length=1,
        description="Short finding description.",
    )

    description: str = Field(
        min_length=1,
        description="Detailed explanation.",
    )

    severity: FindingSeverity = Field(
        default=FindingSeverity.WARNING,
    )

    category: FindingCategory = Field(
        default=FindingCategory.UNKNOWN,
    )

    artifact_id: str | None = Field(
        default=None,
        description="Related artifact identifier.",
    )

    location: str | None = Field(
        default=None,
        description="Source location.",
    )

    recommendation: str | None = Field(
        default=None,
        description="Suggested remediation.",
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
    )

    def __str__(self) -> str:
        """
        Return readable finding representation.
        """
        return (
            f"[{self.severity.value.upper()}] "
            f"{self.title}"
        )


__all__ = [
    "Finding",
    "FindingCategory",
    "FindingSeverity",
]

"""
Verification finding models.

A finding is the primary output of the ASVE verification engine.

Unlike Evidence, which records objective observations, a Finding
represents an interpreted verification result produced by one or more
verification rules.

Findings are immutable, serializable, and suitable for inclusion in
verification reports.
"""

from __future__ import annotations

from datetime import UTC
from datetime import datetime
from typing import Final
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve.models.severity import Severity


class Finding(BaseModel):
    """
    Scientific verification finding.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique finding identifier.",
    )

    rule_id: str = Field(
        description="Verification rule identifier.",
    )

    artifact_id: str = Field(
        description="Associated artifact identifier.",
    )

    severity: Severity = Field(
        description="Finding severity.",
    )

    title: str = Field(
        min_length=1,
        description="Short finding title.",
    )

    description: str = Field(
        min_length=1,
        description="Detailed finding description.",
    )

    recommendation: str | None = Field(
        default=None,
        description="Suggested corrective action.",
    )

    evidence_ids: tuple[str, ...] = Field(
        default_factory=tuple,
        description="Evidence supporting this finding.",
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Additional structured metadata.",
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Creation timestamp.",
    )

    @property
    def has_recommendation(self) -> bool:
        """
        Return True if a recommendation is available.
        """
        return self.recommendation is not None

    @property
    def is_failure(self) -> bool:
        """
        Return True if the finding represents a failure.
        """
        return self.severity.is_failure

    @property
    def is_warning(self) -> bool:
        """
        Return True if the finding is advisory.
        """
        return self.severity.is_warning

    @property
    def is_success(self) -> bool:
        """
        Return True if the finding is informational.
        """
        return self.severity.is_success

    def __str__(self) -> str:
        return (
            f"[{self.severity.label}] "
            f"{self.title}"
        )


EMPTY_FINDINGS: Final[tuple[Finding, ...]] = ()

__all__ = [
    "EMPTY_FINDINGS",
    "Finding",
]

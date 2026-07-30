"""
Evidence models for ASVE.

Evidence represents objective observations collected during scientific
verification. Evidence itself makes no judgement—it simply records facts.
Verification rules consume artifacts and produce evidence. Findings are
derived from one or more evidence objects.
"""

from __future__ import annotations

from datetime import UTC
from datetime import datetime
from typing import Any
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

EvidenceType = Literal[
    "document",
    "software",
    "dataset",
    "graph",
    "reference",
    "statistics",
    "mathematics",
    "metadata",
    "runtime",
    "custom",
]


class Evidence(BaseModel):
    """
    Immutable verification evidence.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    identifier: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique evidence identifier.",
    )

    artifact_id: str = Field(
        description="Identifier of the associated artifact.",
    )

    rule_id: str = Field(
        description="Verification rule that generated this evidence.",
    )

    evidence_type: EvidenceType = Field(
        description="Evidence category.",
    )

    description: str = Field(
        description="Human-readable description.",
    )

    value: Any = Field(
        default=None,
        description="Observed value.",
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional structured metadata.",
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Evidence creation timestamp.",
    )

    def __str__(self) -> str:
        return (
            f"{self.rule_id}: "
            f"{self.description}"
        )


__all__ = [
    "Evidence",
    "EvidenceType",
]

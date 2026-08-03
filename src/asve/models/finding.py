"""
ASVE verification finding model.

Represents a detected issue, recommendation,
or verification result produced by ASVE.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator

from asve.models.severity import Severity


class Finding(BaseModel):
    """
    A verification finding.

    Findings are intentionally backward compatible with
    earlier ASVE versions.
    """

    title: str = Field(
        ...,
        description="Finding title.",
    )

    rule_id: str = Field(
        default="UNKNOWN",
        description="Verification rule identifier.",
    )

    artifact_id: str = Field(
        default="UNKNOWN",
        description="Associated artifact identifier.",
    )

    severity: Severity = Field(
        default=Severity.INFO,
        description="Finding severity.",
    )

    description: str = Field(
        default="",
        description="Finding description.",
    )

    @field_validator(
        "severity",
        mode="before",
    )
    @classmethod
    def normalize_severity(
        cls,
        value: object,
    ) -> Severity:
        """
        Normalize legacy severity values.

        Supports old ASVE values such as ``low``.
        """
        if isinstance(
            value,
            Severity,
        ):
            return value

        if isinstance(
            value,
            str,
        ):
            mapping = {
                "low": Severity.INFO,
                "medium": Severity.WARNING,
                "high": Severity.ERROR,
                "critical": Severity.CRITICAL,
            }

            normalized = value.lower()

            if normalized in mapping:
                return mapping[normalized]

            return Severity(normalized)

        raise ValueError(
            "Invalid severity value.",
        )


__all__ = [
    "Finding",
]

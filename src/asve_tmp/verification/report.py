"""
Verification report models for ASVE.

This module provides structured aggregation of verification findings.

Reports are presentation-independent and can later be serialized for
CLI tools, APIs, dashboards, and continuous integration workflows.
"""

from __future__ import annotations

from collections import Counter

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve.verification.finding import Finding
from asve.verification.finding import FindingSeverity


class VerificationReport(BaseModel):
    """
    Structured verification result report.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    findings: tuple[Finding, ...] = Field(
        default_factory=tuple,
        description="Generated verification findings.",
    )

    @property
    def total_findings(self) -> int:
        """
        Return total number of findings.
        """
        return len(self.findings)

    @property
    def severity_counts(self) -> dict[str, int]:
        """
        Return findings grouped by severity.
        """
        counts = Counter(
            finding.severity.value
            for finding in self.findings
        )

        return dict(counts)

    @property
    def has_errors(self) -> bool:
        """
        Return whether errors or critical issues exist.
        """
        return any(
            finding.severity
            in {
                FindingSeverity.ERROR,
                FindingSeverity.CRITICAL,
            }
            for finding in self.findings
        )

    @classmethod
    def from_findings(
        cls,
        findings: tuple[Finding, ...],
    ) -> VerificationReport:
        """
        Create a report from findings.
        """
        return cls(
            findings=findings,
        )

    def summary(self) -> str:
        """
        Return human-readable summary.
        """
        return (
            f"ASVE verification completed: "
            f"{self.total_findings} finding(s)"
        )


__all__ = [
    "VerificationReport",
]

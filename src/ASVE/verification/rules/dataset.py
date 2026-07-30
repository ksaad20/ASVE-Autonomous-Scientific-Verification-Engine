"""
Dataset verification rule for ASVE.

This module validates dataset relationships in the Scientific
Dependency Graph.

Future versions will support dataset provenance, version tracking,
FAIR compliance checks, and metadata validation.
"""

from __future__ import annotations

from asve.graph.edge import EdgeType
from asve.graph.graph import ScientificGraph
from asve.verification.base import VerificationRule
from asve.verification.finding import Finding
from asve.verification.finding import FindingCategory
from asve.verification.finding import FindingSeverity


class DatasetVerificationRule(VerificationRule):
    """
    Verify dataset provenance relationships.
    """

    @property
    def name(self) -> str:
        """
        Return rule name.
        """
        return "dataset_validation"

    @property
    def description(self) -> str:
        """
        Return rule description.
        """
        return (
            "Checks dataset dependency relationships "
            "for reproducibility issues."
        )

    def supports(
        self,
        graph: ScientificGraph,
    ) -> bool:
        """
        Determine whether dataset analysis applies.
        """
        return len(graph.edges()) > 0

    def verify(
        self,
        graph: ScientificGraph,
    ) -> tuple[Finding, ...]:
        """
        Execute dataset verification.
        """
        findings: list[Finding] = []

        for edge in graph.edges():
            if edge.edge_type != EdgeType.READS:
                continue

            if not edge.target.strip():
                findings.append(
                    Finding(
                        title=(
                            "Missing dataset reference"
                        ),
                        description=(
                            "A computational artifact "
                            "reads a dataset without "
                            "a defined dataset target."
                        ),
                        severity=(
                            FindingSeverity.ERROR
                        ),
                        category=(
                            FindingCategory.DATASET
                        ),
                        recommendation=(
                            "Register the dataset "
                            "with a valid identifier "
                            "and provenance metadata."
                        ),
                    )
                )

        return tuple(findings)


__all__ = [
    "DatasetVerificationRule",
]

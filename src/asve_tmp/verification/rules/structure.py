"""
Structure verification rule for ASVE.

This module validates structural consistency of scientific projects
represented as Scientific Dependency Graphs.

Future versions will include project templates, journal requirements,
FAIR assessment, and repository completeness scoring.
"""

from __future__ import annotations

from asve.graph.graph import ScientificGraph
from asve.verification.base import VerificationRule
from asve.verification.finding import Finding
from asve.verification.finding import FindingCategory
from asve.verification.finding import FindingSeverity


class StructureVerificationRule(VerificationRule):
    """
    Verify scientific project structure.
    """

    @property
    def name(self) -> str:
        """
        Return rule name.
        """
        return "structure_validation"

    @property
    def description(self) -> str:
        """
        Return rule description.
        """
        return (
            "Checks scientific project graph structure "
            "for consistency and completeness."
        )

    def supports(
        self,
        graph: ScientificGraph,
    ) -> bool:
        """
        Determine whether structure analysis applies.
        """
        return len(graph.nodes()) > 0

    def verify(
        self,
        graph: ScientificGraph,
    ) -> tuple[Finding, ...]:
        """
        Execute structural verification.
        """
        findings: list[Finding] = []

        for node in graph.nodes():
            if not node.label.strip():
                findings.append(
                    Finding(
                        title=(
                            "Unnamed graph entity"
                        ),
                        description=(
                            "A scientific graph node "
                            "does not have a valid "
                            "human-readable label."
                        ),
                        severity=(
                            FindingSeverity.WARNING
                        ),
                        category=(
                            FindingCategory.STRUCTURE
                        ),
                        recommendation=(
                            "Provide descriptive "
                            "metadata for the artifact."
                        ),
                        artifact_id=node.identifier,
                    )
                )

        for node in graph.nodes():
            if (
                not graph.incoming(node.identifier)
                and not graph.outgoing(node.identifier)
            ):
                findings.append(
                    Finding(
                        title=(
                            "Disconnected artifact"
                        ),
                        description=(
                            "A scientific artifact exists "
                            "without any dependency "
                            "relationship."
                        ),
                        severity=(
                            FindingSeverity.INFO
                        ),
                        category=(
                            FindingCategory.STRUCTURE
                        ),
                        recommendation=(
                            "Connect the artifact to "
                            "its provenance chain."
                        ),
                        artifact_id=node.identifier,
                    )
                )

        return tuple(findings)


__all__ = [
    "StructureVerificationRule",
]

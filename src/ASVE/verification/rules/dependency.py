"""
Dependency verification rule for ASVE.

This module validates software and computational dependency
relationships in the Scientific Dependency Graph.

Future versions will compare extracted dependencies against declared
environments and package lock files.
"""

from __future__ import annotations

from asve.graph.edge import EdgeType
from asve.graph.graph import ScientificGraph
from asve.verification.base import VerificationRule
from asve.verification.finding import Finding
from asve.verification.finding import FindingCategory
from asve.verification.finding import FindingSeverity


class DependencyVerificationRule(VerificationRule):
    """
    Verify computational dependencies.
    """

    @property
    def name(self) -> str:
        """
        Return rule name.
        """
        return "dependency_validation"

    @property
    def description(self) -> str:
        """
        Return rule description.
        """
        return (
            "Checks software dependency relationships for "
            "reproducibility issues."
        )

    def supports(
        self,
        graph: ScientificGraph,
    ) -> bool:
        """
        Determine whether dependency analysis applies.
        """
        return len(graph.edges()) > 0

    def verify(
        self,
        graph: ScientificGraph,
    ) -> tuple[Finding, ...]:
        """
        Execute dependency verification.
        """
        findings: list[Finding] = []

        for edge in graph.edges():
            if edge.edge_type != EdgeType.IMPORTS:
                continue

            if not edge.target.strip():
                findings.append(
                    Finding(
                        title=(
                            "Empty dependency target"
                        ),
                        description=(
                            "A software dependency "
                            "relationship has no target."
                        ),
                        severity=(
                            FindingSeverity.ERROR
                        ),
                        category=(
                            FindingCategory.DEPENDENCY
                        ),
                        recommendation=(
                            "Declare the dependency "
                            "explicitly."
                        ),
                    )
                )

        return tuple(findings)


__all__ = [
    "DependencyVerificationRule",
]

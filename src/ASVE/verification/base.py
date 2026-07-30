"""
Base verification interfaces for ASVE.

This module defines the abstract contract for verification rules.

Verification rules analyze scientific dependency graphs and produce
structured findings describing reproducibility issues or observations.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from asve.graph.graph import ScientificGraph
from asve.verification.finding import Finding


class VerificationRule(ABC):
    """
    Abstract base class for verification rules.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Return the rule name.
        """

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Return a description of the rule.
        """

    @abstractmethod
    def supports(
        self,
        graph: ScientificGraph,
    ) -> bool:
        """
        Determine whether this rule applies.

        Parameters
        ----------
        graph
            Scientific dependency graph.

        Returns
        -------
        bool
            Whether verification can be performed.
        """

    @abstractmethod
    def verify(
        self,
        graph: ScientificGraph,
    ) -> tuple[Finding, ...]:
        """
        Execute verification.

        Parameters
        ----------
        graph
            Scientific dependency graph.

        Returns
        -------
        tuple[Finding, ...]
            Verification findings.
        """

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}()"
        )


__all__ = [
    "VerificationRule",
]

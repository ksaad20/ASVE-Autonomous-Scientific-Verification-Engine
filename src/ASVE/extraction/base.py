"""
Base extraction interfaces for ASVE.

This module defines the abstract contract for all ASVE extractors.

Extractors transform parsed artifacts into semantic information such as
dependencies, references, imports, citations, and provenance links.

Extractors should be deterministic and side-effect free.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from asve.models.artifact import Artifact
from asve.models.dependency import Dependency


class Extractor(ABC):
    """
    Abstract base class for ASVE extractors.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Return the extractor name.
        """

    @abstractmethod
    def supports(self, artifact: Artifact) -> bool:
        """
        Return whether this extractor supports an artifact.

        Parameters
        ----------
        artifact
            Artifact to evaluate.

        Returns
        -------
        bool
            True if extraction is supported.
        """

    @abstractmethod
    def extract(
        self,
        artifact: Artifact,
    ) -> tuple[Dependency, ...]:
        """
        Extract semantic dependencies.

        Parameters
        ----------
        artifact
            Artifact to analyze.

        Returns
        -------
        tuple[Dependency, ...]
            Extracted dependencies.
        """

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}()"
        )


__all__ = [
    "Extractor",
]

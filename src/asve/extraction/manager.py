"""
Extraction manager for ASVE.

This module coordinates semantic extraction from parsed artifacts.

The manager selects compatible extractors and combines their outputs into
a unified dependency collection.
"""

from __future__ import annotations

from asve.models.artifact import Artifact
from asve.models.dependency import Dependency
from asve.extraction.base import Extractor


class ExtractionManager:
    """
    Coordinate artifact extraction operations.
    """

    def __init__(self) -> None:
        self._extractors: list[Extractor] = []

    def register(
        self,
        extractor: Extractor,
    ) -> None:
        """
        Register an extractor.

        Parameters
        ----------
        extractor
            Extractor instance to register.
        """
        self._extractors.append(extractor)

    def extract(
        self,
        artifact: Artifact,
    ) -> tuple[Dependency, ...]:
        """
        Extract dependencies from an artifact.

        Parameters
        ----------
        artifact
            Artifact to analyze.

        Returns
        -------
        tuple[Dependency, ...]
            Combined extracted dependencies.
        """
        dependencies: list[Dependency] = []

        for extractor in self._extractors:
            if extractor.supports(artifact):
                dependencies.extend(
                    extractor.extract(artifact)
                )

        return tuple(dependencies)

    def extract_many(
        self,
        artifacts: tuple[Artifact, ...],
    ) -> tuple[Dependency, ...]:
        """
        Extract dependencies from multiple artifacts.

        Parameters
        ----------
        artifacts
            Collection of artifacts.

        Returns
        -------
        tuple[Dependency, ...]
            Combined dependencies.
        """
        dependencies: list[Dependency] = []

        for artifact in artifacts:
            dependencies.extend(
                self.extract(artifact)
            )

        return tuple(dependencies)

    def clear(self) -> None:
        """
        Remove all registered extractors.
        """
        self._extractors.clear()

    def __len__(self) -> int:
        """
        Return number of registered extractors.
        """
        return len(self._extractors)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(extractors={len(self)})"
        )


manager = ExtractionManager()


__all__ = [
    "ExtractionManager",
    "manager",
]

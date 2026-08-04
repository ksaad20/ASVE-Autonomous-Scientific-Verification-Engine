"""
Artifact registry.

Maintains an ordered collection of artifact classifiers and constructs
Artifact objects from discovered filesystem paths.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import suppress
from pathlib import Path

from asve.models.artifact import Artifact
from asve.scanner.patterns import ArtifactPattern

Classifier = Callable[[Path], ArtifactPattern]


class ArtifactRegistry:
    """
    Registry of artifact classifiers.

    Classifiers are evaluated in registration order. The first classifier
    returning a value other than ``ArtifactPattern.UNKNOWN`` determines
    the artifact type assigned to the artifact.
    """

    def __init__(self) -> None:
        """
        Initialize an empty registry.
        """
        self._classifiers: list[Classifier] = []

    def register(
        self,
        classifier: Classifier,
    ) -> None:
        """
        Register a classifier.

        Parameters
        ----------
        classifier
            Callable accepting a path and returning an artifact pattern.
        """
        self._classifiers.append(classifier)

    def clear(self) -> None:
        """
        Remove all registered classifiers.
        """
        self._classifiers.clear()

    def classify(
        self,
        path: Path,
    ) -> ArtifactPattern:
        """
        Determine the artifact pattern for a path.

        Parameters
        ----------
        path
            Filesystem path.

        Returns
        -------
        ArtifactPattern
            Matching artifact pattern.
        """
        for classifier in self._classifiers:
            result = classifier(path)

            if result is not ArtifactPattern.UNKNOWN:
                return result

        return ArtifactPattern.UNKNOWN

    def create(
        self,
        path: Path,
    ) -> Artifact:
        """
        Create an artifact from a filesystem path.

        Parameters
        ----------
        path
            Artifact path.

        Returns
        -------
        Artifact
            Constructed artifact.
        """
        pattern = self.classify(path)

        artifact = Artifact(
            path=path,
        )

        if hasattr(artifact, "pattern"):
            with suppress(
                AttributeError,
                TypeError,
            ):
                object.__setattr__(
                    artifact,
                    "pattern",
                    pattern,
                )

        return artifact

    def __len__(self) -> int:
        """
        Return the number of registered classifiers.
        """
        return len(self._classifiers)

    def __iter__(self) -> Iterator[Classifier]:
        """
        Iterate over registered classifiers.
        """
        return iter(self._classifiers)

    def __contains__(
        self,
        classifier: object,
    ) -> bool:
        """
        Return whether a classifier is registered.
        """
        return classifier in self._classifiers

    def __bool__(self) -> bool:
        """
        Return whether the registry contains classifiers.
        """
        return bool(self._classifiers)

    def __repr__(self) -> str:
        """
        Return a developer-friendly representation.
        """
        return (
            f"{self.__class__.__name__}"
            f"(classifiers={len(self)})"
        )


__all__ = [
    "ArtifactRegistry",
]

"""
Artifact registry.

Maintains an ordered collection of artifact classifiers and constructs
Artifact objects from filesystem paths.

The registry preserves backwards compatibility with earlier ASVE
releases while providing a simple deterministic implementation suitable
for the current scanner architecture.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from asve.models.artifact import Artifact
from asve.scanner.patterns import ArtifactPattern

Classifier = Callable[[Path], ArtifactPattern]


class ArtifactRegistry:
    """
    Registry for artifact classifiers.

    Classifiers are evaluated in registration order. The first classifier
    returning a value other than ``ArtifactPattern.UNKNOWN`` determines
    the artifact type.
    """

    def __init__(self) -> None:
        """
        Create an empty registry.
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
            Callable accepting a filesystem path and returning an
            ``ArtifactPattern``.
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
        Classify a filesystem path.

        Parameters
        ----------
        path
            Path to classify.

        Returns
        -------
        ArtifactPattern
            First matching artifact pattern or
            ``ArtifactPattern.UNKNOWN``.
        """
        for classifier in self._classifiers:
            result = classifier(path)

            if result != ArtifactPattern.UNKNOWN:
                return result

        return ArtifactPattern.UNKNOWN

    def create(
        self,
        path: Path,
    ) -> Artifact:
        """
        Construct an Artifact.

        Parameters
        ----------
        path
            Filesystem path.

        Returns
        -------
        Artifact
            Newly created artifact.
        """
        pattern = self.classify(path)

        artifact = Artifact(
            path=path,
        )

        # Preserve compatibility with Artifact models that expose a
        # writable ``pattern`` attribute while remaining safe for models
        # that do not.
        if hasattr(artifact, "pattern"):
            try:
                object.__setattr__(
                    artifact,
                    "pattern",
                    pattern,
                )
            except (AttributeError, TypeError):
                pass

        return artifact


__all__ = [
    "ArtifactRegistry",
]

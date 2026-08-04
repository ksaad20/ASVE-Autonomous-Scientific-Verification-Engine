"""
Artifact registry.

Maintains an ordered collection of artifact classifiers and constructs
Artifact objects from discovered filesystem paths.

The registry preserves backwards compatibility with earlier ASVE
releases while providing a deterministic implementation suitable for
current and future scanner architectures.
"""

from __future__ import annotations

from collections.abc import Callable
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
    the artifact pattern associated with the supplied path.
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
            Callable accepting a filesystem path and returning an
            ``ArtifactPattern``.
        """
        self._classifiers.append(
            classifier,
        )

    def clear(self) -> None:
        """
        Remove every registered classifier.
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
            First matching artifact pattern, otherwise
            ``ArtifactPattern.UNKNOWN``.
        """
        for classifier in self._classifiers:
            result = classifier(
                path,
            )

            if result != ArtifactPattern.UNKNOWN:
                return result

        return ArtifactPattern.UNKNOWN

    def create(
        self,
        path: Path,
    ) -> Artifact:
        """
        Construct an artifact from a filesystem path.

        Parameters
        ----------
        path
            Path representing a discovered artifact.

        Returns
        -------
        Artifact
            Constructed artifact instance.
        """
        pattern = self.classify(
            path,
        )

        artifact = Artifact(
            path=path,
        )

        if hasattr(
            artifact,
            "pattern",
        ):
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


__all__ = [
    "ArtifactRegistry",
]

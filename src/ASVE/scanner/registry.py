"""
ASVE scanner registry.

This module manages artifact classification handlers used by the
scanner subsystem.

The registry provides an extension point for future plugins.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from asve.scanner.patterns import ArtifactPattern
from asve.scanner.patterns import classify_path


Classifier = Callable[
    [Path],
    ArtifactPattern,
]


class ArtifactRegistry:
    """
    Registry for artifact classification handlers.
    """

    def __init__(self) -> None:
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
            Artifact classification function.
        """
        self._classifiers.append(classifier)

    def classify(
        self,
        path: Path,
    ) -> ArtifactPattern:
        """
        Classify an artifact path.

        Parameters
        ----------
        path
            Artifact path.

        Returns
        -------
        ArtifactPattern
            Detected artifact type.
        """
        for classifier in self._classifiers:
            result = classifier(path)

            if result != ArtifactPattern.UNKNOWN:
                return result

        return ArtifactPattern.UNKNOWN

    def clear(self) -> None:
        """
        Remove registered classifiers.
        """
        self._classifiers.clear()

    def __len__(self) -> int:
        """
        Return number of classifiers.
        """
        return len(self._classifiers)


registry = ArtifactRegistry()

registry.register(classify_path)


__all__ = [
    "ArtifactRegistry",
    "registry",
]

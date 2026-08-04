"""
Artifact registry.

Creates Artifact objects from discovered filesystem paths.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import Artifact


class ArtifactRegistry:
    """
    Registry responsible for constructing artifacts.

    Future versions may dispatch to specialized artifact factories,
    but the current implementation provides deterministic Artifact
    creation for every discovered file.
    """

    def create(
        self,
        path: Path,
    ) -> Artifact:
        """
        Create an Artifact from a filesystem path.

        Parameters
        ----------
        path
            File to represent.

        Returns
        -------
        Artifact
            Newly created artifact.
        """
        return Artifact(
            path=path,
        )


__all__ = [
    "ArtifactRegistry",
]

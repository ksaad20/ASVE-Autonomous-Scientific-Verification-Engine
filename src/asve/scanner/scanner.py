"""
Artifact scanning utilities for ASVE.

The scanner walks project directories and creates artifact objects
through the configured artifact registry.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import Artifact
from asve.scanner.registry import ArtifactRegistry


class ArtifactScanner:
    """
    Discover artifacts within a project directory.
    """

    def __init__(
        self,
        registry: ArtifactRegistry,
    ) -> None:
        """
        Initialize the artifact scanner.

        Parameters
        ----------
        registry
            Registry used to create artifacts from discovered files.
        """
        self.registry = registry

    def scan(
        self,
        path: Path,
    ) -> list[Artifact]:
        """
        Scan a project directory for artifacts.

        Parameters
        ----------
        path
            Directory to scan.

        Returns
        -------
        list[Artifact]
            Discovered artifacts in deterministic path order.
        """
        if not path.exists() or not path.is_dir():
            return []

        artifacts: list[Artifact] = []

        for file_path in sorted(path.rglob("*")):
            if not file_path.is_file():
                continue

            artifact = self.registry.create(file_path)

            if artifact is not None:
                artifacts.append(artifact)

        return artifacts


class Scanner(ArtifactScanner):
    """
    Backward-compatible scanner name.
    """


__all__ = [
    "ArtifactScanner",
    "Scanner",
]

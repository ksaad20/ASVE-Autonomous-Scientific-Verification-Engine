"""
Project scanner implementation for ASVE.

The scanner discovers project artifacts and returns
portable artifact collections for downstream verification.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import Artifact
from asve.scanner.registry import ArtifactRegistry


class Scanner:
    """
    Discover artifacts inside a project directory.
    """

    def __init__(
        self,
        registry: ArtifactRegistry,
    ) -> None:
        """
        Initialize scanner.

        Parameters
        ----------
        registry
            Artifact detection registry.
        """
        self.registry = registry

    def scan(
        self,
        path: Path,
    ) -> list[Artifact]:
        """
        Scan a project directory.

        Parameters
        ----------
        path
            Project path.

        Returns
        -------
        list[Artifact]
            Discovered artifacts.
        """
        artifacts: list[Artifact] = []

        if not path.exists() or not path.is_dir():
            return artifacts

        for file_path in sorted(
            path.rglob("*"),
        ):
            if not file_path.is_file():
                continue

            artifact = self.registry.detect(
                file_path,
            )

            if artifact is not None:
                artifacts.append(
                    artifact,
                )

        return artifacts


__all__ = [
    "Scanner",
]

"""
Project artifact scanner.

The scanner discovers files inside a project directory and converts
them into ASVE artifact representations.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from asve.models.artifact import Artifact
from asve.scanner.registry import ArtifactRegistry

__all__ = [
    "Scanner",
]


class Scanner:
    """
    Scan project directories for artifacts.
    """

    def __init__(
        self,
        registry: ArtifactRegistry,
    ) -> None:
        """
        Initialize scanner with an artifact registry.
        """
        self.registry = registry

    def scan(
        self,
        path: Path,
    ) -> list[Artifact]:
        """
        Scan a directory and return discovered artifacts.

        Empty directories return an empty list.
        """
        if not path.exists() or not path.is_dir():
            return []

        artifacts: list[Artifact] = []

        for file_path in self._iter_files(path):
            artifact = self.registry.create(
                file_path,
            )

            if artifact is not None:
                artifacts.append(
                    artifact,
                )

        return artifacts

    def _iter_files(
        self,
        path: Path,
    ) -> Iterable[Path]:
        """
        Yield files eligible for scanning.
        """
        for item in sorted(path.rglob("*")):
            if item.is_file():
                yield item

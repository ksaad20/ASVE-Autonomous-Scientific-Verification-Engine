"""
ASVE artifact scanner.

Scans project directories for supported scientific artifacts.
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
        registry: ArtifactRegistry | None = None,
    ) -> None:
        """
        Create a scanner.

        Parameters
        ----------
        registry
            Optional artifact registry. If omitted, a default registry
            is created automatically.
        """
        self.registry = registry or ArtifactRegistry()

    def scan(
        self,
        path: Path,
    ) -> list[Artifact]:
        """
        Scan a project directory.

        Parameters
        ----------
        path
            Directory to scan.

        Returns
        -------
        list[Artifact]
            Discovered artifacts in deterministic order.
        """
        if not path.exists():
            return []

        if not path.is_dir():
            return []

        artifacts: list[Artifact] = []

        for file_path in sorted(path.rglob("*")):
            if not file_path.is_file():
                continue

            if any(part.startswith(".") for part in file_path.parts):
                continue

            create = getattr(
                self.registry,
                "create",
                None,
            )

            if callable(create):
                artifact = create(file_path)

                if artifact is not None:
                    artifacts.append(artifact)

        return artifacts


# Backwards compatibility
Scanner = ArtifactScanner

__all__ = [
    "ArtifactScanner",
    "Scanner",
]

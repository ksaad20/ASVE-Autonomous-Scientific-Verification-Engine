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
    Discover scientific artifacts within a project directory.
    """

    def __init__(
        self,
        registry: ArtifactRegistry | None = None,
    ) -> None:
        """
        Create an artifact scanner.

        Parameters
        ----------
        registry
            Artifact registry used to classify and construct artifacts.
            If omitted, a default registry is created.
        """
        self.registry = registry or ArtifactRegistry()

    def scan(
        self,
        path: str | Path,
    ) -> list[Artifact] | tuple[()]:
        """
        Scan a project directory.

        Parameters
        ----------
        path
            Filesystem path to scan.

        Returns
        -------
        list[Artifact] | tuple[()]
            Artifacts discovered in deterministic order. Returns an
            empty tuple for missing or invalid paths for backwards
            compatibility.
        """
        path = Path(path)

        if not path.exists():
            return ()

        if not path.is_dir():
            return ()

        artifacts: list[Artifact] = []

        create = getattr(
            self.registry,
            "create",
            None,
        )

        classify = getattr(
            self.registry,
            "classify",
            None,
        )

        for file_path in sorted(path.rglob("*")):
            if not file_path.is_file():
                continue

            if any(part.startswith(".") for part in file_path.parts):
                continue

            artifact: Artifact | None = None

            if callable(create):
                artifact = create(file_path)

            elif callable(classify):
                artifact = classify(file_path)

            if artifact is not None:
                artifacts.append(artifact)

        return artifacts


# Backwards compatibility
Scanner = ArtifactScanner

__all__ = [
    "ArtifactScanner",
    "Scanner",
]

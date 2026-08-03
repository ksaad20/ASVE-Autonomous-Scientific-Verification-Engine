"""Artifact scanner for ASVE.

Discovers scientific artifacts within a project directory while
respecting ignore patterns (e.g., version-control metadata).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.models.artifact import Artifact


class ArtifactScanner:
    """Discovers files and directories that constitute scientific artifacts.

    Hidden directories (those starting with ``.``) are skipped to avoid
    version-control metadata and transient files.

    Examples
    --------
    >>> scanner = ArtifactScanner()
    >>> artifacts = scanner.scan("./project")
    >>> len(artifacts) >= 0
    True

    """

    def __init__(
        self,
        registry: Any | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the scanner.

        Parameters
        ----------
        registry : Any or None
            Optional artifact registry for lookups.
        **kwargs : Any
            Reserved for future extension.

        """
        self._registry = registry

    def scan(self, path: str | Path) -> tuple[Artifact, ...]:
        """Scan *path* for discoverable artifacts.

        Parameters
        ----------
        path : str or pathlib.Path
            Project root to scan.

        Returns
        -------
        tuple[Artifact, ...]
            Discovered artifacts. Returns an empty tuple if *path*
            does not exist.

        """
        project_path = Path(path)
        if not project_path.exists():
            return ()

        artifacts: list[Artifact] = []
        for file_path in project_path.rglob("*"):
            if not file_path.is_file():
                continue

            rel_parts = file_path.relative_to(project_path).parts
            if any(part.startswith(".") for part in rel_parts):
                continue

            artifacts.append(Artifact(path=file_path))

        return tuple(artifacts)


# Backwards-compatible alias used by older tests.
Scanner = ArtifactScanner

__all__ = [
    "ArtifactScanner",
    "Scanner",
]

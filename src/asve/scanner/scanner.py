"""
ASVE artifact scanner.

This module discovers files inside scientific projects and converts
them into ASVE artifact representations.

The scanner is intentionally separated from parsing and extraction.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import Artifact
from asve.scanner.ignore import IgnoreMatcher


class ArtifactScanner:
    """
    Discover scientific artifacts in a project directory.
    """

    def __init__(
        self,
        ignore_matcher: IgnoreMatcher | None = None,
    ) -> None:
        self._ignore_matcher = (
            ignore_matcher
            or IgnoreMatcher()
        )

    def scan(
        self,
        project_path: str | Path,
    ) -> tuple[Artifact, ...]:
        """
        Scan a project directory.

        Parameters
        ----------
        project_path
            Root project directory.

        Returns
        -------
        tuple[Artifact, ...]
            Discovered artifacts.
        """
        root = Path(project_path)

        if not root.exists():
            return ()

        artifacts: list[Artifact] = []

        for path in root.rglob("*"):
            if not path.is_file():
                continue

            if self._ignore_matcher.matches(path):
                continue

            artifacts.append(
                Artifact(
                    path=path,
                )
            )

        return tuple(artifacts)

Scanner = ArtifactScanner

__all__ = [
    "Scanner",
    "ArtifactScanner"
]

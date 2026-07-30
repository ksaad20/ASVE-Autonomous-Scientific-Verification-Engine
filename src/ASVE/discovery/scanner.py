"""
Filesystem scanner for ASVE.

This module is responsible for deterministic filesystem discovery.
It recursively scans a research project and returns candidate artifact
paths. Parsing, classification, and graph construction are handled by
later stages of the ASVE pipeline.

The scanner intentionally performs no semantic analysis.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path


class ProjectScanner:
    """
    Deterministically scan a research project.

    Parameters
    ----------
    root
        Root directory of the research project.
    """

    def __init__(self, root: str | Path) -> None:
        self._root = Path(root).resolve()

    @property
    def root(self) -> Path:
        """Return the project root directory."""
        return self._root

    def scan(self) -> tuple[Path, ...]:
        """
        Discover all files beneath the project root.

        Returns
        -------
        tuple[Path, ...]
            Sorted collection of discovered files.
        """
        files = sorted(
            path
            for path in self._root.rglob("*")
            if path.is_file()
        )

        return tuple(files)

    def iter_files(self) -> Iterator[Path]:
        """
        Iterate over discovered files.

        Yields
        ------
        Path
            One discovered file at a time.
        """
        yield from self.scan()

    def exists(self) -> bool:
        """
        Return True if the project root exists.
        """
        return self._root.exists()

    def __len__(self) -> int:
        """
        Return the number of discovered files.
        """
        return len(self.scan())

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"root={self.root!s})"
        )


__all__ = [
    "ProjectScanner",
  ]

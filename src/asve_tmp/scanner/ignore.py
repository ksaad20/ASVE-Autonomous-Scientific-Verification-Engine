"""
ASVE scanner ignore rules.

This module provides path filtering for artifact discovery.

Ignore matching is intentionally lightweight and deterministic.
Future versions may support .gitignore-compatible patterns.
"""

from __future__ import annotations

from pathlib import Path


_DEFAULT_IGNORED_NAMES = frozenset(
    {
        ".git",
        ".svn",
        ".hg",
        ".venv",
        "venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "build",
        "dist",
    }
)


class IgnoreMatcher:
    """
    Determine whether paths should be ignored.
    """

    def __init__(
        self,
        ignored_names: frozenset[str]
        | None = None,
    ) -> None:
        self._ignored_names = (
            ignored_names
            or _DEFAULT_IGNORED_NAMES
        )

    def matches(
        self,
        path: Path,
    ) -> bool:
        """
        Check whether a path should be ignored.

        Parameters
        ----------
        path
            File or directory path.

        Returns
        -------
        bool
            True if ignored.
        """
        return any(
            part in self._ignored_names
            for part in path.parts
        )

    def add(
        self,
        name: str,
    ) -> None:
        """
        Add an ignored path name.

        Parameters
        ----------
        name
            Directory or file name.
        """
        self._ignored_names = (
            *self._ignored_names,
            name,
        )


__all__ = [
    "IgnoreMatcher",
]

"""
Project abstraction for ASVE.

This module defines the public Project API for the Automated Scientific
Verification Engine (ASVE).

A Project represents a scientific research workspace containing
manuscripts, software, datasets, notebooks, and other computational
artifacts.

The Project class acts as the primary orchestration interface while
delegating implementation details to dedicated discovery, verification,
graph, and reporting components.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

from asve.config import ASVEConfig
from asve.config import DEFAULT_CONFIG


class Project:
    """
    Representation of an ASVE research project.

    Parameters
    ----------
    root
        Root directory of the project.

    config
        ASVE configuration.
    """

    def __init__(
        self,
        root: str | Path = ".",
        *,
        config: ASVEConfig = DEFAULT_CONFIG,
    ) -> None:
        self._root: Final[Path] = Path(root).resolve()
        self._config: Final[ASVEConfig] = config

    @property
    def root(self) -> Path:
        """
        Return the absolute project directory.
        """
        return self._root

    @property
    def config(self) -> ASVEConfig:
        """
        Return the project configuration.
        """
        return self._config

    def discover(self) -> "Project":
        """
        Discover research artifacts.

        Returns
        -------
        Project
            Self, enabling fluent chaining.
        """
        return self

    def build_graph(self) -> "Project":
        """
        Build the scientific dependency graph.

        Returns
        -------
        Project
            Self, enabling fluent chaining.
        """
        return self

    def verify(self) -> "Project":
        """
        Execute scientific verification.

        Returns
        -------
        Project
            Self, enabling fluent chaining.
        """
        return self

    def report(self) -> "Project":
        """
        Generate verification reports.

        Returns
        -------
        Project
            Self, enabling fluent chaining.
        """
        return self

    def summary(self) -> str:
        """
        Return a human-readable project summary.
        """
        return (
            "ASVE Project\n"
            f"Root: {self.root}\n"
            "Status: Ready"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"root={self.root!s})"
        )


__all__ = [
    "Project",
]

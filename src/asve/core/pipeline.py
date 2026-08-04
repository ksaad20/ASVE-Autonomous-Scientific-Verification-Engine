"""
ASVE analysis pipeline.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.core.analyzer import Analyzer
from asve.core.config import ASVEConfig


class ASVEPipeline:
    """
    High-level analysis pipeline.
    """

    def __init__(
        self,
        config: ASVEConfig | None = None,
    ) -> None:
        """
        Initialize the pipeline.

        Parameters
        ----------
        config
            Optional pipeline configuration.
        """
        self.config = config or ASVEConfig()
        self.analyzer = Analyzer()

    def run(
        self,
        project: Path,
    ) -> Any:
        """
        Analyze a project.

        Parameters
        ----------
        project
            Project directory.

        Returns
        -------
        Any
            Analysis result.
        """
        return self.analyzer.analyze(project)

    def analyze(
        self,
        project: Path,
    ) -> Any:
        """
        Compatibility alias for ``run()``.
        """
        return self.run(project)


__all__ = [
    "ASVEPipeline",
]

"""
ASVE analysis pipeline.

Coordinates the complete ASVE verification workflow.

Pipeline responsibilities
-------------------------
1. Scan the project for artifacts.
2. Build an analysis context.
3. Execute the analysis engine.
4. Run verification.
5. Return a verification report.

The pipeline intentionally orchestrates components without embedding
their implementation details.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.analyzer import Analyzer
from asve.core.config import ASVEConfig
from asve.core.context import AnalysisContext
from asve.graph.graph import ScientificGraph
from asve.scanner.registry import ArtifactRegistry
from asve.scanner.scanner import Scanner
from asve.verification.report import VerificationReport


class ASVEPipeline:
    """
    Complete ASVE verification pipeline.
    """

    def __init__(
        self,
        config: ASVEConfig | None = None,
    ) -> None:
        """
        Create a pipeline instance.

        Parameters
        ----------
        config
            Optional ASVE configuration.
        """
        self.config = config or ASVEConfig()

        self.registry = ArtifactRegistry()
        self.scanner = Scanner(
            registry=self.registry,
        )

        self.analyzer = Analyzer()

    def run(
        self,
        project: Path,
    ) -> VerificationReport:
        """
        Execute the complete verification workflow.

        Parameters
        ----------
        project
            Project directory.

        Returns
        -------
        VerificationReport
            Verification results.
        """
        artifacts = self.scanner.scan(
            project,
        )

        context = AnalysisContext(
            project=project,
            artifacts=artifacts,
            graph=ScientificGraph(),
        )

        graph = self.analyzer.analyze(
            context,
        )

        report = VerificationReport()

        # Future versions populate findings from graph verification.
        _ = graph

        return report

    def analyze(
        self,
        project: Path,
    ) -> VerificationReport:
        """
        Analyze a project.

        This method exists for backwards compatibility.

        Parameters
        ----------
        project
            Project directory.

        Returns
        -------
        VerificationReport
            Verification report.
        """
        return self.run(
            project,
        )


__all__ = [
    "ASVEPipeline",
]

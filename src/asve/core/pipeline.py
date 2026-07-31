"""
ASVE analysis pipeline.

This module provides the high-level workflow coordinator that connects
artifact discovery, extraction, graph construction, and verification.

The pipeline is intentionally lightweight and delegates domain logic
to specialized subsystems.
"""

from __future__ import annotations

from pathlib import Path

from asve.graph.graph import ScientificGraph
from asve.verification.engine import VerificationEngine
from asve.verification.report import VerificationReport


class ASVEPipeline:
    """
    Main ASVE reproducibility analysis pipeline.
    """

    def __init__(
        self,
        verification_engine: VerificationEngine | None = None,
    ) -> None:
        self._verification_engine = (
            verification_engine
            or VerificationEngine()
        )

    def analyze(
        self,
        project_path: str | Path,
    ) -> VerificationReport:
        """
        Analyze a scientific project.

        Parameters
        ----------
        project_path
            Root directory of the research project.

        Returns
        -------
        VerificationReport
            Verification results.
        """
        graph = self._build_graph(
            project_path,
        )

        findings = (
            self._verification_engine.verify(
                graph,
            )
        )

        return VerificationReport.from_findings(
            findings,
        )

    def _build_graph(
        self,
        project_path: str | Path,
    ) -> ScientificGraph:
        """
        Build scientific dependency graph.

        This method is intentionally isolated so future versions can
        integrate scanner, parser, extractor, and graph builder
        implementations.
        """
        _ = Path(project_path)

        return ScientificGraph()


__all__ = [
    "ASVEPipeline",
]

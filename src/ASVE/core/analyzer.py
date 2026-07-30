"""
ASVE analysis worker.

This module performs the internal analysis workflow by converting
scientific artifacts into a Scientific Dependency Graph.

The analyzer is intentionally separated from the pipeline. The
pipeline manages orchestration, while the analyzer performs the
artifact-to-graph transformation.
"""

from __future__ import annotations

from collections.abc import Iterable

from asve.core.context import AnalysisContext
from asve.graph.graph import ScientificGraph
from asve.models.artifact import Artifact


class ASVEAnalyzer:
    """
    Internal ASVE analysis engine.

    Converts discovered artifacts into graph representations.
    """

    def analyze(
        self,
        context: AnalysisContext,
    ) -> ScientificGraph:
        """
        Analyze artifacts and construct a graph.

        Parameters
        ----------
        context
            Active analysis context.

        Returns
        -------
        ScientificGraph
            Generated scientific dependency graph.
        """
        graph = context.graph

        for artifact in self._artifacts(
            context.artifacts,
        ):
            self._process_artifact(
                artifact,
                graph,
            )

        return graph

    def _artifacts(
        self,
        artifacts: Iterable[Artifact],
    ) -> Iterable[Artifact]:
        """
        Iterate over discovered artifacts.

        Isolated for future filtering and prioritization.
        """
        return artifacts

    def _process_artifact(
        self,
        artifact: Artifact,
        graph: ScientificGraph,
    ) -> None:
        """
        Process a single artifact.

        Parser, extractor, and graph builder integrations are added
        here through dependency injection in future versions.
        """
        _ = artifact
        _ = graph


__all__ = [
    "ASVEAnalyzer",
]

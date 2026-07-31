"""
Tests for the ASVE analysis engine.

These tests validate artifact-to-graph processing behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.analyzer import ASVEAnalyzer
from asve.core.context import AnalysisContext
from asve.graph.graph import ScientificGraph
from asve.models.artifact import Artifact


def test_analyzer_returns_graph(
    tmp_path: Path,
) -> None:
    """
    Analyzer should return a ScientificGraph.
    """
    artifact_path = (
        tmp_path
        / "analysis.py"
    )

    artifact_path.write_text(
        "print('analysis')",
        encoding="utf-8",
    )

    artifact = Artifact(
        path=artifact_path,
    )

    context = AnalysisContext(
        project_path=tmp_path,
        artifacts=[
            artifact,
        ],
        graph=ScientificGraph(),
    )

    analyzer = ASVEAnalyzer()

    graph = analyzer.analyze(
        context,
    )

    assert isinstance(
        graph,
        ScientificGraph,
    )


def test_analyzer_handles_empty_context(
    tmp_path: Path,
) -> None:
    """
    Analyzer should handle projects without artifacts.
    """
    context = AnalysisContext(
        project_path=tmp_path,
        graph=ScientificGraph(),
    )

    analyzer = ASVEAnalyzer()

    graph = analyzer.analyze(
        context,
    )

    assert isinstance(
        graph,
        ScientificGraph,
    )


def test_analyzer_preserves_context_graph(
    tmp_path: Path,
) -> None:
    """
    Analyzer should operate on the existing context graph.
    """
    existing_graph = ScientificGraph()

    context = AnalysisContext(
        project_path=tmp_path,
        graph=existing_graph,
    )

    analyzer = ASVEAnalyzer()

    result = analyzer.analyze(
        context,
    )

    assert result is existing_graph

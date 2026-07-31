"""
Tests for the ASVE analysis context.

These tests verify runtime state management.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.context import AnalysisContext
from asve.graph.graph import ScientificGraph
from asve.models.artifact import Artifact


def test_context_initializes_with_project(
    tmp_path: Path,
) -> None:
    """
    Context should store project location.
    """
    context = AnalysisContext(
        project_path=tmp_path,
    )

    assert context.project_path == tmp_path


def test_context_stores_graph(
    tmp_path: Path,
) -> None:
    """
    Context should preserve graph state.
    """
    graph = ScientificGraph()

    context = AnalysisContext(
        project_path=tmp_path,
        graph=graph,
    )

    assert context.graph is graph


def test_context_adds_artifact(
    tmp_path: Path,
) -> None:
    """
    Context should register artifacts.
    """
    artifact_path = (
        tmp_path
        / "paper.py"
    )

    artifact_path.write_text(
        "print('test')",
        encoding="utf-8",
    )

    artifact = Artifact(
        path=artifact_path,
    )

    context = AnalysisContext(
        project_path=tmp_path,
    )

    context.add_artifact(
        artifact,
    )

    assert len(
        context.artifacts,
    ) == 1

    assert (
        context.artifacts[0]
        == artifact
    )


def test_context_metadata_default(
    tmp_path: Path,
) -> None:
    """
    Context should initialize metadata safely.
    """
    context = AnalysisContext(
        project_path=tmp_path,
    )

    assert context.metadata == {}

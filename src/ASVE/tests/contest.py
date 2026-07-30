"""
Shared pytest fixtures for ASVE.

This module provides reusable testing resources for scanner,
verification, graph, and pipeline tests.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from asve.graph.graph import ScientificGraph
from asve.models.artifact import Artifact


@pytest.fixture
def temporary_project(
    tmp_path: Path,
) -> Path:
    """
    Create a minimal scientific project.

    Parameters
    ----------
    tmp_path
        Pytest temporary directory.

    Returns
    -------
    Path
        Project directory.
    """
    project = tmp_path / "project"

    project.mkdir()

    (project / "paper.md").write_text(
        "# Example Research Project\n",
        encoding="utf-8",
    )

    (project / "analysis.py").write_text(
        "print('analysis')\n",
        encoding="utf-8",
    )

    return project


@pytest.fixture
def empty_graph() -> ScientificGraph:
    """
    Return an empty scientific graph.
    """
    return ScientificGraph()


@pytest.fixture
def sample_artifact(
    tmp_path: Path,
) -> Artifact:
    """
    Create a sample artifact.
    """
    path = tmp_path / "example.py"

    path.write_text(
        "print('hello')\n",
        encoding="utf-8",
    )

    return Artifact(
        path=path,
    )

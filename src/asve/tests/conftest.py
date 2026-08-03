"""Pytest fixtures for ASVE test suite.

Provides reusable test infrastructure shared across modules.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from asve.graph.graph import ScientificGraph


@pytest.fixture
def temporary_project(
    tmp_path: Path,
) -> Path:
    """Create a minimal scientific project for testing.

    Returns
    -------
    pathlib.Path
        Directory containing ``paper.md`` and ``analysis.py``.

    """
    paper = tmp_path / "paper.md"
    paper.write_text(
        "# Research Paper\n\nAbstract.\n",
        encoding="utf-8",
    )

    analysis = tmp_path / "analysis.py"
    analysis.write_text(
        "def calculate(value):\n    return value * 2\n",
        encoding="utf-8",
    )

    return tmp_path


@pytest.fixture
def empty_graph() -> ScientificGraph:
    """Return an empty scientific dependency graph."""
    return ScientificGraph()

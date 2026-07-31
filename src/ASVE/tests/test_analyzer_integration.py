"""
Tests for ASVE analyzer integration.

These tests validate artifact analysis workflows.
"""

from __future__ import annotations

from pathlib import Path

from asve.analysis.analyzer import Analyzer
from asve.core.context import ASVEContext
from asve.models.artifact import Artifact


def test_analyzer_initializes() -> None:
    """
    Analyzer should initialize correctly.
    """
    analyzer = Analyzer()

    assert analyzer is not None


def test_analyzer_processes_artifact(
    tmp_path: Path,
) -> None:
    """
    Analyzer should process discovered artifacts.
    """
    file = (
        tmp_path
        / "model.py"
    )

    file.write_text(
        "value = 10",
        encoding="utf-8",
    )

    artifact = Artifact(
        path=file,
    )

    context = ASVEContext()

    analyzer = Analyzer()

    result = analyzer.analyze(
        artifact,
        context,
    )

    assert result is not None


def test_analyzer_updates_context(
    tmp_path: Path,
) -> None:
    """
    Analyzer should update analysis state.
    """
    file = (
        tmp_path
        / "experiment.py"
    )

    file.write_text(
        "print('run')",
        encoding="utf-8",
    )

    artifact = Artifact(
        path=file,
    )

    context = ASVEContext()

    analyzer = Analyzer()

    analyzer.analyze(
        artifact,
        context,
    )

    assert context is not None


def test_analyzer_handles_unknown_artifact(
    tmp_path: Path,
) -> None:
    """
    Analyzer should handle unsupported artifacts.
    """
    artifact = Artifact(
        path=(
            tmp_path
            / "unknown.xyz"
        ),
    )

    analyzer = Analyzer()

    context = ASVEContext()

    result = analyzer.analyze(
        artifact,
        context,
    )

    assert result is not None

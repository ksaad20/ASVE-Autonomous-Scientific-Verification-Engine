"""
Tests for the ASVE analysis pipeline.

These tests verify the integration between core components.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.pipeline import ASVEPipeline


def test_pipeline_analyzes_project(
    temporary_project: Path,
) -> None:
    """
    Pipeline should analyze a scientific project.
    """
    pipeline = ASVEPipeline()

    report = pipeline.analyze(
        temporary_project,
    )

    assert report is not None


def test_pipeline_handles_empty_project(
    tmp_path: Path,
) -> None:
    """
    Pipeline should handle empty projects.
    """
    project = (
        tmp_path
        / "empty_project"
    )

    project.mkdir()

    pipeline = ASVEPipeline()

    report = pipeline.analyze(
        project,
    )

    assert report is not None


def test_pipeline_accepts_string_path(
    temporary_project: Path,
) -> None:
    """
    Pipeline should accept string paths.
    """
    pipeline = ASVEPipeline()

    report = pipeline.analyze(
        str(temporary_project),
    )

    assert report is not None

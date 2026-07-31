"""
Tests for ASVE pipeline integration.

These tests validate end-to-end component coordination.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.pipeline import ASVEPipeline
from asve.core.config import ASVEConfig
from asve.verification.report import VerificationReport


def test_pipeline_initialization(
    tmp_path: Path,
) -> None:
    """
    Pipeline should initialize with configuration.
    """
    config = ASVEConfig()

    pipeline = ASVEPipeline(
        config=config,
    )

    assert pipeline is not None


def test_pipeline_runs_on_project(
    tmp_path: Path,
) -> None:
    """
    Pipeline should analyze a project directory.
    """
    source = (
        tmp_path
        / "analysis.py"
    )

    source.write_text(
        "print('test')",
        encoding="utf-8",
    )

    pipeline = ASVEPipeline(
        config=ASVEConfig(),
    )

    report = pipeline.run(
        tmp_path,
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_pipeline_handles_empty_project(
    tmp_path: Path,
) -> None:
    """
    Pipeline should handle empty projects.
    """
    pipeline = ASVEPipeline(
        config=ASVEConfig(),
    )

    report = pipeline.run(
        tmp_path,
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_pipeline_produces_repeatable_results(
    tmp_path: Path,
) -> None:
    """
    Identical inputs should produce stable outputs.
    """
    pipeline = ASVEPipeline(
        config=ASVEConfig(),
    )

    first = pipeline.run(
        tmp_path,
    )

    second = pipeline.run(
        tmp_path,
    )

    assert (
        first.total_findings
        ==
        second.total_findings
    )

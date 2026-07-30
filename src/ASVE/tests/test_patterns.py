"""
Tests for ASVE artifact classification patterns.

These tests verify deterministic file-type classification.
"""

from __future__ import annotations

from pathlib import Path

from asve.scanner.patterns import ArtifactPattern
from asve.scanner.patterns import classify_path


def test_classifies_python_source() -> None:
    """
    Python files should be classified correctly.
    """
    result = classify_path(
        Path("analysis.py"),
    )

    assert result == ArtifactPattern.PYTHON


def test_classifies_latex_manuscript() -> None:
    """
    LaTeX files should be identified as manuscripts.
    """
    result = classify_path(
        Path("paper.tex"),
    )

    assert result == ArtifactPattern.LATEX


def test_classifies_notebook() -> None:
    """
    Notebook files should be detected.
    """
    result = classify_path(
        Path("experiment.ipynb"),
    )

    assert result == ArtifactPattern.NOTEBOOK


def test_classifies_dataset() -> None:
    """
    Dataset files should be detected.
    """
    csv_result = classify_path(
        Path("measurements.csv"),
    )

    tsv_result = classify_path(
        Path("measurements.tsv"),
    )

    assert csv_result == ArtifactPattern.DATASET
    assert tsv_result == ArtifactPattern.DATASET


def test_classifies_configuration() -> None:
    """
    Configuration files should be detected.
    """
    result = classify_path(
        Path("environment.yaml"),
    )

    assert result == ArtifactPattern.CONFIGURATION


def test_unknown_extension_returns_unknown() -> None:
    """
    Unsupported extensions should return UNKNOWN.
    """
    result = classify_path(
        Path("archive.xyz"),
    )

    assert result == ArtifactPattern.UNKNOWN

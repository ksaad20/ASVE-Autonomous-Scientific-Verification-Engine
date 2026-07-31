"""
Tests for the ASVE artifact scanner.

These tests verify deterministic project discovery behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.scanner.scanner import ArtifactScanner


def test_scanner_discovers_files(
    temporary_project: Path,
) -> None:
    """
    Scanner should discover project files.
    """
    scanner = ArtifactScanner()

    artifacts = scanner.scan(
        temporary_project,
    )

    artifact_paths = {
        artifact.path.name
        for artifact in artifacts
    }

    assert "paper.md" in artifact_paths
    assert "analysis.py" in artifact_paths


def test_scanner_ignores_hidden_metadata(
    temporary_project: Path,
) -> None:
    """
    Scanner should ignore version-control directories.
    """
    git_directory = (
        temporary_project
        / ".git"
    )

    git_directory.mkdir()

    ignored_file = (
        git_directory
        / "config"
    )

    ignored_file.write_text(
        "metadata",
        encoding="utf-8",
    )

    scanner = ArtifactScanner()

    artifacts = scanner.scan(
        temporary_project,
    )

    artifact_paths = {
        artifact.path
        for artifact in artifacts
    }

    assert ignored_file not in artifact_paths


def test_scanner_returns_empty_for_missing_path(
    tmp_path: Path,
) -> None:
    """
    Scanner should handle missing projects safely.
    """
    scanner = ArtifactScanner()

    artifacts = scanner.scan(
        tmp_path / "missing",
    )

    assert artifacts == ()

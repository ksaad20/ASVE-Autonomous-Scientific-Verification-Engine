"""
Tests for ASVE scanner integration.

These tests validate filesystem artifact discovery.
"""

from __future__ import annotations

from pathlib import Path

from asve.scanner.scanner import Scanner
from asve.scanner.registry import ArtifactRegistry


def test_scanner_initializes() -> None:
    """
    Scanner should initialize correctly.
    """
    scanner = Scanner(
        registry=ArtifactRegistry(),
    )

    assert scanner is not None


def test_scanner_discovers_files(
    tmp_path: Path,
) -> None:
    """
    Scanner should discover project files.
    """
    file = (
        tmp_path
        / "analysis.py"
    )

    file.write_text(
        "print('test')",
        encoding="utf-8",
    )

    scanner = Scanner(
        registry=ArtifactRegistry(),
    )

    artifacts = scanner.scan(
        tmp_path,
    )

    assert len(artifacts) >= 1


def test_scanner_handles_empty_directory(
    tmp_path: Path,
) -> None:
    """
    Empty projects should scan safely.
    """
    scanner = Scanner(
        registry=ArtifactRegistry(),
    )

    artifacts = scanner.scan(
        tmp_path,
    )

    assert isinstance(
        artifacts,
        list,
    )


def test_scanner_is_deterministic(
    tmp_path: Path,
) -> None:
    """
    Same input should produce stable results.
    """
    (
        tmp_path
        / "file.py"
    ).write_text(
        "x = 1",
        encoding="utf-8",
    )

    scanner = Scanner(
        registry=ArtifactRegistry(),
    )

    first = scanner.scan(
        tmp_path,
    )

    second = scanner.scan(
        tmp_path,
    )

    assert len(first) == len(second)

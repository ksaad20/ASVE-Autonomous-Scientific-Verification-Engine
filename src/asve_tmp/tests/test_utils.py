"""
Tests for ASVE utility functions.

These tests validate common helper behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.utils.hashing import hash_file
from asve.utils.paths import normalize_path
from asve.utils.identifiers import generate_id


def test_normalize_path(
    tmp_path: Path,
) -> None:
    """
    Path normalization should return a stable path.
    """
    file_path = (
        tmp_path
        / "example.py"
    )

    normalized = normalize_path(
        file_path,
    )

    assert isinstance(
        normalized,
        Path,
    )


def test_hash_file(
    tmp_path: Path,
) -> None:
    """
    File hashing should return a digest.
    """
    file_path = (
        tmp_path
        / "data.txt"
    )

    file_path.write_text(
        "scientific data",
        encoding="utf-8",
    )

    digest = hash_file(
        file_path,
    )

    assert isinstance(
        digest,
        str,
    )

    assert len(digest) > 0


def test_hash_changes_with_content(
    tmp_path: Path,
) -> None:
    """
    Different contents should produce different hashes.
    """
    first = (
        tmp_path
        / "first.txt"
    )

    second = (
        tmp_path
        / "second.txt"
    )

    first.write_text(
        "A",
        encoding="utf-8",
    )

    second.write_text(
        "B",
        encoding="utf-8",
    )

    assert (
        hash_file(first)
        != hash_file(second)
    )


def test_identifier_generation() -> None:
    """
    Identifier generator should create values.
    """
    identifier = generate_id()

    assert isinstance(
        identifier,
        str,
    )

    assert len(identifier) > 0

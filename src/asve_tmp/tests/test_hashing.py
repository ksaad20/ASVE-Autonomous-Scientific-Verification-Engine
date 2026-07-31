"""
Tests for ASVE hashing utilities.

These tests validate artifact fingerprinting.
"""

from __future__ import annotations

from pathlib import Path

from asve.utils.hashing import (
    hash_file,
    hash_text,
)


def test_hash_text_returns_value() -> None:
    """
    Text hashing should return a fingerprint.
    """
    result = hash_text(
        "scientific data",
    )

    assert isinstance(
        result,
        str,
    )

    assert len(
        result,
    ) > 0


def test_hash_text_is_deterministic() -> None:
    """
    Same input should generate same hash.
    """
    first = hash_text(
        "ASVE",
    )

    second = hash_text(
        "ASVE",
    )

    assert first == second


def test_different_text_has_different_hash() -> None:
    """
    Different inputs should generate different fingerprints.
    """
    first = hash_text(
        "input-a",
    )

    second = hash_text(
        "input-b",
    )

    assert first != second


def test_hash_file_returns_value(
    tmp_path: Path,
) -> None:
    """
    File hashing should work.
    """
    file = (
        tmp_path
        / "sample.txt"
    )

    file.write_text(
        "data",
        encoding="utf-8",
    )

    result = hash_file(
        file,
    )

    assert isinstance(
        result,
        str,
    )


def test_modified_file_changes_hash(
    tmp_path: Path,
) -> None:
    """
    File modifications should change fingerprints.
    """
    file = (
        tmp_path
        / "sample.txt"
    )

    file.write_text(
        "version one",
        encoding="utf-8",
    )

    first = hash_file(
        file,
    )

    file.write_text(
        "version two",
        encoding="utf-8",
    )

    second = hash_file(
        file,
    )

    assert first != second

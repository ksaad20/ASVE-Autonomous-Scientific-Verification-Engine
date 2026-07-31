"""
Tests for ASVE caching system.

These tests validate analysis result reuse behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.cache.manager import CacheManager


def test_cache_initializes(
    tmp_path: Path,
) -> None:
    """
    Cache manager should initialize.
    """
    cache = CacheManager(
        path=tmp_path,
    )

    assert cache is not None


def test_cache_stores_value(
    tmp_path: Path,
) -> None:
    """
    Cache should store results.
    """
    cache = CacheManager(
        path=tmp_path,
    )

    cache.set(
        "artifact_1",
        {
            "status": "complete",
        },
    )

    assert cache.exists(
        "artifact_1",
    )


def test_cache_retrieves_value(
    tmp_path: Path,
) -> None:
    """
    Cache should return stored data.
    """
    cache = CacheManager(
        path=tmp_path,
    )

    value = {
        "result": True,
    }

    cache.set(
        "analysis",
        value,
    )

    result = cache.get(
        "analysis",
    )

    assert result == value


def test_cache_invalidates_entry(
    tmp_path: Path,
) -> None:
    """
    Cache entries should be removable.
    """
    cache = CacheManager(
        path=tmp_path,
    )

    cache.set(
        "temporary",
        {
            "value": 1,
        },
    )

    cache.invalidate(
        "temporary",
    )

    assert not cache.exists(
        "temporary",
    )


def test_missing_cache_returns_none(
    tmp_path: Path,
) -> None:
    """
    Unknown keys should return no result.
    """
    cache = CacheManager(
        path=tmp_path,
    )

    assert (
        cache.get(
            "missing",
        )
        is None
    )

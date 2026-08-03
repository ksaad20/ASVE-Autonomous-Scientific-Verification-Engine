"""
Cache manager implementation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


class CacheManager:
    """
    Simple in-memory cache manager.

    The cache path is retained for future persistence support.
    """

    def __init__(
        self,
        path: Path | str | None = None,
    ) -> None:
        """
        Initialize the cache.

        Parameters
        ----------
        path
            Optional cache directory.
        """
        self.path = (
            Path(path)
            if path is not None
            else None
        )
        self._cache: dict[str, Any] = {}

    def get(
        self,
        key: str,
    ) -> Any | None:
        """
        Retrieve a cached value.
        """
        return self._cache.get(key)

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store a cached value.
        """
        self._cache[key] = value

    def invalidate(
        self,
        key: str,
    ) -> None:
        """
        Remove a cached value.
        """
        self._cache.pop(key, None)

    def clear(self) -> None:
        """
        Remove all cached values.
        """
        self._cache.clear()

    def exists(
        self,
        key: str,
   ) -> bool:
        """
        Return whether a cache entry exists.
        """
    return key in self._cache

    def __contains__(
        self,
        key: str,
    ) -> bool:
        return key in self._cache

    def __len__(self) -> int:
        return len(self._cache)

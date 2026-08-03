"""
Cache manager implementation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


class CacheManager:
    """
    Simple in-memory cache manager.

    Parameters
    ----------
    path
        Optional cache directory. Stored for compatibility with future
        persistent cache implementations.
    """

    def __init__(
        self,
        path: Path | None = None,
    ) -> None:
        """
        Initialize the cache manager.
        """
        self.path = path
        self._cache: dict[str, Any] = {}

    def get(
        self,
        key: str,
    ) -> Any | None:
        """
        Retrieve a cached value.

        Parameters
        ----------
        key
            Cache key.

        Returns
        -------
        Any | None
            Cached value if present, otherwise ``None``.
        """
        return self._cache.get(key)

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store a value in the cache.

        Parameters
        ----------
        key
            Cache key.
        value
            Value to cache.
        """
        self._cache[key] = value

    def invalidate(
        self,
        key: str,
    ) -> None:
        """
        Remove a cached entry.

        Parameters
        ----------
        key
            Cache key.
        """
        self._cache.pop(key, None)

    def clear(self) -> None:
        """
        Remove all cached entries.
        """
        self._cache.clear()

    def exists(
        self,
        key: str,
    ) -> bool:
        """
        Return whether a cache entry exists.

        Parameters
        ----------
        key
            Cache key.

        Returns
        -------
        bool
            ``True`` if the key exists.
        """
        return key in self._cache

    def __contains__(
        self,
        key: str,
    ) -> bool:
        """
        Support the ``in`` operator.
        """
        return self.exists(key)

    def __len__(self) -> int:
        """
        Return the number of cached entries.
        """
        return len(self._cache)

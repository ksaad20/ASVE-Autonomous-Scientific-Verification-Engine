"""Hashing utilities for ASVE.

Provides deterministic fingerprinting for text and file artifacts,
using SHA-256 for cryptographic hashing.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def hash_text(text: str) -> str:
    """Return a SHA-256 hex digest of the given text.

    Parameters
    ----------
    text : str
        The text content to hash.

    Returns
    -------
    str
        A 64-character hexadecimal SHA-256 digest.

    Examples
    --------
    >>> hash_text("hello")
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hash_file(path: str | Path) -> str:
    """Return a SHA-256 hex digest of the file at *path*.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the file to hash.

    Returns
    -------
    str
        A 64-character hexadecimal SHA-256 digest.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    IsADirectoryError
        If *path* points to a directory.

    """
    file_path = Path(path)
    hasher = hashlib.sha256()
    with file_path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


__all__ = [
    "hash_file",
    "hash_text",
]

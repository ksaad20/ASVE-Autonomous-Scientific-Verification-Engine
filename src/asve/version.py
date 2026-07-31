"""
Version information for ASVE.

This module provides the canonical version metadata for the package.
It is intentionally self-contained and free of third-party dependencies
to avoid circular imports and ensure safe imports during packaging,
documentation generation, and CLI startup.
"""

from __future__ import annotations

from typing import Final, NamedTuple

_MAJOR: Final[int] = 0
_MINOR: Final[int] = 0
_PATCH: Final[int] = 1

_RELEASE_LEVEL: Final[str] = "final"
_SERIAL: Final[int] = 0


class VersionInfo(NamedTuple):
    """Structured version information."""

    major: int
    minor: int
    patch: int
    releaselevel: str
    serial: int


version_info: Final[VersionInfo] = VersionInfo(
    major=_MAJOR,
    minor=_MINOR,
    patch=_PATCH,
    releaselevel=_RELEASE_LEVEL,
    serial=_SERIAL,
)

__version__: Final[str] = (
    f"{_MAJOR}.{_MINOR}.{_PATCH}"
    if _RELEASE_LEVEL == "final"
    else (
        f"{_MAJOR}.{_MINOR}.{_PATCH}"
        f"{_RELEASE_LEVEL}{_SERIAL}"
    )
)


def get_version() -> str:
    """
    Return the canonical ASVE version string.

    Returns
    -------
    str
        The package version.
    """
    return __version__


__all__ = [
    "__version__",
    "version_info",
    "VersionInfo",
    "get_version",
]

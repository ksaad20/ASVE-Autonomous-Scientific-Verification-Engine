"""
Tests for ASVE version metadata.

These tests validate package release information.
"""

from __future__ import annotations

import re

from asve import __version__


def test_version_exists() -> None:
    """
    Package version should be defined.
    """
    assert __version__


def test_version_is_string() -> None:
    """
    Version should be represented as text.
    """
    assert isinstance(
        __version__,
        str,
    )


def test_version_uses_semver() -> None:
    """
    Version should follow semantic versioning.
    """
    pattern = (
        r"^\d+\.\d+\.\d+"
        r"([\-\.][0-9A-Za-z]+)?$"
    )

    assert re.match(
        pattern,
        __version__,
    )


def test_version_not_empty() -> None:
    """
    Version metadata should be valid.
    """
    assert (
        len(__version__.strip())
        > 0
    )

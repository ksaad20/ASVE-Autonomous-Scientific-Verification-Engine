"""
Tests for ASVE package installation behavior.

These tests validate the package as an end-user would consume it.
"""

from __future__ import annotations

import importlib.metadata


def test_package_metadata_exists() -> None:
    """
    Installed package metadata should be available.
    """
    version = importlib.metadata.version(
        "asve",
    )

    assert version


def test_package_imports() -> None:
    """
    Main package should import successfully.
    """
    import asve

    assert asve is not None


def test_public_api_available() -> None:
    """
    Public API should remain accessible.
    """
    from asve.api import verify

    assert callable(
        verify,
    )

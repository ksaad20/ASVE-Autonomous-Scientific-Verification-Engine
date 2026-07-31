"""
Tests for ASVE public package imports.

These tests ensure the supported user-facing interface remains stable.
"""

from __future__ import annotations


def test_asve_package_imports() -> None:
    """
    ASVE package should import successfully.
    """
    import asve

    assert asve is not None


def test_public_verify_imports() -> None:
    """
    Public verify function should be available.
    """
    from asve.api import verify

    assert callable(
        verify,
    )


def test_api_package_exports_verify() -> None:
    """
    API package should expose verify.
    """
    import asve.api as api

    assert "verify" in api.__all__

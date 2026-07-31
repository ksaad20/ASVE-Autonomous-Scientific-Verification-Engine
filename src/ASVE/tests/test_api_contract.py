"""
Tests for ASVE public API contract.

These tests validate external-facing interfaces.
"""

from __future__ import annotations

import inspect

import asve

from asve.api import verify


def test_package_exports_version() -> None:
    """
    Package should expose version metadata.
    """
    assert hasattr(
        asve,
        "__version__",
    )


def test_verify_is_public_callable() -> None:
    """
    Verify function should be part of public API.
    """
    assert callable(
        verify,
    )


def test_verify_has_signature() -> None:
    """
    Public functions should maintain signatures.
    """
    signature = inspect.signature(
        verify,
    )

    assert len(
        signature.parameters,
    ) > 0


def test_public_api_module_exists() -> None:
    """
    API module should be importable.
    """
    from asve import api

    assert api is not None


def test_version_is_accessible() -> None:
    """
    Version should be readable externally.
    """
    assert isinstance(
        asve.__version__,
        str,
    )

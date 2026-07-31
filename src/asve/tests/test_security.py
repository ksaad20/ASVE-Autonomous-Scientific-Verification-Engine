"""
Tests for ASVE security behavior.

These tests validate safe handling of external inputs.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from asve.security.validator import SecurityValidator


def test_security_validator_initializes() -> None:
    """
    Security validator should initialize.
    """
    validator = SecurityValidator()

    assert validator is not None


def test_safe_path_is_allowed(
    tmp_path: Path,
) -> None:
    """
    Normal project paths should pass validation.
    """
    validator = SecurityValidator()

    result = validator.validate_path(
        tmp_path,
    )

    assert result is True


def test_invalid_path_is_rejected() -> None:
    """
    Invalid paths should fail validation.
    """
    validator = SecurityValidator()

    with pytest.raises(
        Exception,
    ):
        validator.validate_path(
            Path(
                "/nonexistent/asve/path",
            ),
        )


def test_sensitive_files_are_detected() -> None:
    """
    Sensitive file patterns should be recognized.
    """
    validator = SecurityValidator()

    result = validator.is_sensitive(
        ".env",
    )

    assert result is True


def test_normal_files_are_safe() -> None:
    """
    Normal source files should not be flagged.
    """
    validator = SecurityValidator()

    result = validator.is_sensitive(
        "analysis.py",
    )

    assert result is False

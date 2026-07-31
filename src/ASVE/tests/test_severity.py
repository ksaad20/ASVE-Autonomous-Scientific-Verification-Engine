"""
Tests for ASVE verification severity levels.

These tests validate severity classification behavior.
"""

from __future__ import annotations

from asve.verification.severity import Severity


def test_severity_levels_exist() -> None:
    """
    Standard severity levels should exist.
    """
    assert Severity.INFO
    assert Severity.WARNING
    assert Severity.ERROR


def test_severity_values_are_strings() -> None:
    """
    Severity values should be serializable.
    """
    assert isinstance(
        Severity.INFO.value,
        str,
    )

    assert isinstance(
        Severity.WARNING.value,
        str,
    )

    assert isinstance(
        Severity.ERROR.value,
        str,
    )


def test_severity_ordering() -> None:
    """
    Higher impact severities should rank higher.
    """
    assert (
        Severity.ERROR.level
        >
        Severity.WARNING.level
    )

    assert (
        Severity.WARNING.level
        >
        Severity.INFO.level
    )


def test_severity_serialization() -> None:
    """
    Severity should expose a stable value.
    """
    value = Severity.ERROR.value

    assert value == "error"

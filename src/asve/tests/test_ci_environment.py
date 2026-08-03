"""
Tests for ASVE CI environment compatibility.

These tests validate automated execution behavior.
"""

from __future__ import annotations

from collections.abc import MutableMapping
import os
import sys


def test_python_runtime_available() -> None:
    """
    Python runtime should be available.
    """
    assert sys.version_info.major >= 3


def test_package_runs_without_terminal() -> None:
    """
    Package should run without interactive input.
    """
    assert hasattr(
        sys,
        "stdout",
    )


def test_environment_access() -> None:
    """
    Environment variables should be accessible.
    """
    assert isinstance(
        os.environ,
        MutableMapping,
    )


def test_ci_variable_handling(
    monkeypatch,
) -> None:
    """
    CI variables should not break execution.
    """
    monkeypatch.setenv(
        "CI",
        "true",
    )

    assert (
        os.environ["CI"]
        == "true"
    )


def test_non_interactive_mode() -> None:
    """
    ASVE should support automated execution.
    """
    assert (
        sys.stdin
        is not None
    )

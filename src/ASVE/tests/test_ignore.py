"""
Tests for ASVE scanner ignore rules.

These tests verify deterministic path filtering behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.scanner.ignore import IgnoreMatcher


def test_default_git_directory_is_ignored() -> None:
    """
    Git metadata should be ignored.
    """
    matcher = IgnoreMatcher()

    path = Path(
        "project/.git/config",
    )

    assert matcher.matches(path)


def test_virtual_environment_is_ignored() -> None:
    """
    Virtual environments should be ignored.
    """
    matcher = IgnoreMatcher()

    path = Path(
        "project/.venv/lib/python3/site.py",
    )

    assert matcher.matches(path)


def test_python_source_is_not_ignored() -> None:
    """
    Normal scientific source files should remain visible.
    """
    matcher = IgnoreMatcher()

    path = Path(
        "project/src/model.py",
    )

    assert not matcher.matches(path)


def test_custom_ignore_rule_can_be_added() -> None:
    """
    Users should be able to add custom exclusions.
    """
    matcher = IgnoreMatcher()

    matcher.add(
        "results",
    )

    path = Path(
        "project/results/output.csv",
    )

    assert matcher.matches(path)

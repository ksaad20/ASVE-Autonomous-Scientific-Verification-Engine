"""
Tests for ASVE built-in registrations.

These tests verify default components are correctly activated.
"""

from __future__ import annotations

from pathlib import Path

from asve.scanner.builtin import (
    register_builtin_classifiers,
)
from asve.scanner.patterns import ArtifactPattern
from asve.scanner.registry import ArtifactRegistry


def test_builtin_classifiers_register() -> None:
    """
    Built-in registration should add classifiers.
    """
    registry = ArtifactRegistry()

    register_builtin_classifiers(
        registry,
    )

    assert len(registry) > 0


def test_builtin_python_classifier() -> None:
    """
    Built-in classifier should detect Python files.
    """
    registry = ArtifactRegistry()

    register_builtin_classifiers(
        registry,
    )

    result = registry.classify(
        Path("analysis.py"),
    )

    assert result == ArtifactPattern.PYTHON


def test_builtin_unknown_file() -> None:
    """
    Unknown formats should remain unknown.
    """
    registry = ArtifactRegistry()

    register_builtin_classifiers(
        registry,
    )

    result = registry.classify(
        Path("unknown.xyz"),
    )

    assert result == ArtifactPattern.UNKNOWN

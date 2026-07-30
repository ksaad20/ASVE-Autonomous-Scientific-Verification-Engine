"""
Tests for the ASVE artifact registry.

These tests verify extensible artifact classification behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.scanner.patterns import ArtifactPattern
from asve.scanner.registry import ArtifactRegistry


def test_registry_registers_classifier() -> None:
    """
    Registry should accept new classifiers.
    """
    registry = ArtifactRegistry()

    def classifier(
        path: Path,
    ) -> ArtifactPattern:
        if path.name == "special.data":
            return ArtifactPattern.DATASET

        return ArtifactPattern.UNKNOWN

    registry.register(
        classifier,
    )

    result = registry.classify(
        Path("special.data"),
    )

    assert result == ArtifactPattern.DATASET


def test_registry_returns_unknown_without_match() -> None:
    """
    Registry should return UNKNOWN when no classifier matches.
    """
    registry = ArtifactRegistry()

    result = registry.classify(
        Path("unknown.file"),
    )

    assert result == ArtifactPattern.UNKNOWN


def test_registry_clear_removes_classifiers() -> None:
    """
    Clearing registry should remove handlers.
    """
    registry = ArtifactRegistry()

    registry.register(
        lambda _: ArtifactPattern.PYTHON,
    )

    assert len(registry) == 1

    registry.clear()

    assert len(registry) == 0


def test_multiple_classifiers_use_first_match() -> None:
    """
    Registry should stop after first successful classifier.
    """
    registry = ArtifactRegistry()

    registry.register(
        lambda _: ArtifactPattern.MARKDOWN,
    )

    registry.register(
        lambda _: ArtifactPattern.PYTHON,
    )

    result = registry.classify(
        Path("file.py"),
    )

    assert result == ArtifactPattern.MARKDOWN

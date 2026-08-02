"""
Tests for ASVE extraction components.

These tests validate conversion of parsed data into
scientific entities.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.extractors.base import BaseExtractor
from asve.extractors.registry import ExtractorRegistry


class DummyExtractor(BaseExtractor):  # type: ignore[misc]
    """
    Minimal extractor for testing.
    """

    def supports(self, source: str) -> bool:
        """
        Check if source is supported.
        """
        return True

    def extract(self, source: Any) -> dict[str, Any]:
        """
        Extract data from source.
        """
        return {}


def test_extractor_registry_registers() -> None:
    """
    Registry should store extractors.
    """
    registry = ExtractorRegistry()

    registry.register(DummyExtractor())

    assert len(registry) == 1


def test_extractor_selection() -> None:
    """
    Registry should select compatible extractors.
    """
    registry = ExtractorRegistry()

    extractor = DummyExtractor()

    registry.register(extractor)

    result = registry.get_extractors(object())

    assert extractor in result


def test_extractor_execution(tmp_path: Path) -> None:
    """
    Extractor should produce structured output.
    """
    extractor = DummyExtractor()

    artifact = {
        "path": tmp_path / "paper.py",
    }

    result = extractor.extract(artifact)

    assert result["entity"] == "test"

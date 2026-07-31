"""
Tests for ASVE extraction components.

These tests validate conversion of parsed data into
scientific entities.
"""

from __future__ import annotations

from pathlib import Path

from asve.extractors.registry import ExtractorRegistry
from asve.extractors.base import BaseExtractor


class DummyExtractor(BaseExtractor):
    """
    Minimal extractor implementation for testing.
    """

    name = "dummy"

    def supports(
        self,
        artifact,
    ) -> bool:
        """
        Accept all test artifacts.
        """
        return True

    def extract(
        self,
        artifact,
    ) -> dict:
        """
        Return extracted data.
        """
        return {
            "entity": "test",
        }


def test_extractor_registry_registers() -> None:
    """
    Registry should store extractors.
    """
    registry = ExtractorRegistry()

    registry.register(
        DummyExtractor(),
    )

    assert len(registry) == 1


def test_extractor_selection() -> None:
    """
    Registry should select compatible extractors.
    """
    registry = ExtractorRegistry()

    extractor = DummyExtractor()

    registry.register(
        extractor,
    )

    result = registry.get_extractors(
        object(),
    )

    assert extractor in result


def test_extractor_execution(
    tmp_path: Path,
) -> None:
    """
    Extractor should produce structured output.
    """
    extractor = DummyExtractor()

    artifact = {
        "path": (
            tmp_path
            / "paper.py"
        ),
    }

    result = extractor.extract(
        artifact,
    )

    assert result["entity"] == "test"

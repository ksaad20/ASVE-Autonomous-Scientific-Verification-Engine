"""
Tests for ASVE parser infrastructure.

These tests validate parser registration and dispatch behavior.
"""

from __future__ import annotations

from pathlib import Path

from asve.parsers.registry import ParserRegistry
from asve.parsers.base import BaseParser


class DummyParser(BaseParser):
    """
    Minimal parser implementation for testing.
    """

    extensions = (
        ".dummy",
    )

    def parse(
        self,
        path: Path,
    ) -> dict:
        """
        Return a test parse result.
        """
        return {
            "parsed": True,
            "file": str(path),
        }


def test_parser_registry_registers_parser() -> None:
    """
    Registry should store parsers.
    """
    registry = ParserRegistry()

    registry.register(
        DummyParser(),
    )

    assert len(registry) == 1


def test_parser_registry_selects_parser() -> None:
    """
    Registry should select matching parser.
    """
    registry = ParserRegistry()

    registry.register(
        DummyParser(),
    )

    parser = registry.get_parser(
        Path("example.dummy"),
    )

    assert isinstance(
        parser,
        DummyParser,
    )


def test_parser_returns_none_for_unknown_format() -> None:
    """
    Unsupported files should not match.
    """
    registry = ParserRegistry()

    registry.register(
        DummyParser(),
    )

    parser = registry.get_parser(
        Path("unknown.xyz"),
    )

    assert parser is None


def test_parser_execution() -> None:
    """
    Selected parser should process artifacts.
    """
    parser = DummyParser()

    result = parser.parse(
        Path("experiment.dummy"),
    )

    assert result["parsed"] is True

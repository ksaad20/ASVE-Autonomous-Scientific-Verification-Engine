"""
TOML parser for ASVE.

This module implements parsing support for TOML documents.

The parser validates TOML syntax using Python's standard library and
delegates artifact creation to StructuredDataParser.
"""

from __future__ import annotations

from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from asve.exceptions import ParserError
from asve.parsers.structured import StructuredDataParser


class TOMLParser(StructuredDataParser):
    """
    Parser for TOML documents.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "toml"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """
        return frozenset(
            {
                ".toml",
            },
        )

    def parse_content(self, path: Path) -> None:
        """
        Validate a TOML document.

        Parameters
        ----------
        path
            Path to the TOML document.

        Raises
        ------
        ParserError
            If the document cannot be parsed.
        """
        try:
            with path.open("rb") as stream:
                tomllib.load(stream)
        except OSError as exc:
            raise ParserError(
                f"Unable to read TOML file '{path}'.",
            ) from exc
        except tomllib.TOMLDecodeError as exc:
            raise ParserError(
                f"Invalid TOML document '{path}'.",
            ) from exc


__all__ = [
    "TOMLParser",
]

"""
JSON parser for ASVE.

This module implements parsing support for JSON documents.

The parser validates JSON syntax using Python's standard library and
delegates artifact creation to StructuredDataParser.
"""

from __future__ import annotations

import json
from pathlib import Path

from asve.exceptions import ParserError
from asve.parsers.structured import StructuredDataParser


class JSONParser(StructuredDataParser):
    """
    Parser for JSON documents.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "json"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """
        return frozenset(
            {
                ".json",
                ".jsonld",
            }
        )

    def parse_content(self, path: Path) -> None:
        """
        Validate a JSON document.

        Parameters
        ----------
        path
            Path to the JSON document.

        Raises
        ------
        ParserError
            If the document is not valid JSON.
        """
        try:
            with path.open(
                mode="r",
                encoding="utf-8",
            ) as stream:
                json.load(stream)
        except OSError as exc:
            raise ParserError(
                f"Unable to read JSON file '{path}'."
            ) from exc
        except json.JSONDecodeError as exc:
            raise ParserError(
                f"Invalid JSON document '{path}'."
            ) from exc


__all__ = [
    "JSONParser",
]

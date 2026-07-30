"""
YAML parser for ASVE.

This module implements parsing support for YAML documents.

YAML support is optional and requires the ``PyYAML`` package.
The parser validates YAML syntax and delegates artifact creation to
StructuredDataParser.
"""

from __future__ import annotations

from pathlib import Path

from asve.exceptions import ParserError
from asve.parsers.structured import StructuredDataParser

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


class YAMLParser(StructuredDataParser):
    """
    Parser for YAML documents.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "yaml"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """
        return frozenset(
            {
                ".yaml",
                ".yml",
            }
        )

    def parse_content(self, path: Path) -> None:
        """
        Validate a YAML document.

        Parameters
        ----------
        path
            Path to the YAML document.

        Raises
        ------
        ParserError
            If YAML support is unavailable or the document is invalid.
        """
        if yaml is None:
            raise ParserError(
                "YAML support requires the 'PyYAML' package."
            )

        try:
            with path.open(
                mode="r",
                encoding="utf-8",
            ) as stream:
                yaml.safe_load(stream)
        except OSError as exc:
            raise ParserError(
                f"Unable to read YAML file '{path}'."
            ) from exc
        except yaml.YAMLError as exc:
            raise ParserError(
                f"Invalid YAML document '{path}'."
            ) from exc


__all__ = [
    "YAMLParser",
]

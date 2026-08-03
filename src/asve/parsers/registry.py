"""
Parser registry for ASVE.

Maintains registered parsers and selects the appropriate
parser for input artifacts.
"""

from __future__ import annotations

from pathlib import Path

from asve.parsers.base import Parser


class ParserRegistry:
    """
    Registry of available parsers.
    """

    def __init__(self) -> None:
        """
        Initialize empty parser registry.
        """
        self._parsers: list[Parser] = []

    def register(
        self,
        parser: Parser,
    ) -> None:
        """
        Register a parser.

        Parameters
        ----------
        parser
            Parser implementation.
        """
        self._parsers.append(
            parser,
        )

    def get_parser(
        self,
        path: Path,
    ) -> Parser | None:
        """
        Return parser matching a file.

        Parameters
        ----------
        path
            File path.

        Returns
        -------
        Parser | None
            Matching parser or None.
        """
        for parser in self._parsers:
            if parser.supports(
                path,
            ):
                return parser

        return None

    def parsers(
        self,
    ) -> list[Parser]:
        """
        Return registered parsers.
        """
        return list(
            self._parsers,
        )


__all__ = [
    "ParserRegistry",
]

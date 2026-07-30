"""
Parser dispatcher for ASVE.

The dispatcher selects the appropriate parser for a given artifact using
the parser registry and delegates parsing to that parser.

It contains no parsing logic itself.
"""

from __future__ import annotations

from pathlib import Path

from asve.exceptions import ParserError
from asve.models.artifact import Artifact
from asve.parsers.base import ArtifactParser
from asve.parsers.registry import ParserRegistry
from asve.parsers.registry import registry


class ParserDispatcher:
    """
    Dispatch parsing requests to registered parsers.
    """

    def __init__(
        self,
        parser_registry: ParserRegistry = registry,
    ) -> None:
        self._registry = parser_registry

    @property
    def registry(self) -> ParserRegistry:
        """
        Return the parser registry.
        """
        return self._registry

    def parser_for(self, path: Path) -> ArtifactParser:
        """
        Return the parser responsible for a file.

        Parameters
        ----------
        path
            File to parse.

        Raises
        ------
        ParserError
            If no parser supports the supplied file.
        """
        parser = self._registry.get(path)

        if parser is None:
            raise ParserError(
                f"No parser registered for '{path.suffix}'."
            )

        return parser

    def parse(self, path: Path) -> Artifact:
        """
        Parse a single file.

        Parameters
        ----------
        path
            File to parse.

        Returns
        -------
        Artifact
            Parsed artifact.
        """
        parser = self.parser_for(path)
        return parser.parse(path)

    def supports(self, path: Path) -> bool:
        """
        Return True if a parser exists for the supplied file.
        """
        return self._registry.supports(path)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(parsers={len(self.registry)})"
        )


dispatcher = ParserDispatcher()


__all__ = [
    "ParserDispatcher",
    "dispatcher",
]

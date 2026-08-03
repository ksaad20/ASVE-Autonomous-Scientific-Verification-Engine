"""
Parser registry for ASVE.

The parser registry maintains the mapping between filename extensions
and parser implementations.

Concrete parsers register themselves with this registry, allowing the
remainder of the application to discover parsers without importing them
directly.

The registry is intentionally lightweight and deterministic.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from asve.parsers.base import ArtifactParser


class ParserRegistry:
    """
    Registry of artifact parsers.
    """
    def get_parser(
        self,
        path: Path,
    ) -> ArtifactParser | None:
        """
        Compatibility alias for parser lookup.

        Parameters
        ----------
        path
            File path to resolve.

        Returns
        -------
        ArtifactParser | None
            Matching parser if registered.
        """
        return self.get(path)

    def __init__(self) -> None:
        self._parsers: dict[str, ArtifactParser] = {}

    def register(self, parser: ArtifactParser) -> None:
        """
        Register a parser.

        Parameters
        ----------
        parser
            Parser instance to register.

        Raises
        ------
        ValueError
            If a parser is already registered for one of its supported
            extensions.
        """
        for extension in parser.supported_extensions:
            key = extension.lower()

            if key in self._parsers:
                raise ValueError(
                    f"Parser already registered for '{key}'."
                )

            self._parsers[key] = parser

    def unregister(self, extension: str) -> None:
        """
        Remove a parser.

        Missing extensions are ignored.
        """
        self._parsers.pop(extension.lower(), None)

    def get(self, path: Path) -> ArtifactParser | None:
        """
        Return the parser for a file.

        Parameters
        ----------
        path
            File to parse.

        Returns
        -------
        ArtifactParser | None
            Registered parser, if available.
        """
        return self._parsers.get(path.suffix.lower())

    def supports(self, path: Path) -> bool:
        """
        Return True if a parser exists for the file.
        """
        return self.get(path) is not None

    def extensions(self) -> tuple[str, ...]:
        """
        Return registered extensions.
        """
        return tuple(sorted(self._parsers))

    def parsers(self) -> tuple[ArtifactParser, ...]:
        """
        Return unique registered parsers.
        """
        return tuple(dict.fromkeys(self._parsers.values()))

    def clear(self) -> None:
        """
        Remove every registered parser.
        """
        self._parsers.clear()

    def __contains__(self, extension: str) -> bool:
        return extension.lower() in self._parsers

    def __len__(self) -> int:
        return len(self.parsers())

    def __iter__(self) -> Iterator[ArtifactParser]:
        yield from self.parsers()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"extensions={self.extensions()!r})"
        )


# Default global parser registry.
#
# This singleton allows parser dispatch components to share one registry
# without requiring explicit dependency wiring throughout the package.
registry = ParserRegistry()

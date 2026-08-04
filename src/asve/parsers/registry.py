"""
Parser registry for ASVE.

The registry maps filename extensions to parser implementations and
provides deterministic parser lookup for supported artifacts.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from asve.parsers.base import ArtifactParser


class ParserRegistry:
    """
    Registry of artifact parsers.
    """

    def __init__(self) -> None:
        """
        Initialize an empty parser registry.
        """
        self._parsers: dict[str, ArtifactParser] = {}

    def register(
        self,
        parser: ArtifactParser,
    ) -> None:
        """
        Register a parser.

        Parameters
        ----------
        parser
            Parser instance to register.

        Raises
        ------
        ValueError
            If an extension is already registered.
        """
        for extension in parser.supported_extensions:
            key = extension.lower()

            if key in self._parsers:
                raise ValueError(
                    f"Parser already registered for '{key}'.",
                )

            self._parsers[key] = parser

    def unregister(
        self,
        extension: str,
    ) -> None:
        """
        Remove the parser registered for an extension.

        Missing extensions are ignored.
        """
        self._parsers.pop(
            extension.lower(),
            None,
        )

    def get(
        self,
        path: Path,
    ) -> ArtifactParser | None:
        """
        Return the parser registered for a file path.
        """
        return self._parsers.get(
            path.suffix.lower(),
        )

    def get_parser(
        self,
        path: Path,
    ) -> ArtifactParser | None:
        """
        Return the parser registered for a file path.

        This method preserves compatibility with the earlier registry API.
        """
        return self.get(
            path,
        )

    def supports(
        self,
        path: Path,
    ) -> bool:
        """
        Return whether a parser exists for a file path.
        """
        return self.get(path) is not None

    def extensions(
        self,
    ) -> tuple[str, ...]:
        """
        Return registered extensions in deterministic order.
        """
        return tuple(
            sorted(self._parsers),
        )

    def parsers(
        self,
    ) -> tuple[ArtifactParser, ...]:
        """
        Return unique registered parsers.
        """
        return tuple(
            dict.fromkeys(
                self._parsers.values(),
            ),
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all registered parsers.
        """
        self._parsers.clear()

    def __contains__(
        self,
        extension: str,
    ) -> bool:
        """
        Return whether an extension is registered.
        """
        return extension.lower() in self._parsers

    def __len__(
        self,
    ) -> int:
        """
        Return the number of unique registered parsers.
        """
        return len(
            self.parsers(),
        )

    def __iter__(
        self,
    ) -> Iterator[ArtifactParser]:
        """
        Iterate over unique registered parsers.
        """
        yield from self.parsers()

    def __repr__(
        self,
    ) -> str:
        """
        Return a developer-readable registry representation.
        """
        return (
            f"{self.__class__.__name__}("
            f"extensions={self.extensions()!r})"
        )


registry = ParserRegistry()


__all__ = [
    "ParserRegistry",
    "registry",
]

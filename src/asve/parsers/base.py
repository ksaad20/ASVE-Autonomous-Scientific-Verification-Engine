"""Base parser interface for artifact extraction.

This module defines the abstract base class that all artifact parsers must
implement, ensuring a consistent API across the package.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asve.models.artifact import Artifact


class ArtifactParser(ABC):
    """Abstract base class for artifact parsers.

    Provides a common interface for parsing artifacts from various
    sources and formats. Concrete implementations must override the
    :meth:`parse` method.

    Examples
    --------
    >>> class MyParser(ArtifactParser):
    ...     def parse(self, path: Path) -> Artifact:
    ...         ...

    """

    @abstractmethod
    def parse(self, path: Path) -> Artifact:
        """Parse an artifact from the given path.

        Parameters
        ----------
        path : pathlib.Path
            Path to the artifact file or directory.

        Returns
        -------
        Artifact
            Parsed artifact metadata.

        Raises
        ------
        FileNotFoundError
            If the artifact path does not exist.
        ValueError
            If the artifact format is not supported or invalid.
        NotImplementedError
            If the parser does not support the artifact type.

        """

    def __repr__(self) -> str:
        """Return a string representation of the parser."""
        return f"{self.__class__.__name__}()"


# Backwards-compatible alias.
BaseParser = ArtifactParser

__all__ = [
    "ArtifactParser",
    "BaseParser",
]

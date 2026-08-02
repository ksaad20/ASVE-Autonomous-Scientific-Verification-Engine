Base parser interfaces for ASVE.

Every parser converts a supported scientific artifact into a normalized
representation that can be consumed by the remainder of the ASVE
pipeline.

Concrete parsers should be deterministic, side-effect free, and avoid
modifying project files.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pathlib import Path

from asve.models.artifact import Artifact


class ArtifactParser(ABC):
    """
    Abstract base class for all ASVE artifact parsers.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Return the parser name.
        """

    @property
    @abstractmethod
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """

    def supports(self, path: Path) -> bool:
        """
        Return True if this parser supports the supplied file.
        """
        return path.suffix.lower() in self.supported_extensions

    @abstractmethod
    def parse(self, path: Path) -> Artifact:
        """
        Parse a file into an Artifact.

        Parameters
        ----------
        path
            Path to the artifact.

        Returns
        -------
        Artifact
            Parsed artifact metadata.
        """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

BaseParser = ArtifactParser

__all__ = [
    "BaseParser",
    "ArtifactParser"
]

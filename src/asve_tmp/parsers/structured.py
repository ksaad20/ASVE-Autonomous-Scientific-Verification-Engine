"""
Base classes for structured data parsers.

Structured parsers operate on machine-readable formats such as JSON,
YAML, TOML, CSV, XML, and similar formats.

This module centralizes common file handling behavior so concrete
parsers only need to implement the format-specific parsing logic.
"""

from __future__ import annotations

from abc import abstractmethod
from pathlib import Path
from uuid import uuid4

from asve.exceptions import ParserError
from asve.models.artifact import Artifact
from asve.models.artifact import ArtifactType
from asve.parsers.base import ArtifactParser


class StructuredDataParser(ArtifactParser):
    """
    Base class for structured data parsers.
    """

    @property
    def artifact_type(self) -> ArtifactType:
        """
        Return the artifact type produced by this parser.
        """
        return "dataset"

    def parse(self, path: Path) -> Artifact:
        """
        Parse a structured data file.

        Parameters
        ----------
        path
            Structured data file.

        Returns
        -------
        Artifact
            Parsed artifact metadata.
        """
        resolved = path.resolve()

        try:
            self.parse_content(resolved)
        except OSError as exc:
            raise ParserError(
                f"Unable to read '{resolved}'."
            ) from exc

        return Artifact(
            identifier=str(uuid4()),
            name=resolved.stem,
            path=resolved,
            artifact_type=self.artifact_type,
            size_bytes=resolved.stat().st_size,
        )

    @abstractmethod
    def parse_content(self, path: Path) -> None:
        """
        Validate the contents of a structured file.

        Implementations should raise an exception if parsing fails.
        """

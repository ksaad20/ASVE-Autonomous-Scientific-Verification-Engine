"""
Markdown parser for ASVE.

This module implements parsing support for Markdown documents.

The current implementation extracts normalized artifact metadata only.
Future versions will support heading extraction, citation analysis,
figure discovery, code block inspection, and dependency extraction.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from asve.models.artifact import Artifact
from asve.parsers.base import ArtifactParser


class MarkdownParser(ArtifactParser):
    """
    Parser for Markdown documents.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "markdown"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """
        return frozenset(
            {
                ".md",
                ".markdown",
            }
        )

    def parse(self, path: Path) -> Artifact:
        """
        Parse a Markdown document.

        Parameters
        ----------
        path
            Markdown file.

        Returns
        -------
        Artifact
            Parsed artifact metadata.
        """
        resolved = path.resolve()

        return Artifact(
            identifier=str(uuid4()),
            name=resolved.stem,
            path=resolved,
            artifact_type="document",
            size_bytes=resolved.stat().st_size,
        )


__all__ = [
    "MarkdownParser",
]

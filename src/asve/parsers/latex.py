"""
LaTeX parser for ASVE.

This module implements parsing support for LaTeX source documents.

The MVP implementation extracts normalized artifact metadata only.
Future versions will support dependency extraction, citation analysis,
label/reference validation, equation indexing, bibliography parsing,
and document graph construction.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from asve.models.artifact import Artifact
from asve.parsers.base import ArtifactParser


class LatexParser(ArtifactParser):
    """
    Parser for LaTeX source documents.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "latex"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return the supported filename extensions.
        """
        return frozenset(
            {
                ".tex",
                ".ltx",
            }
        )

    def parse(self, path: Path) -> Artifact:
        """
        Parse a LaTeX document.

        Parameters
        ----------
        path
            Path to the LaTeX source file.

        Returns
        -------
        Artifact
            Normalized artifact metadata.
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
    "LatexParser",
]

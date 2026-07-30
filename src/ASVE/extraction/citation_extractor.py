"""
Citation extractor for ASVE.

This module extracts citation relationships from scientific documents.

Supported MVP formats:

- LaTeX citation commands
- BibTeX citation keys

Future versions will support DOI validation, citation metadata,
reference completeness analysis, and provenance scoring.
"""

from __future__ import annotations

import re

from asve.extraction.base import Extractor
from asve.models.artifact import Artifact
from asve.models.dependency import Dependency
from asve.models.dependency import DependencyType


_CITATION_PATTERN = re.compile(
    r"\\cite[a-zA-Z]*\{([^}]+)\}"
)

_BIB_ENTRY_PATTERN = re.compile(
    r"@\w+\s*\{\s*([^,]+),"
)


class CitationExtractor(Extractor):
    """
    Extract citation dependencies from scientific artifacts.
    """

    @property
    def name(self) -> str:
        """
        Return extractor name.
        """
        return "citation"

    def supports(
        self,
        artifact: Artifact,
    ) -> bool:
        """
        Determine whether the artifact is citation-aware.
        """
        return artifact.path.suffix.lower() in {
            ".tex",
            ".bib",
        }

    def extract(
        self,
        artifact: Artifact,
    ) -> tuple[Dependency, ...]:
        """
        Extract citation relationships.

        Parameters
        ----------
        artifact
            Scientific document artifact.

        Returns
        -------
        tuple[Dependency, ...]
            Citation dependencies.
        """
        content = artifact.path.read_text(
            encoding="utf-8",
        )

        if artifact.path.suffix.lower() == ".tex":
            return self._extract_citations(
                artifact,
                content,
            )

        return self._extract_bib_entries(
            artifact,
            content,
        )

    def _extract_citations(
        self,
        artifact: Artifact,
        content: str,
    ) -> tuple[Dependency, ...]:
        """
        Extract LaTeX citation keys.
        """
        dependencies: list[Dependency] = []

        for group in _CITATION_PATTERN.findall(content):
            keys = (
                key.strip()
                for key in group.split(",")
            )

            dependencies.extend(
                Dependency(
                    source=str(artifact.identifier),
                    target=key,
                    dependency_type=(
                        DependencyType.CITES
                    ),
                    metadata={
                        "format": "latex",
                    },
                )
                for key in keys
            )

        return tuple(dependencies)

    def _extract_bib_entries(
        self,
        artifact: Artifact,
        content: str,
    ) -> tuple[Dependency, ...]:
        """
        Extract BibTeX entry identifiers.
        """
        return tuple(
            Dependency(
                source=str(artifact.identifier),
                target=entry,
                dependency_type=(
                    DependencyType.REFERENCES
                ),
                metadata={
                    "format": "bibtex",
                },
            )
            for entry in _BIB_ENTRY_PATTERN.findall(content)
        )


__all__ = [
    "CitationExtractor",
      ]

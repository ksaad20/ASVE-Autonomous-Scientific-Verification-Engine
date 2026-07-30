"""
Scientific reference extractor for ASVE.

This module extracts artifact relationships from scientific documents.

Supported MVP relationships:

- LaTeX include dependencies
- LaTeX bibliography dependencies
- Markdown local references
- Markdown image references

Future versions will support richer semantic linking.
"""

from __future__ import annotations

import re
from pathlib import Path

from asve.extraction.base import Extractor
from asve.models.artifact import Artifact
from asve.models.dependency import Dependency
from asve.models.dependency import DependencyType


_LATEX_REFERENCE_PATTERN = re.compile(
    r"\\(?:input|include)\{([^}]+)\}"
)

_LATEX_BIB_PATTERN = re.compile(
    r"\\(?:bibliography|addbibresource)\{([^}]+)\}"
)

_MARKDOWN_LINK_PATTERN = re.compile(
    r"\[[^\]]+\]\(([^)]+)\)"
)

_MARKDOWN_IMAGE_PATTERN = re.compile(
    r"!\[[^\]]*\]\(([^)]+)\)"
)


class ReferenceExtractor(Extractor):
    """
    Extract document reference dependencies.
    """

    @property
    def name(self) -> str:
        """
        Return extractor name.
        """
        return "scientific_references"

    def supports(
        self,
        artifact: Artifact,
    ) -> bool:
        """
        Determine supported artifact types.
        """
        return artifact.path.suffix.lower() in {
            ".tex",
            ".md",
            ".markdown",
        }

    def extract(
        self,
        artifact: Artifact,
    ) -> tuple[Dependency, ...]:
        """
        Extract references from an artifact.
        """
        content = artifact.path.read_text(
            encoding="utf-8",
        )

        suffix = artifact.path.suffix.lower()

        if suffix == ".tex":
            return self._extract_latex(
                artifact,
                content,
            )

        return self._extract_markdown(
            artifact,
            content,
        )

    def _extract_latex(
        self,
        artifact: Artifact,
        content: str,
    ) -> tuple[Dependency, ...]:
        """
        Extract LaTeX references.
        """
        dependencies: list[Dependency] = []

        for match in _LATEX_REFERENCE_PATTERN.findall(
            content
        ):
            dependencies.append(
                self._dependency(
                    artifact,
                    match,
                    DependencyType.INCLUDES,
                )
            )

        for match in _LATEX_BIB_PATTERN.findall(
            content
        ):
            dependencies.append(
                self._dependency(
                    artifact,
                    match,
                    DependencyType.REFERENCES,
                )
            )

        return tuple(dependencies)

    def _extract_markdown(
        self,
        artifact: Artifact,
        content: str,
    ) -> tuple[Dependency, ...]:
        """
        Extract Markdown references.
        """
        references = (
            _MARKDOWN_LINK_PATTERN.findall(content)
            + _MARKDOWN_IMAGE_PATTERN.findall(content)
        )

        return tuple(
            self._dependency(
                artifact,
                reference,
                DependencyType.REFERENCES,
            )
            for reference in references
            if not reference.startswith("http")
        )

    @staticmethod
    def _dependency(
        artifact: Artifact,
        target: str,
        dependency_type: DependencyType,
    ) -> Dependency:
        """
        Create dependency object.
        """
        return Dependency(
            source=str(artifact.identifier),
            target=str(Path(target)),
            dependency_type=dependency_type,
            metadata={
                "extractor": "reference",
            },
        )


__all__ = [
    "ReferenceExtractor",
]

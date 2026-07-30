"""
Jupyter Notebook parser for ASVE.

This module implements parsing support for Jupyter Notebook documents.

The MVP validates notebook structure using the official ``nbformat``
library and returns normalized artifact metadata. Future versions will
extract code cells, markdown cells, execution order, outputs,
dependencies, and reproducibility diagnostics.
"""

from __future__ import annotations

from pathlib import Path

from asve.exceptions import ParserError
from asve.models.artifact import ArtifactType
from asve.parsers.structured import StructuredDataParser

try:
    import nbformat
except ImportError:  # pragma: no cover
    nbformat = None


class NotebookParser(StructuredDataParser):
    """
    Parser for Jupyter Notebook files.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "notebook"

    @property
    def artifact_type(self) -> ArtifactType:
        """
        Return the artifact type.
        """
        return "notebook"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """
        return frozenset(
            {
                ".ipynb",
            }
        )

    def parse_content(self, path: Path) -> None:
        """
        Validate a Jupyter Notebook.

        Parameters
        ----------
        path
            Notebook file.

        Raises
        ------
        ParserError
            If notebook support is unavailable or the notebook is
            malformed.
        """
        if nbformat is None:
            raise ParserError(
                "Notebook support requires the 'nbformat' package."
            )

        try:
            with path.open(
                mode="r",
                encoding="utf-8",
            ) as stream:
                nbformat.read(
                    stream,
                    as_version=4,
                )
        except OSError as exc:
            raise ParserError(
                f"Unable to read notebook '{path}'."
            ) from exc
        except Exception as exc:
            raise ParserError(
                f"Invalid notebook '{path}'."
            ) from exc


__all__ = [
    "NotebookParser",
]

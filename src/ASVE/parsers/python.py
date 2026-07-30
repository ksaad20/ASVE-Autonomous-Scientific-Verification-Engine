"""
Python parser for ASVE.

This module implements parsing support for Python source files.

The MVP implementation validates Python syntax using the standard
library AST parser and returns normalized artifact metadata. Future
versions will extract imports, classes, functions, type annotations,
docstrings, and software dependency information.
"""

from __future__ import annotations

import ast
from pathlib import Path
from uuid import uuid4

from asve.exceptions import ParserError
from asve.models.artifact import Artifact
from asve.parsers.base import ArtifactParser


class PythonParser(ArtifactParser):
    """
    Parser for Python source files.
    """

    @property
    def name(self) -> str:
        """Return the parser name."""
        return "python"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """Return supported filename extensions."""
        return frozenset({".py"})

    def parse(self, path: Path) -> Artifact:
        """
        Parse a Python source file.

        Parameters
        ----------
        path
            Python source file.

        Returns
        -------
        Artifact
            Parsed artifact metadata.

        Raises
        ------
        ParserError
            If the file cannot be parsed as valid Python.
        """
        resolved = path.resolve()

        try:
            source = resolved.read_text(encoding="utf-8")
            ast.parse(source, filename=str(resolved))
        except OSError as exc:
            raise ParserError(
                f"Unable to read Python file '{resolved}'."
            ) from exc
        except SyntaxError as exc:
            raise ParserError(
                f"Invalid Python syntax in '{resolved}'."
            ) from exc

        return Artifact(
            identifier=str(uuid4()),
            name=resolved.stem,
            path=resolved,
            artifact_type="software",
            size_bytes=resolved.stat().st_size,
        )


__all__ = [
    "PythonParser",
]

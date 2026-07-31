"""
Python import dependency extractor for ASVE.

This module extracts software dependencies from Python artifacts.

The extractor uses Python's AST representation to analyze imports
without executing user code.

Future versions will resolve package metadata, compare environments,
and detect undeclared dependencies.
"""

from __future__ import annotations

import ast
from pathlib import Path

from asve.models.artifact import Artifact
from asve.models.dependency import Dependency
from asve.models.dependency import DependencyType
from asve.extraction.base import Extractor


class ImportExtractor(Extractor):
    """
    Extract Python import dependencies.
    """

    @property
    def name(self) -> str:
        """
        Return extractor name.
        """
        return "python_imports"

    def supports(
        self,
        artifact: Artifact,
    ) -> bool:
        """
        Return whether the artifact is a Python file.
        """
        return artifact.path.suffix.lower() == ".py"

    def extract(
        self,
        artifact: Artifact,
    ) -> tuple[Dependency, ...]:
        """
        Extract imported modules.

        Parameters
        ----------
        artifact
            Python source artifact.

        Returns
        -------
        tuple[Dependency, ...]
            Import dependencies.
        """
        source = artifact.path.read_text(
            encoding="utf-8",
        )

        tree = ast.parse(
            source,
            filename=str(artifact.path),
        )

        dependencies: list[Dependency] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                dependencies.extend(
                    self._from_imports(
                        artifact,
                        (
                            alias.name
                            for alias in node.names
                        ),
                    )
                )

            elif isinstance(node, ast.ImportFrom):
                if node.module is not None:
                    dependencies.extend(
                        self._from_imports(
                            artifact,
                            (node.module,),
                        )
                    )

        return tuple(dependencies)

    def _from_imports(
        self,
        artifact: Artifact,
        modules: tuple[str, ...] | object,
    ) -> list[Dependency]:
        """
        Convert imported modules into dependencies.
        """
        return [
            Dependency(
                source=str(artifact.identifier),
                target=module,
                dependency_type=(
                    DependencyType.IMPORTS
                ),
                metadata={
                    "language": "python",
                },
            )
            for module in modules
        ]


__all__ = [
    "ImportExtractor",
          ]

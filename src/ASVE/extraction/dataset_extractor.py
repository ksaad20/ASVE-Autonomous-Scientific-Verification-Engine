"""
Dataset dependency extractor for ASVE.

This module extracts dataset usage relationships from computational
artifacts.

The MVP implementation analyzes Python source code using the AST module
to identify common dataset loading operations.

Future versions will support:
- dataframe transformations
- output lineage
- model provenance
- notebook execution tracking
"""

from __future__ import annotations

import ast

from asve.extraction.base import Extractor
from asve.models.artifact import Artifact
from asve.models.dependency import Dependency
from asve.models.dependency import DependencyType


_DATASET_FUNCTIONS = frozenset(
    {
        "read_csv",
        "read_excel",
        "read_json",
        "read_parquet",
        "load",
        "genfromtxt",
    }
)


class DatasetExtractor(Extractor):
    """
    Extract dataset dependencies from software artifacts.
    """

    @property
    def name(self) -> str:
        """
        Return extractor name.
        """
        return "dataset"

    def supports(
        self,
        artifact: Artifact,
    ) -> bool:
        """
        Determine whether the artifact is analyzable.
        """
        return artifact.path.suffix.lower() == ".py"

    def extract(
        self,
        artifact: Artifact,
    ) -> tuple[Dependency, ...]:
        """
        Extract dataset usage dependencies.

        Parameters
        ----------
        artifact
            Python source artifact.

        Returns
        -------
        tuple[Dependency, ...]
            Dataset dependencies.
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
            if isinstance(node, ast.Call):
                dependency = self._extract_call(
                    artifact,
                    node,
                )

                if dependency is not None:
                    dependencies.append(dependency)

        return tuple(dependencies)

    def _extract_call(
        self,
        artifact: Artifact,
        node: ast.Call,
    ) -> Dependency | None:
        """
        Extract dataset dependency from a function call.
        """
        if not isinstance(node.func, ast.Attribute):
            return None

        if node.func.attr not in _DATASET_FUNCTIONS:
            return None

        if not node.args:
            return None

        argument = node.args[0]

        if not isinstance(argument, ast.Constant):
            return None

        if not isinstance(argument.value, str):
            return None

        return Dependency(
            source=str(artifact.identifier),
            target=argument.value,
            dependency_type=(
                DependencyType.READS
            ),
            metadata={
                "extractor": "dataset",
                "language": "python",
                "function": node.func.attr,
            },
        )


__all__ = [
    "DatasetExtractor",
]

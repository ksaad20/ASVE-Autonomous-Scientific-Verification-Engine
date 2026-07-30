"""
Artifact classifier for ASVE.

This module classifies filesystem objects into scientific artifact
categories. Classification is intentionally lightweight and relies on
file metadata (such as extension and filename) rather than parsing file
contents.

Classification is deterministic and side-effect free.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import ArtifactType


_DOCUMENT_EXTENSIONS = frozenset(
    {
        ".md",
        ".rst",
        ".tex",
        ".txt",
    }
)

_DATASET_EXTENSIONS = frozenset(
    {
        ".csv",
        ".tsv",
        ".json",
        ".jsonl",
        ".parquet",
        ".xlsx",
    }
)

_NOTEBOOK_EXTENSIONS = frozenset(
    {
        ".ipynb",
    }
)

_SOFTWARE_EXTENSIONS = frozenset(
    {
        ".py",
        ".r",
        ".jl",
        ".m",
    }
)

_CONFIGURATION_FILES = frozenset(
    {
        "pyproject.toml",
        "environment.yml",
        "requirements.txt",
        "Dockerfile",
        "docker-compose.yml",
        "CITATION.cff",
    }
)


class ArtifactClassifier:
    """
    Classify filesystem objects into artifact types.
    """

    def classify(self, path: Path) -> ArtifactType:
        """
        Classify a filesystem path.

        Parameters
        ----------
        path
            Path to classify.

        Returns
        -------
        ArtifactType
            Classified artifact type.
        """
        name = path.name
        suffix = path.suffix.lower()

        if name in _CONFIGURATION_FILES:
            return "configuration"

        if suffix in _DOCUMENT_EXTENSIONS:
            return "document"

        if suffix in _DATASET_EXTENSIONS:
            return "dataset"

        if suffix in _NOTEBOOK_EXTENSIONS:
            return "notebook"

        if suffix in _SOFTWARE_EXTENSIONS:
            return "software"

        return "unknown"


__all__ = [
    "ArtifactClassifier",
]

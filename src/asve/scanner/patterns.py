"""
ASVE artifact classification patterns.

This module defines deterministic rules for identifying scientific
artifact categories from file paths.

Future versions may include content-based classification.
"""

from __future__ import annotations

from pathlib import Path
from enum import Enum


class ArtifactPattern(str, Enum):
    """
    Scientific artifact categories.
    """

    PYTHON = "python"

    NOTEBOOK = "notebook"

    LATEX = "latex"

    MARKDOWN = "markdown"

    DATASET = "dataset"

    CONFIGURATION = "configuration"

    JSON = "json"

    UNKNOWN = "unknown"


_EXTENSION_MAP = {
    ".py": ArtifactPattern.PYTHON,
    ".ipynb": ArtifactPattern.NOTEBOOK,
    ".tex": ArtifactPattern.LATEX,
    ".md": ArtifactPattern.MARKDOWN,
    ".markdown": ArtifactPattern.MARKDOWN,
    ".csv": ArtifactPattern.DATASET,
    ".tsv": ArtifactPattern.DATASET,
    ".json": ArtifactPattern.JSON,
    ".yaml": ArtifactPattern.CONFIGURATION,
    ".yml": ArtifactPattern.CONFIGURATION,
    ".toml": ArtifactPattern.CONFIGURATION,
}


def classify_path(
    path: Path,
) -> ArtifactPattern:
    """
    Classify an artifact based on extension.

    Parameters
    ----------
    path
        File path.

    Returns
    -------
    ArtifactPattern
        Detected artifact category.
    """
    return _EXTENSION_MAP.get(
        path.suffix.lower(),
        ArtifactPattern.UNKNOWN,
    )


__all__ = [
    "ArtifactPattern",
    "classify_path",
]

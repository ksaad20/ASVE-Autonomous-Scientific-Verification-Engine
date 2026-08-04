"""
Metadata extraction utilities.

This module provides deterministic metadata extraction for ASVE artifacts.
Metadata is intentionally lightweight and reproducible so that repeated
analysis of the same artifact produces identical results.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.models.artifact import Artifact


class MetadataExtractor:
    """
    Extract metadata from scientific artifacts.

    The extractor produces a dictionary containing basic filesystem
    information that is independent of parser implementations. Additional
    metadata sources may be incorporated in future versions without
    changing the public API.
    """

    def extract(
        self,
        artifact: Artifact,
    ) -> dict[str, Any]:
        """
        Extract metadata from an artifact.

        Parameters
        ----------
        artifact
            Artifact whose metadata should be extracted.

        Returns
        -------
        dict[str, Any]
            Deterministic metadata describing the artifact.
        """
        path = Path(artifact.path)

        return {
            "filename": path.name,
            "stem": path.stem,
            "suffix": path.suffix,
            "path": str(path),
            "parent": str(path.parent),
            "exists": path.exists(),
        }


__all__ = [
    "MetadataExtractor",
]

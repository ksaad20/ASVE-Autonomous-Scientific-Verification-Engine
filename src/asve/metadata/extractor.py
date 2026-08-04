"""
Metadata extraction utilities.

Provides deterministic metadata extraction for filesystem paths and
ASVE artifacts.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.models.artifact import Artifact


class MetadataExtractor:
    """
    Extract metadata from artifacts or filesystem paths.
    """

    def extract(
        self,
        artifact: Artifact | Path | str,
    ) -> dict[str, Any]:
        """
        Extract deterministic metadata.

        Parameters
        ----------
        artifact
            Artifact instance, filesystem path, or string path.

        Returns
        -------
        dict[str, Any]
            Extracted metadata.
        """
        if isinstance(artifact, Artifact):
            path = Path(artifact.path)
        else:
            path = Path(artifact)

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

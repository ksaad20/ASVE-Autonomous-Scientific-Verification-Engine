"""
Metadata extraction utilities.

Provides deterministic metadata extraction for ASVE artifacts and
filesystem paths. The extractor accepts either an ``Artifact`` instance
or a path-like object for backwards compatibility with earlier ASVE
releases and existing test suites.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.models.artifact import Artifact


class MetadataExtractor:
    """
    Extract deterministic metadata from scientific artifacts.

    The extracted metadata is intentionally lightweight and stable so
    that repeated extraction of the same artifact always produces the
    same result.
    """

    def extract(
        self,
        artifact: Artifact | Path | str,
    ) -> dict[str, Any]:
        """
        Extract metadata from an artifact or filesystem path.

        Parameters
        ----------
        artifact
            Artifact instance, ``pathlib.Path`` object, or string path.

        Returns
        -------
        dict[str, Any]
            Dictionary containing deterministic metadata describing the
            supplied artifact.
        """
        path = (
            Path(artifact.path)
            if isinstance(artifact, Artifact)
            else Path(artifact)
        )

        return {
            "filename": path.name,
            "stem": path.stem,
            "suffix": path.suffix,
            "path": str(path),
            "parent": str(path.parent),
            "exists": path.exists(),
            "is_file": path.is_file(),
            "is_dir": path.is_dir(),
        }


__all__ = [
    "MetadataExtractor",
]

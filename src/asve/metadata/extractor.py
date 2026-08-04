"""
Metadata extraction utilities.

Provides deterministic metadata extraction for ASVE artifacts and
filesystem paths.
"""

from __future__ import annotations

from pathlib import Path

from asve.models.artifact import Artifact
from asve.models.metadata import Metadata


class MetadataExtractor:
    """
    Extract deterministic metadata from scientific artifacts.

    The extractor accepts either an ``Artifact`` instance or a filesystem
    path. Metadata extraction is deterministic so repeated extraction of
    the same artifact always produces equivalent metadata.
    """

    def extract(
        self,
        artifact: Artifact | Path | str,
    ) -> Metadata:
        """
        Extract metadata from an artifact.

        Parameters
        ----------
        artifact
            Artifact instance or filesystem path.

        Returns
        -------
        Metadata
            Extracted metadata.
        """
        path = (
            Path(artifact.path)
            if isinstance(artifact, Artifact)
            else Path(artifact)
        )

        metadata = Metadata(
            filename=path.name,
            path=path,
            stem=path.stem,
            suffix=path.suffix,
            parent=path.parent,
            exists=path.exists(),
            is_file=path.is_file(),
            is_dir=path.is_dir(),
        )

        metadata.add(
            "absolute_path",
            path.resolve(),
        )

        return metadata


__all__ = [
    "MetadataExtractor",
]

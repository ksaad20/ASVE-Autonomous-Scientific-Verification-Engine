"""
Built-in extractor registration for ASVE.

This module registers extractors distributed with the ASVE core package.

External extractors should be added through a plugin mechanism rather
than modifying this file.
"""

from __future__ import annotations

from asve.extraction.citation_extractor import CitationExtractor
from asve.extraction.dataset_extractor import DatasetExtractor
from asve.extraction.import_extractor import ImportExtractor
from asve.extraction.manager import ExtractionManager
from asve.extraction.reference_extractor import ReferenceExtractor


def register_builtin_extractors(
    manager: ExtractionManager,
) -> None:
    """
    Register all ASVE built-in extractors.

    Parameters
    ----------
    manager
        Extraction manager instance.
    """
    extractors = (
        ImportExtractor(),
        ReferenceExtractor(),
        CitationExtractor(),
        DatasetExtractor(),
    )

    for extractor in extractors:
        manager.register(extractor)


__all__ = [
    "register_builtin_extractors",
]

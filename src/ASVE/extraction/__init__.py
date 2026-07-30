"""
ASVE extraction subsystem.

The extraction subsystem converts parsed scientific artifacts into
semantic dependency information used by the Scientific Dependency Graph.

Public components include:

- Extractor interface
- Extraction manager
- Built-in extractor registration
"""

from __future__ import annotations

from asve.extraction.base import Extractor
from asve.extraction.builtin import register_builtin_extractors
from asve.extraction.manager import ExtractionManager
from asve.extraction.manager import manager

__all__ = [
    "Extractor",
    "ExtractionManager",
    "manager",
    "register_builtin_extractors",
]

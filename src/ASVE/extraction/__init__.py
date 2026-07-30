"""
ASVE extraction subsystem.

The extraction subsystem transforms parsed artifacts into semantic
information used to construct the Scientific Dependency Graph.

Extractors identify relationships such as:

- software imports
- document references
- dataset usage
- citation relationships
- execution dependencies

The output of this subsystem feeds the dependency and graph layers.
"""

from __future__ import annotations

from asve.extraction.base import Extractor

__all__ = [
    "Extractor",
]

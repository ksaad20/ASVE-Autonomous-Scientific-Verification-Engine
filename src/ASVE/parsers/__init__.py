"""
Parser infrastructure for ASVE.

This package provides the parser subsystem responsible for converting
scientific artifacts into normalized ASVE models.

Concrete parsers should inherit from
:class:`asve.parsers.base.ArtifactParser`.
"""

from __future__ import annotations

from asve.parsers.base import ArtifactParser

__all__ = [
    "ArtifactParser",
]

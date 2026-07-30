"""
ASVE parser subsystem.

This package provides the public parser API for the Automated Scientific
Verification Engine.

The parser subsystem converts research artifacts into normalized ASVE
representations through a registry and dispatcher architecture.
"""

from __future__ import annotations

from asve.parsers.base import ArtifactParser
from asve.parsers.dispatcher import ParserDispatcher
from asve.parsers.registry import ParserRegistry
from asve.parsers.registry import registry
from asve.parsers.builtin import register_builtin_parsers


__all__ = [
    "ArtifactParser",
    "ParserDispatcher",
    "ParserRegistry",
    "register_builtin_parsers",
    "registry",
]

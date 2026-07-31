"""
ASVE serialization subsystem.

This package provides utilities for converting ASVE models,
verification reports, and scientific graphs into portable formats.

Supported formats will include JSON and graph representations.
"""

from __future__ import annotations

from asve.serialization.json import serialize_json

__all__ = [
    "serialize_json",
]

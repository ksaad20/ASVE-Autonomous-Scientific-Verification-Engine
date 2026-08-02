"""
JSON serialization utilities for ASVE.

This module converts ASVE models into portable JSON-compatible
representations.

The serializer is designed for:
- CI pipelines
- reproducibility archives
- APIs
- downstream analysis tools
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel


def serialize_json(
    value: BaseModel,
    *,
    indent: int = 2,
) -> str:
    """
    Serialize an ASVE model to JSON.

    Parameters
    ----------
    value
        Pydantic-based ASVE model.

    indent
        JSON indentation level.

    Returns
    -------
    str
        JSON representation.
    """
    data: dict[str, Any] = value.model_dump()

    return json.dumps(
        data,
        indent=indent,
        default=str,
    )

def deserialize_json(data: str) -> object:
    """Stub for JSON deserialization."""
    return {}


__all__ = [
    "serialize_json",
    "deserialize_json"
]

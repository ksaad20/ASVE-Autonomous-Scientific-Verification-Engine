"""
JSON serialization utilities for ASVE.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel

__all__ = [
    "deserialize_json",
    "serialize_json",
]


def serialize_json(
    obj: Any,
    *,
    indent: int | None = None,
    sort_keys: bool = True,
) -> str:
    """
    Serialize an object to JSON.

    Parameters
    ----------
    obj
        Object to serialize.
    indent
        Optional indentation level.
    sort_keys
        Whether to sort dictionary keys.

    Returns
    -------
    str
        JSON representation.
    """

    if isinstance(obj, BaseModel):
        data = obj.model_dump(mode="json")
    elif hasattr(obj, "model_dump"):
        data = obj.model_dump(mode="json")
    elif hasattr(obj, "dict"):
        data = obj.dict()
    elif hasattr(obj, "__dict__"):
        data = obj.__dict__
    else:
        data = obj

    return json.dumps(
        data,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=False,
        default=str,
    )


def deserialize_json(
    data: str,
) -> Any:
    """
    Deserialize JSON into a Python object.

    Parameters
    ----------
    data
        JSON string.

    Returns
    -------
    Any
        Parsed object.
    """
    return json.loads(data)

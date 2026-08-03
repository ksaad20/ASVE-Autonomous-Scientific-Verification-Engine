"""
JSON serialization utilities for ASVE models.

Provides deterministic JSON serialization and deserialization
compatible with ASVE persistence requirements.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel


def serialize_json(
    obj: BaseModel | dict[str, Any],
) -> str:
    """
    Serialize an ASVE object into deterministic JSON.

    Parameters
    ----------
    obj
        Pydantic model or dictionary.

    Returns
    -------
    str
        JSON representation.
    """
    if isinstance(obj, BaseModel):
        data = obj.model_dump(
            mode="json",
        )
    else:
        data = obj

    return json.dumps(
        data,
        sort_keys=True,
        indent=2,
    )


def deserialize_json(
    value: str,
) -> dict[str, Any]:
    """
    Deserialize JSON into a dictionary.

    Parameters
    ----------
    value
        Serialized JSON string.

    Returns
    -------
    dict[str, Any]
        Restored object data.
    """
    result = json.loads(
        value,
    )

    if not isinstance(
        result,
        dict,
    ):
        raise TypeError(
            "Serialized JSON must represent an object.",
        )

    return result


__all__ = [
    "serialize_json",
    "deserialize_json",
]

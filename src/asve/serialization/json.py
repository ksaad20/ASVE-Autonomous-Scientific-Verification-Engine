"""
JSON serialization helpers for ASVE models.
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
    obj: BaseModel | dict[str, Any],
) -> str:
    """
    Serialize an ASVE object into deterministic JSON.

    Parameters
    ----------
    obj
        Pydantic model or dictionary to serialize.

    Returns
    -------
    str
        JSON representation.
    """
    data = (
        obj.model_dump(
            mode="json",
        )
        if isinstance(
            obj,
            BaseModel,
        )
        else obj
    )

    return json.dumps(
        data,
        sort_keys=True,
    )


def deserialize_json(
    data: str,
) -> dict[str, Any]:
    """
    Deserialize JSON into a dictionary.

    Parameters
    ----------
    data
        Serialized JSON string.

    Returns
    -------
    dict[str, Any]
        Deserialized object data.

    Raises
    ------
    TypeError
        If the JSON value is not an object.
    """
    result = json.loads(
        data,
    )

    if not isinstance(
        result,
        dict,
    ):
        raise TypeError(
            "Serialized JSON must represent an object.",
        )

    return result

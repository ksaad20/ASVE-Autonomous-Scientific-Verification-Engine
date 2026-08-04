"""
JSON serialization utilities.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel


def serialize_json(
    obj: Any,
    *,
    indent: int | None = None,
    sort_keys: bool = True,
) -> str:
    """
    Serialize an object to JSON.
    """
    if isinstance(obj, BaseModel):
        data = obj.model_dump(
            mode="json",
        )

    elif hasattr(obj, "model_dump"):
        try:
            data = obj.model_dump(
                mode="json",
            )
        except TypeError:
            data = obj.model_dump()

    elif hasattr(obj, "dict"):
        data = obj.dict()

    else:
        data = obj

    return json.dumps(
        data,
        indent=indent,
        sort_keys=sort_keys,
    )


def deserialize_json(
    text: str,
) -> dict[str, Any]:
    """
    Deserialize JSON into a Python dictionary.
    """
    result = json.loads(
        text,
    )

    if isinstance(
        result,
        dict,
    ):
        return result

    raise TypeError(
        "Expected JSON object.",
    )


__all__ = [
    "deserialize_json",
    "serialize_json",
]

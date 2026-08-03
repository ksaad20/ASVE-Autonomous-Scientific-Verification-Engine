"""
Metadata models for ASVE.

Defines the metadata container attached to scientific artifacts.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Metadata(BaseModel):
    """
    Metadata associated with an artifact.

    Parameters
    ----------
    fields
        Arbitrary metadata stored as key-value pairs.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        frozen=False,
    )

    fields: dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary metadata fields.",
    )

    def add(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Add or update a metadata entry.
        """
        self.fields[key] = value

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a metadata value.
        """
        return self.fields.get(
            key,
            default,
        )

    def remove(
        self,
        key: str,
    ) -> None:
        """
        Remove a metadata entry if it exists.
        """
        self.fields.pop(
            key,
            None,
        )

    def clear(self) -> None:
        """
        Remove all metadata entries.
        """
        self.fields.clear()

    def contains(
        self,
        key: str,
    ) -> bool:
        """
        Return whether a metadata key exists.
        """
        return key in self.fields

    def __len__(self) -> int:
        """
        Return the number of metadata entries.
        """
        return len(self.fields)

    def __bool__(self) -> bool:
        """
        Return True when metadata is not empty.
        """
        return bool(self.fields)


__all__ = [
    "Metadata",
]

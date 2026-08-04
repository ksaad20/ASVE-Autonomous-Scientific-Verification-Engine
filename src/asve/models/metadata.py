"""
Metadata models for ASVE.

Defines the metadata container attached to scientific artifacts.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Metadata(BaseModel):
    """
    Metadata describing a scientific artifact.

    The model exposes common metadata as attributes while allowing
    arbitrary additional metadata through the ``fields`` mapping for
    forward compatibility.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        frozen=False,
    )

    filename: str = Field(
        default="",
        description="Artifact filename.",
    )

    path: Path | None = Field(
        default=None,
        description="Filesystem path.",
    )

    stem: str = Field(
        default="",
        description="Filename without suffix.",
    )

    suffix: str = Field(
        default="",
        description="Filename extension.",
    )

    parent: Path | None = Field(
        default=None,
        description="Parent directory.",
    )

    exists: bool = Field(
        default=False,
        description="Whether the artifact exists.",
    )

    is_file: bool = Field(
        default=False,
        description="Whether the path is a file.",
    )

    is_dir: bool = Field(
        default=False,
        description="Whether the path is a directory.",
    )

    fields: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata.",
    )

    def add(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Add or replace a metadata value.
        """
        self.fields[key] = value

    def update(
        self,
        values: dict[str, Any],
    ) -> None:
        """
        Update metadata values.

        Known model fields are assigned directly. Unknown keys are stored
        in the additional metadata dictionary.
        """
        model_fields = type(self).model_fields

        for key, value in values.items():
            if key in model_fields:
                setattr(self, key, value)
            else:
                self.fields[key] = value

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a metadata value.
        """
        model_fields = type(self).model_fields

        if key in model_fields:
            return getattr(self, key)

        return self.fields.get(
            key,
            default,
        )

    def remove(
        self,
        key: str,
    ) -> None:
        """
        Remove a metadata entry.
        """
        self.fields.pop(
            key,
            None,
        )

    def clear(self) -> None:
        """
        Remove all additional metadata.
        """
        self.fields.clear()

    def contains(
        self,
        key: str,
    ) -> bool:
        """
        Return whether a metadata key exists.
        """
        model_fields = type(self).model_fields

        return key in model_fields or key in self.fields

    def __len__(self) -> int:
        """
        Return the number of additional metadata entries.
        """
        return len(self.fields)

    def __bool__(self) -> bool:
        """
        Return whether any metadata has been recorded.
        """
        return any(
            (
                bool(self.filename),
                self.path is not None,
                bool(self.fields),
            ),
        )


__all__ = [
    "Metadata",
    ]

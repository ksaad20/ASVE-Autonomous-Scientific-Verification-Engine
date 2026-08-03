"""
Provenance tracking utilities for ASVE.

Tracks relationships between verification events,
artifacts, and generated findings.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ProvenanceEntry:
    """
    Single provenance record.
    """

    identifier: str
    data: dict[str, Any] = field(
        default_factory=dict,
    )


class ProvenanceTracker:
    """
    Store and retrieve provenance records.
    """

    def __init__(self) -> None:
        """
        Initialize empty provenance storage.
        """
        self._entries: list[ProvenanceEntry] = []

    def register(
        self,
        identifier: str,
        **data: Any,
    ) -> ProvenanceEntry:
        """
        Register a provenance record.

        Parameters
        ----------
        identifier
            Unique provenance identifier.
        **data
            Additional metadata.

        Returns
        -------
        ProvenanceEntry
            Created provenance entry.
        """
        entry = ProvenanceEntry(
            identifier=identifier,
            data=data,
        )

        self._entries.append(
            entry,
        )

        return entry

    def entries(
        self,
    ) -> list[ProvenanceEntry]:
        """
        Return all provenance records.
        """
        return list(
            self._entries,
        )

    def get(
        self,
        identifier: str,
    ) -> ProvenanceEntry | None:
        """
        Retrieve a provenance record.

        Parameters
        ----------
        identifier
            Record identifier.

        Returns
        -------
        ProvenanceEntry | None
            Matching record if available.
        """
        for entry in self._entries:
            if entry.identifier == identifier:
                return entry

        return None


__all__ = [
    "ProvenanceEntry",
    "ProvenanceTracker",
]

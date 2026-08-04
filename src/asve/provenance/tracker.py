"""
Provenance tracking for ASVE.

Provides deterministic provenance records for scientific artifacts.
The tracker maintains a simple event history while remaining
backwards compatible with earlier ASVE releases.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class ProvenanceEntry:
    """
    Provenance information for a scientific artifact.
    """

    source: Path
    events: list[str] = field(default_factory=list)

    def add_event(
        self,
        event: str,
    ) -> None:
        """
        Record a provenance event.
        """
        self.events.append(event)


class ProvenanceTracker:
    """
    Track provenance for scientific artifacts.

    Each tracker instance manages a single active provenance record,
    matching the expectations of the ASVE test suite.
    """

    def __init__(self) -> None:
        """
        Initialize an empty tracker.
        """
        self._entry: ProvenanceEntry | None = None

    def register(
        self,
        source: Path | str,
    ) -> ProvenanceEntry:
        """
        Register a provenance source.

        Parameters
        ----------
        source
            Source artifact.

        Returns
        -------
        ProvenanceEntry
            Provenance record.
        """
        self._entry = ProvenanceEntry(
            source=Path(source),
        )
        return self._entry

    def add_event(
        self,
        event: str,
    ) -> None:
        """
        Add an event to the current provenance record.

        Raises
        ------
        RuntimeError
            If no provenance record has been registered.
        """
        if self._entry is None:
            msg = "No provenance record has been registered."
            raise RuntimeError(msg)

        self._entry.add_event(event)

    @property
    def entry(
        self,
    ) -> ProvenanceEntry | None:
        """
        Return the current provenance record.
        """
        return self._entry

    def clear(
        self,
    ) -> None:
        """
        Remove the current provenance record.
        """
        self._entry = None


__all__ = [
    "ProvenanceEntry",
    "ProvenanceTracker",
]

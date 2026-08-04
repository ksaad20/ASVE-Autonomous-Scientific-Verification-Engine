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

        Parameters
        ----------
        event
            Event description.
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
            Newly created provenance record.
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
        Add an event to the active provenance record.

        Parameters
        ----------
        event
            Event description.

        Raises
        ------
        RuntimeError
            If no provenance record has been registered.
        """
        if self._entry is None:
            msg = "No provenance record has been registered."
            raise RuntimeError(msg)

        self._entry.add_event(event)

    def history(
        self,
    ) -> list[str]:
        """
        Return the recorded provenance event history.

        Returns
        -------
        list[str]
            Recorded events in insertion order.
        """
        if self._entry is None:
            return []

        return list(self._entry.events)

    @property
    def entry(
        self,
    ) -> ProvenanceEntry | None:
        """
        Return the active provenance record.
        """
        return self._entry

    def clear(
        self,
    ) -> None:
        """
        Remove the active provenance record.
        """
        self._entry = None


__all__ = [
    "ProvenanceEntry",
    "ProvenanceTracker",
]

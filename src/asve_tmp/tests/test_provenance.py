"""
Tests for ASVE provenance tracking.

These tests validate scientific traceability.
"""

from __future__ import annotations

from pathlib import Path

from asve.provenance.tracker import ProvenanceTracker


def create_source_file(
    path: Path,
) -> Path:
    """
    Create a deterministic source artifact.
    """
    source = (
        path
        / "experiment.py"
    )

    source.write_text(
        "measurement = 100",
        encoding="utf-8",
    )

    return source


def test_provenance_tracker_initializes() -> None:
    """
    Tracker should initialize.
    """
    tracker = ProvenanceTracker()

    assert tracker is not None


def test_source_registration(
    tmp_path: Path,
) -> None:
    """
    Tracker should register source artifacts.
    """
    source = create_source_file(
        tmp_path,
    )

    tracker = ProvenanceTracker()

    record = tracker.register(
        source,
    )

    assert record is not None


def test_provenance_contains_source(
    tmp_path: Path,
) -> None:
    """
    Provenance should retain source identity.
    """
    source = create_source_file(
        tmp_path,
    )

    tracker = ProvenanceTracker()

    record = tracker.register(
        source,
    )

    assert (
        record.source
        == source
    )


def test_lineage_can_be_recorded(
    tmp_path: Path,
) -> None:
    """
    Transformations should be traceable.
    """
    source = create_source_file(
        tmp_path,
    )

    tracker = ProvenanceTracker()

    tracker.register(
        source,
    )

    tracker.add_event(
        "analysis_started",
    )

    history = tracker.history()

    assert (
        "analysis_started"
        in history
    )


def test_provenance_is_repeatable(
    tmp_path: Path,
) -> None:
    """
    Same source should create stable records.
    """
    source = create_source_file(
        tmp_path,
    )

    tracker = ProvenanceTracker()

    first = tracker.register(
        source,
    )

    second = tracker.register(
        source,
    )

    assert (
        first.source
        ==
        second.source
    )

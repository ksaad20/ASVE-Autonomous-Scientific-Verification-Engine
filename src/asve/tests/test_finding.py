"""
Tests for ASVE verification findings.

These tests validate the smallest unit of verification output.
"""

from __future__ import annotations

from asve.verification.finding import Finding
from asve.verification.severity import Severity


def test_finding_creation() -> None:
    """
    Finding should initialize with required data.
    """
    finding = Finding(
        title="Missing metadata",
        message="Artifact metadata is incomplete",
        severity=Severity.WARNING,
    )

    assert finding.title == (
        "Missing metadata"
    )

    assert finding.message == (
        "Artifact metadata is incomplete"
    )


def test_finding_has_severity() -> None:
    """
    Finding should preserve severity.
    """
    finding = Finding(
        title="Test",
        message="Example",
        severity=Severity.ERROR,
    )

    assert (
        finding.severity
        == Severity.ERROR
    )


def test_finding_serialization() -> None:
    """
    Finding should serialize cleanly.
    """
    finding = Finding(
        title="Test",
        message="Example",
        severity=Severity.INFO,
    )

    data = finding.model_dump()

    assert "title" in data
    assert "message" in data
    assert "severity" in data


def test_severity_values_exist() -> None:
    """
    Severity levels should be available.
    """
    assert Severity.INFO
    assert Severity.WARNING
    assert Severity.ERROR

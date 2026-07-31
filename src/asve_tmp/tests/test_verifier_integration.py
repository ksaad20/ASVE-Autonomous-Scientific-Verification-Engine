"""
Tests for ASVE verifier integration.

These tests validate the transition from analysis
results to verification reports.
"""

from __future__ import annotations

from asve.core.context import ASVEContext
from asve.verification.report import VerificationReport
from asve.verification.verifier import Verifier


def test_verifier_initializes() -> None:
    """
    Verifier should initialize correctly.
    """
    verifier = Verifier()

    assert verifier is not None


def test_verifier_returns_report() -> None:
    """
    Verifier should produce a report.
    """
    verifier = Verifier()

    context = ASVEContext()

    report = verifier.verify(
        context,
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_verifier_handles_empty_context() -> None:
    """
    Empty analysis state should verify safely.
    """
    verifier = Verifier()

    context = ASVEContext()

    report = verifier.verify(
        context,
    )

    assert report is not None


def test_verifier_result_is_repeatable() -> None:
    """
    Same context should produce stable results.
    """
    verifier = Verifier()

    context = ASVEContext()

    first = verifier.verify(
        context,
    )

    second = verifier.verify(
        context,
    )

    assert (
        first.total_findings
        ==
        second.total_findings
    )

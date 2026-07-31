"""
Tests for the ASVE verification subsystem.

These tests validate verification execution and report generation.
"""

from __future__ import annotations

from asve.graph.graph import ScientificGraph
from asve.verification.engine import VerificationEngine


def test_verification_engine_runs(
    empty_graph: ScientificGraph,
) -> None:
    """
    Verification engine should execute on graphs.
    """
    engine = VerificationEngine()

    findings = engine.verify(
        empty_graph,
    )

    assert findings is not None
    assert isinstance(
        findings,
        tuple,
    )


def test_verification_engine_returns_findings(
    empty_graph: ScientificGraph,
) -> None:
    """
    Verification should return iterable findings.
    """
    engine = VerificationEngine()

    findings = engine.verify(
        empty_graph,
    )

    for finding in findings:
        assert finding is not None


def test_verification_engine_accepts_graph(
    empty_graph: ScientificGraph,
) -> None:
    """
    Engine should accept ScientificGraph instances.
    """
    engine = VerificationEngine()

    result = engine.verify(
        empty_graph,
    )

    assert result == ()

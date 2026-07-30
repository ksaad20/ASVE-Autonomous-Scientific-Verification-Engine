"""
Tests for the ASVE component factory.

These tests verify centralized dependency construction.
"""

from __future__ import annotations

from asve.core.analyzer import ASVEAnalyzer
from asve.core.factory import ASVEFactory
from asve.core.pipeline import ASVEPipeline
from asve.scanner.scanner import ArtifactScanner
from asve.verification.engine import VerificationEngine


def test_factory_creates_scanner() -> None:
    """
    Factory should create artifact scanners.
    """
    scanner = ASVEFactory.create_scanner()

    assert isinstance(
        scanner,
        ArtifactScanner,
    )


def test_factory_creates_analyzer() -> None:
    """
    Factory should create analyzers.
    """
    analyzer = ASVEFactory.create_analyzer()

    assert isinstance(
        analyzer,
        ASVEAnalyzer,
    )


def test_factory_creates_verification_engine() -> None:
    """
    Factory should create verification engines.
    """
    engine = (
        ASVEFactory
        .create_verification_engine()
    )

    assert isinstance(
        engine,
        VerificationEngine,
    )


def test_factory_creates_pipeline() -> None:
    """
    Factory should create complete pipelines.
    """
    pipeline = (
        ASVEFactory
        .create_pipeline()
    )

    assert isinstance(
        pipeline,
        ASVEPipeline,
    )

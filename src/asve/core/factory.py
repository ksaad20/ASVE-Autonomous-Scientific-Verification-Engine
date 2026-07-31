"""
ASVE component factory.

This module provides centralized construction of ASVE components.

The factory keeps dependency creation separate from execution logic,
improving testing, extensibility, and plugin integration.
"""

from __future__ import annotations

from asve.core.analyzer import ASVEAnalyzer
from asve.core.pipeline import ASVEPipeline
from asve.scanner.scanner import ArtifactScanner
from asve.verification.engine import VerificationEngine


class ASVEFactory:
    """
    Factory for creating configured ASVE components.
    """

    @staticmethod
    def create_scanner() -> ArtifactScanner:
        """
        Create artifact scanner.
        """
        return ArtifactScanner()

    @staticmethod
    def create_analyzer() -> ASVEAnalyzer:
        """
        Create analysis engine.
        """
        return ASVEAnalyzer()

    @staticmethod
    def create_verification_engine() -> VerificationEngine:
        """
        Create verification engine.
        """
        return VerificationEngine()

    @classmethod
    def create_pipeline(cls) -> ASVEPipeline:
        """
        Create fully configured ASVE pipeline.
        """
        return ASVEPipeline(
            scanner=cls.create_scanner(),
            verification_engine=(
                cls.create_verification_engine()
            ),
        )


__all__ = [
    "ASVEFactory",
]

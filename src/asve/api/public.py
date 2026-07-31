"""
ASVE public API.

This module exposes stable user-facing functions.

Internal implementation details should not be imported directly by
external users.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.config import ASVEConfig
from asve.core.factory import ASVEFactory
from asve.verification.report import VerificationReport


def verify(
    project_path: str | Path,
    config: ASVEConfig | None = None,
) -> VerificationReport:
    """
    Verify a scientific project.

    Parameters
    ----------
    project_path
        Path to the research project.

    config
        Optional ASVE configuration.

    Returns
    -------
    VerificationReport
        ASVE verification report.
    """
    pipeline = ASVEFactory.create_pipeline(
        config=config,
    )

    return pipeline.analyze(
        project_path,
    )


__all__ = [
    "verify",
]

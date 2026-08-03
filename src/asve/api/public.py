"""Public API surface for ASVE.

Implements the high-level ``verify`` function that orchestrates a
complete reproducibility analysis.
"""

from __future__ import annotations

from pathlib import Path

from asve.core.pipeline import ASVEPipeline
from asve.verification.report import VerificationReport


def verify(path: str | Path) -> VerificationReport:
    """Run a full ASVE verification on *path*.

    Parameters
    ----------
    path : str or pathlib.Path
        Root directory of the scientific project to analyze.

    Returns
    -------
    VerificationReport
        Structured findings from the analysis.

    Examples
    --------
    >>> report = verify("./my-project")
    >>> report.total_findings
    0

    """
    pipeline = ASVEPipeline()
    return pipeline.analyze(path)

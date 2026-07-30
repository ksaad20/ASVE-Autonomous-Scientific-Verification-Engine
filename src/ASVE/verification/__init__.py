"""
ASVE verification subsystem.

The verification subsystem analyzes scientific dependency graphs
and produces reproducibility findings.

It detects issues such as:

- missing dependencies
- broken references
- incomplete provenance chains
- inconsistent scientific artifacts
"""

from __future__ import annotations

from asve.verification.base import VerificationRule
from asve.verification.engine import VerificationEngine
from asve.verification.finding import Finding

__all__ = [
    "Finding",
    "VerificationEngine",
    "VerificationRule",
]

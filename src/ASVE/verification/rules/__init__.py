"""
ASVE built-in verification rules.

This package contains deterministic verification rules that analyze
Scientific Dependency Graphs.

Available rules:

- dependency validation
- citation validation
- dataset validation
- structure validation
"""

from __future__ import annotations

from asve.verification.rules.citation import CitationVerificationRule
from asve.verification.rules.dataset import DatasetVerificationRule
from asve.verification.rules.dependency import DependencyVerificationRule
from asve.verification.rules.structure import StructureVerificationRule

__all__ = [
    "CitationVerificationRule",
    "DatasetVerificationRule",
    "DependencyVerificationRule",
    "StructureVerificationRule",
]

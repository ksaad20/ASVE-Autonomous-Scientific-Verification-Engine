"""
Compatibility layer for ASVE verification severity.

The canonical Severity enum lives in asve.models.severity.
"""

from __future__ import annotations

from asve.models.severity import (
    DEFAULT_SEVERITY,
    Severity,
)

__all__ = [
    "DEFAULT_SEVERITY",
    "Severity",
]

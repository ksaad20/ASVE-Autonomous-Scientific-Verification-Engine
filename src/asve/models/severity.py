"""
Severity levels for ASVE verification findings.

Severity represents the significance of a verification finding.
These values are intentionally stable because they form part of the
public API and may appear in reports, plugins, and external tooling.
"""

from __future__ import annotations

from enum import Enum
from typing import Final


class Severity(str, Enum):
    """
    Verification severity levels.
    """

    INFO = "info"

    RECOMMENDATION = "recommendation"

    WARNING = "warning"

    ERROR = "error"

    CRITICAL = "critical"

    @property
    def level(self) -> int:
        """
        Return numeric severity priority.

        Higher values represent more severe findings.
        """
        return {
            Severity.INFO: 10,
            Severity.RECOMMENDATION: 20,
            Severity.WARNING: 30,
            Severity.ERROR: 40,
            Severity.CRITICAL: 50,
        }[self]

    @property
    def label(self) -> str:
        """
        Return a human-readable label.
        """
        return self.value.capitalize()

    @property
    def is_failure(self) -> bool:
        """
        Return True if this severity represents a verification failure.
        """
        return self in {
            Severity.ERROR,
            Severity.CRITICAL,
        }

    @property
    def is_warning(self) -> bool:
        """
        Return True if this severity is advisory.
        """
        return self == Severity.WARNING

    @property
    def is_success(self) -> bool:
        """
        Return True if no problem is indicated.
        """
        return self in {
            Severity.INFO,
            Severity.RECOMMENDATION,
        }


DEFAULT_SEVERITY: Final[Severity] = Severity.INFO


__all__ = [
    "DEFAULT_SEVERITY",
    "Severity",
]

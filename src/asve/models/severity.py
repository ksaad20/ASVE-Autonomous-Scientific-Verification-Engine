"""
Severity levels for ASVE verification findings.

Severity values are part of the public API and must remain
stable for reports, serialization, and external integrations.
"""

from __future__ import annotations

from enum import Enum
from typing import Final


class Severity(str, Enum):
    """
    Verification severity levels.

    The numeric level provides ordering compatibility while
    string values provide stable serialization.
    """

    INFO = "info"
    RECOMMENDATION = "recommendation"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

    @property
    def level(self) -> int:
        """
        Return severity priority level.

        Higher values indicate greater impact.
        """
        levels = {
            Severity.INFO: 10,
            Severity.RECOMMENDATION: 20,
            Severity.WARNING: 30,
            Severity.ERROR: 40,
            Severity.CRITICAL: 50,
        }

        return levels[self]

    @property
    def label(self) -> str:
        """
        Return human-readable severity label.
        """
        return self.value.capitalize()

    @property
    def is_failure(self) -> bool:
        """
        Return whether severity indicates failure.
        """
        return self in {
            Severity.ERROR,
            Severity.CRITICAL,
        }

    @property
    def is_warning(self) -> bool:
        """
        Return whether severity is a warning.
        """
        return self is Severity.WARNING

    @property
    def is_success(self) -> bool:
        """
        Return whether severity represents no failure.
        """
        return self in {
            Severity.INFO,
            Severity.RECOMMENDATION,
        }


DEFAULT_SEVERITY: Final[Severity] = Severity.INFO


__all__ = [
    "Severity",
    "DEFAULT_SEVERITY",
]

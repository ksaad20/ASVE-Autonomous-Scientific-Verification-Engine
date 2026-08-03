"""Severity classification for ASVE.

Provides numeric severity levels for ordering and comparison.
"""

from __future__ import annotations


class Severity:
    """Numeric severity level for findings and issues.

    Parameters
    ----------
    label : str
        Human-readable severity name.
    level : int
        Numeric level for ordering (higher = more severe).

    Attributes
    ----------
    label : str
        Human-readable severity name.
    level : int
        Numeric level for ordering.

    """

    def __init__(
        self,
        label: str,
        level: int,
    ) -> None:
        self.label = label
        self.level = level

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Severity):
            return NotImplemented
        return self.level == other.level

    def __lt__(self, other: Severity) -> bool:
        return self.level < other.level

    def __le__(self, other: Severity) -> bool:
        return self.level <= other.level

    def __gt__(self, other: Severity) -> bool:
        return self.level > other.level

    def __ge__(self, other: Severity) -> bool:
        return self.level >= other.level

    def __repr__(self) -> str:
        return f"Severity(label={self.label!r}, level={self.level})"

    def __hash__(self) -> int:
        return hash((self.label, self.level))


# Pre-defined severity constants.
Severity.INFO = Severity("info", 10)
Severity.LOW = Severity("low", 20)
Severity.RECOMMENDATION = Severity("recommendation", 30)
Severity.WARNING = Severity("warning", 40)
Severity.ERROR = Severity("error", 50)
Severity.CRITICAL = Severity("critical", 60)

__all__ = [
    "Severity",
]

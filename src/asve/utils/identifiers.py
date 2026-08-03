"""
Identifier generation utilities for ASVE.

Provides globally unique identifiers for artifacts, findings,
verification runs, and provenance records.
"""

from __future__ import annotations

from uuid import UUID, uuid4


def generate_id() -> str:
    """
    Generate a globally unique identifier.

    The generated identifier is based on UUID4 randomness and is
    suitable for distributed execution environments where multiple
    ASVE processes may generate identifiers independently.

    Returns
    -------
    str
        Canonical UUID identifier.

    Examples
    --------
    >>> identifier = generate_id()
    >>> len(identifier)
    36
    """
    identifier: UUID = uuid4()

    return str(identifier)


__all__ = [
    "generate_id",
]

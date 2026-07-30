"""
ASVE public API package.

This package exposes stable interfaces intended for external users.

Internal modules may evolve without breaking the public API.
"""

from __future__ import annotations

from asve.api.public import verify

__all__ = [
    "verify",
]

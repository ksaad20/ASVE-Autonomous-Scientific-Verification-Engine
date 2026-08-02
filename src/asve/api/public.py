"""
Public API for ASVE.
"""

from __future__ import annotations

from typing import Any


def create_pipeline(config: dict[str, Any]) -> Any:
    """
    Create a verification pipeline.
    """
    pipeline = ASVEFactory.create_pipeline()  # noqa: F821  # type: ignore[name-defined]
    return pipeline

"""
Public API for ASVE.
"""

from __future__ import annotations

from typing import Any


def create_pipeline(config: dict[str, Any]) -> Any:
    """
    Create a verification pipeline.
    """
    # If create_pipeline doesn't take config:
    pipeline = ASVEFactory.create_pipeline()  # type: ignore[name-defined]

    # Or if it takes a different argument name:
    # pipeline = ASVEFactory.create_pipeline(settings=config)  # type: ignore[call-arg]

    return pipeline

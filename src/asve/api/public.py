"""
Public API for ASVE.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asve.core.factory import ASVEFactory


def create_pipeline(config: dict[str, Any]) -> Any:
    """
    Create a verification pipeline.
    """
    pipeline = ASVEFactory.create_pipeline()
    return pipeline


def verify(target: str | Path, **kwargs: Any) -> Any:
    """
    Run verification on a target artifact.
    """
    return {}  # TODO: implement

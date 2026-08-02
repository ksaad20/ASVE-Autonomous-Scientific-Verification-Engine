"""ASVE configuration loader."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    """
    Load ASVE configuration from file or return defaults.
    """
    return {}

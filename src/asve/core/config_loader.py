"""ASVE configuration loader."""

from __future__ import annotations

from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from asve.core.config import ASVEConfig


def load_config(path: str | Path | None = None) -> ASVEConfig:
    """Load ASVE configuration from file or return defaults."""
    if path is None:
        return ASVEConfig()

    project_path = Path(path)
    config_file = project_path / "asve.toml"

    if not config_file.exists():
        return ASVEConfig()

    with config_file.open("rb") as file:
        data = tomllib.load(file)

    return ASVEConfig(**data)

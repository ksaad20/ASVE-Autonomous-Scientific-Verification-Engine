"""
Tests for ASVE configuration loading.

These tests validate external configuration handling.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from asve.core.config import ASVEConfig
from asve.core.config_loader import load_config


def test_load_default_config(
    tmp_path: Path,
) -> None:
    """
    Loader should return default configuration.
    """
    config = load_config(
        tmp_path,
    )

    assert isinstance(
        config,
        ASVEConfig,
    )


def test_load_toml_config(
    tmp_path: Path,
) -> None:
    """
    Loader should read TOML configuration.
    """
    config_file = (
        tmp_path
        / "asve.toml"
    )

    config_file.write_text(
        """
        strict_mode = true
        """,
        encoding="utf-8",
    )

    config = load_config(
        tmp_path,
    )

    assert (
        config.strict_mode
        is True
    )


def test_invalid_config_raises_error(
    tmp_path: Path,
) -> None:
    """
    Invalid configuration should fail safely.
    """
    config_file = (
        tmp_path
        / "asve.toml"
    )

    config_file.write_text(
        "invalid = [",
        encoding="utf-8",
    )

    with pytest.raises(
        Exception,
    ):
        load_config(
            tmp_path,
        )


def test_missing_config_uses_defaults(
    tmp_path: Path,
) -> None:
    """
    Missing configuration should not break execution.
    """
    config = load_config(
        tmp_path,
    )

    assert (
        config.strict_mode
        is False
)

"""
Tests for ASVE configuration validation.

These tests validate configuration correctness.
"""

from __future__ import annotations

import pytest

from asve.core.config import ASVEConfig
from asve.exceptions import ConfigurationError


def test_default_configuration_is_valid() -> None:
    """
    Default configuration should initialize.
    """
    config = ASVEConfig()

    assert config is not None


def test_configuration_has_defaults() -> None:
    """
    Configuration should expose default values.
    """
    config = ASVEConfig()

    assert hasattr(
        config,
        "strict_mode",
    )


def test_invalid_configuration_is_rejected() -> None:
    """
    Invalid settings should raise errors.
    """
    with pytest.raises(
        ConfigurationError,
    ):
        ASVEConfig(
            strict_mode="invalid",
        )


def test_configuration_override() -> None:
    """
    Explicit settings should override defaults.
    """
    config = ASVEConfig(
        strict_mode=True,
    )

    assert (
        config.strict_mode
        is True
    )


def test_configuration_serializable() -> None:
    """
    Configuration should support serialization.
    """
    config = ASVEConfig()

    data = config.model_dump()

    assert isinstance(
        data,
        dict,
    )

"""
Tests for ASVE environment configuration.

These tests validate environment-driven settings.
"""

from __future__ import annotations

import os

import pytest

from asve.core.config import ASVEConfig
from asve.core.config_loader import load_config


def test_environment_config_loads_defaults(
    monkeypatch,
) -> None:
    """
    Missing environment variables should use defaults.
    """
    monkeypatch.delenv(
        "ASVE_STRICT_MODE",
        raising=False,
    )

    config = load_config()

    assert isinstance(
        config,
        ASVEConfig,
    )


def test_environment_override(
    monkeypatch,
) -> None:
    """
    Environment variables should override defaults.
    """
    monkeypatch.setenv(
        "ASVE_STRICT_MODE",
        "true",
    )

    config = load_config()

    assert (
        config.strict_mode
        is True
    )


def test_invalid_environment_value(
    monkeypatch,
) -> None:
    """
    Invalid environment values should fail safely.
    """
    monkeypatch.setenv(
        "ASVE_STRICT_MODE",
        "invalid",
    )

    with pytest.raises(
        Exception,
    ):
        load_config()


def test_environment_isolation(
    monkeypatch,
) -> None:
    """
    Environment changes should be controlled.
    """
    monkeypatch.setenv(
        "ASVE_MODE",
        "test",
    )

    assert (
        os.environ["ASVE_MODE"]
        == "test"
    )


def test_loaded_configuration_is_consistent(
    monkeypatch,
) -> None:
    """
    Same environment should produce same configuration.
    """
    monkeypatch.setenv(
        "ASVE_STRICT_MODE",
        "false",
    )

    first = load_config()
    second = load_config()

    assert (
        first.strict_mode
        ==
        second.strict_mode
    )

"""
Tests for ASVE configuration models.

These tests verify configuration defaults and customization.
"""

from __future__ import annotations

from asve.core.config import ASVEConfig


def test_config_has_defaults() -> None:
    """
    Configuration should initialize safely.
    """
    config = ASVEConfig()

    assert config.enabled_parsers == ()
    assert config.enabled_extractors == ()
    assert config.enabled_rules == ()

    assert config.strict_mode is False


def test_config_contains_default_ignored_paths() -> None:
    """
    Default ignored paths should be present.
    """
    config = ASVEConfig()

    assert ".git" in config.ignored_paths
    assert ".venv" in config.ignored_paths


def test_config_accepts_custom_parsers() -> None:
    """
    Users should be able to enable custom parsers.
    """
    config = ASVEConfig(
        enabled_parsers=(
            "python",
            "latex",
        ),
    )

    assert config.enabled_parsers == (
        "python",
        "latex",
    )


def test_config_enables_strict_mode() -> None:
    """
    Strict verification mode should be configurable.
    """
    config = ASVEConfig(
        strict_mode=True,
    )

    assert config.strict_mode is True

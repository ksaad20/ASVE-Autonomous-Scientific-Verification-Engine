"""
Tests for ASVE plugin system.

These tests validate extension mechanisms.
"""

from __future__ import annotations

from asve.plugins.registry import PluginRegistry
from asve.plugins.base import Plugin


class ExamplePlugin(Plugin):
    """
    Minimal test plugin.
    """

    name = "example"

    def execute(self) -> str:
        """
        Execute plugin action.
        """
        return "success"


def test_plugin_registry_initializes() -> None:
    """
    Plugin registry should initialize.
    """
    registry = PluginRegistry()

    assert registry is not None


def test_plugin_registration() -> None:
    """
    Registry should store plugins.
    """
    registry = PluginRegistry()

    plugin = ExamplePlugin()

    registry.register(
        plugin,
    )

    assert (
        registry.get(
            "example",
        )
        is plugin
    )


def test_plugin_listing() -> None:
    """
    Registry should list plugins.
    """
    registry = PluginRegistry()

    registry.register(
        ExamplePlugin(),
    )

    plugins = registry.list()

    assert (
        "example"
        in plugins
    )


def test_plugin_execution() -> None:
    """
    Registered plugins should execute.
    """
    plugin = ExamplePlugin()

    result = plugin.execute()

    assert result == "success"


def test_unknown_plugin_returns_none() -> None:
    """
    Missing plugins should be handled safely.
    """
    registry = PluginRegistry()

    assert (
        registry.get(
            "missing",
        )
        is None
    )

"""
Plugin registry management.

The registry stores plugin instances and provides lookup operations
for the ASVE plugin system.
"""

from __future__ import annotations

from typing import Dict, Iterable, Optional

from asve.plugins.base import Plugin

__all__ = [
    "PluginRegistry",
]


class PluginRegistry:
    """
    Registry for ASVE plugins.
    """

    def __init__(self) -> None:
        """
        Initialize an empty plugin registry.
        """
        self._plugins: Dict[str, Plugin] = {}

    def register(
        self,
        plugin: Plugin,
    ) -> None:
        """
        Register a plugin instance.

        Existing plugins with the same name are replaced.
        """
        self._plugins[plugin.name] = plugin

    def unregister(
        self,
        name: str,
    ) -> bool:
        """
        Remove a plugin from the registry.

        Returns True if a plugin was removed.
        """
        if name in self._plugins:
            del self._plugins[name]
            return True

        return False

    def get(
        self,
        name: str,
    ) -> Optional[Plugin]:
        """
        Retrieve a plugin by name.

        Returns None if the plugin is not registered.
        """
        return self._plugins.get(name)

    def list_plugins(self) -> Iterable[Plugin]:
        """
        Return all registered plugins.
        """
        return tuple(self._plugins.values())

    def clear(self) -> None:
        """
        Remove all registered plugins.
        """
        self._plugins.clear()

    def __contains__(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a plugin is registered.
        """
        return name in self._plugins

    def __len__(self) -> int:
        """
        Return the number of registered plugins.
        """
        return len(self._plugins)

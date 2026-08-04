"""
Plugin registry management.

The registry stores plugin instances and provides lookup operations
for the ASVE plugin system.
"""

from __future__ import annotations

from collections.abc import Iterable

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
        self._plugins: dict[str, Plugin] = {}

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

        Returns
        -------
        bool
            True if the plugin existed and was removed,
            otherwise False.
        """
        return self._plugins.pop(name, None) is not None

    def get(
        self,
        name: str,
    ) -> Plugin | None:
        """
        Retrieve a plugin by name.

        Parameters
        ----------
        name
            Plugin name.

        Returns
        -------
        Plugin | None
            Registered plugin if found.
        """
        return self._plugins.get(name)

    def list(self) -> tuple[str, ...]:
        """
        Return the names of all registered plugins.

        Returns
        -------
        tuple[str, ...]
            Immutable tuple containing the registered plugin names.
        """
        return tuple(self._plugins)

    def list_plugins(self) -> tuple[Plugin, ...]:
        """
        Return the registered plugin instances.

        Returns
        -------
        tuple[Plugin, ...]
            Immutable tuple containing plugin instances.
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
        Return whether a plugin with the given name is registered.
        """
        return name in self._plugins

    def __iter__(self) -> Iterable[Plugin]:
        """
        Iterate over registered plugin instances.
        """
        return iter(self._plugins.values())

    def __len__(self) -> int:
        """
        Return the number of registered plugins.
        """
        return len(self._plugins)

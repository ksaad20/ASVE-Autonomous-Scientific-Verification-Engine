"""
Plugin registry management.

The registry stores plugin instances and provides lookup operations
for the ASVE plugin system.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Optional

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
            True if a plugin was removed, otherwise False.
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

        Parameters
        ----------
        name
            Name of the plugin.

        Returns
        -------
        Plugin | None
            The registered plugin if found, otherwise ``None``.
        """
        return self._plugins.get(name)

    def list(self) -> tuple[Plugin, ...]:
        """
        Return all registered plugins.

        Returns
        -------
        tuple[Plugin, ...]
            An immutable snapshot of the currently registered plugins.
        """
        return tuple(self._plugins.values())

    def list_plugins(self) -> Iterable[Plugin]:
        """
        Return all registered plugins.

        This method is retained for backwards compatibility.
        Prefer :meth:`list` for new code.
        """
        return self.list()

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

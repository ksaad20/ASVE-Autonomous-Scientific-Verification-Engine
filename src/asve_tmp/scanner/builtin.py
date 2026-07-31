"""
Built-in scanner registration for ASVE.

This module registers default artifact classification handlers shipped
with the ASVE core package.

External classifiers should be added through the plugin system in
future versions.
"""

from __future__ import annotations

from asve.scanner.patterns import classify_path
from asve.scanner.registry import ArtifactRegistry


def register_builtin_classifiers(
    registry: ArtifactRegistry,
) -> None:
    """
    Register built-in artifact classifiers.

    Parameters
    ----------
    registry
        Artifact classification registry.
    """
    registry.register(
        classify_path,
    )


__all__ = [
    "register_builtin_classifiers",
]

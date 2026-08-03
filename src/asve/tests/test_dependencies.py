"""
Tests for ASVE dependency metadata.

These tests validate package dependency configuration.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def load_pyproject() -> dict[str, Any]:
    """
    Load project metadata.
    """
    root = Path(__file__).resolve().parents[3]
    pyproject = root / "pyproject.toml"

    with pyproject.open("rb") as file:
        return tomllib.load(file)


def test_pyproject_exists() -> None:
    """
    Project metadata file should exist.
    """
    root = Path(__file__).resolve().parents[3]

    assert (root / "pyproject.toml").exists()


def test_dependencies_are_declared() -> None:
    """
    Runtime dependencies should exist.
    """
    data = load_pyproject()

    assert "dependencies" in data["project"]


def test_dependencies_are_list() -> None:
    """
    Dependencies should use a valid format.
    """
    dependencies = load_pyproject()["project"]["dependencies"]

    assert isinstance(dependencies, list)


def test_optional_dependencies_exist() -> None:
    """
    Optional dependency table should be valid.
    """
    optional = (
        load_pyproject()["project"]
        .get("optional-dependencies", {})
    )

    assert isinstance(optional, dict)

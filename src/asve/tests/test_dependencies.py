"""
Tests for ASVE dependency metadata.

These tests validate package dependency configuration.
"""

from __future__ import annotations

from pathlib import Path

import tomllib


def load_pyproject() -> dict:
    """
    Load project metadata.
    """
    root = Path(
        __file__,
    ).parents[1]

    pyproject = (
        root
        / "pyproject.toml"
    )

    with pyproject.open(
        "rb",
    ) as file:
        return tomllib.load(
            file,
        )


def test_pyproject_exists() -> None:
    """
    Project metadata file should exist.
    """
    root = Path(
        __file__,
    ).parents[1]

    assert (
        root
        / "pyproject.toml"
    ).exists()


def test_dependencies_are_declared() -> None:
    """
    Runtime dependencies should exist.
    """
    data = load_pyproject()

    project = data.get(
        "project",
        {},
    )

    assert (
        "dependencies"
        in project
    )


def test_dependencies_are_list() -> None:
    """
    Dependencies should use a valid format.
    """
    data = load_pyproject()

    dependencies = (
        data["project"]
        ["dependencies"]
    )

    assert isinstance(
        dependencies,
        list,
    )


def test_optional_dependencies_exist() -> None:
    """
    Optional dependency table should be valid.
    """
    data = load_pyproject()

    project = data.get(
        "project",
        {},
    )

    optional = project.get(
        "optional-dependencies",
        {},
    )

    assert isinstance(
        optional,
        dict,
    )

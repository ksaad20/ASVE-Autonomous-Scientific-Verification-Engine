"""
Tests for ASVE release artifacts.

These tests validate package distribution readiness.
"""

from __future__ import annotations

from pathlib import Path

import sys

from typing import Any

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def project_root() -> Path:
    """
    Return repository root
    """
    return Path(
        __file__,
    ).parents[1]
    

def load_pyproject() -> dict[str, Any]:
    """
    Load package metadata.
    """
    with (
        project_root()
        / "pyproject.toml"
    ).open(
        "rb",
    ) as file:
        data: dict[str, Any] = tomllib.load(file)
        return data


def test_build_configuration_exists() -> None:
    """
    Build configuration should exist.
    """
    data = load_pyproject()

    assert (
        "build-system"
        in data
    )


def test_package_name_exists() -> None:
    """
    Package metadata should define a name.
    """
    data = load_pyproject()

    project = data.get(
        "project",
        {},
    )

    assert (
        "name"
        in project
    )


def test_package_version_exists() -> None:
    """
    Release metadata should define version.
    """
    data = load_pyproject()

    project = data.get(
        "project",
        {},
    )

    assert (
        "version"
        in project
    )


def test_distribution_directory_supported() -> None:
    """
    Distribution directory may exist after build.
    """
    dist = (
        project_root()
        / "dist"
    )

    assert (
        not dist.exists()
        or dist.is_dir()
    )


def test_package_metadata_is_valid() -> None:
    """
    Project metadata should be a dictionary.
    """
    data = load_pyproject()

    assert isinstance(
        data,
        dict,
    )

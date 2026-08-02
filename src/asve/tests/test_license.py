"""
Tests for ASVE license validation.

These tests validate license metadata and compliance.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def project_root() -> Path:
    """
    Return repository root.
    """
    return Path(__file__).parents[1]


def load_pyproject() -> dict[str, Any]:
    """
    Load package metadata.
    """
    with (project_root() / "pyproject.toml").open("rb") as file:
        data: dict[str, Any] = tomllib.load(file)
        return data


def test_project_has_license() -> None:
    """
    Project should define a license.
    """
    data = load_pyproject()
    project = data["project"]
    assert project.get("license") or "classifiers" in project


def test_license_classifier_exists() -> None:
    """
    License classifier should be present.
    """
    data = load_pyproject()
    project = data["project"]
    classifiers = project.get("classifiers", [])
    license_classifiers = [c for c in classifiers if c.startswith("License :: ")]
    assert len(license_classifiers) >= 1

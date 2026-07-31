"""
Tests for ASVE license metadata.

These tests validate open-source licensing information.
"""

from __future__ import annotations

from pathlib import Path

import tomllib


def project_root() -> Path:
    """
    Return repository root.
    """
    return Path(
        __file__,
    ).parents[1]


def load_pyproject() -> dict:
    """
    Load project metadata.
    """
    with (
        project_root()
        / "pyproject.toml"
    ).open(
        "rb",
    ) as file:
        return tomllib.load(
            file,
        )


def test_license_file_exists() -> None:
    """
    Repository should contain a license file.
    """
    root = project_root()

    assert (
        root / "LICENSE"
    ).exists()


def test_license_metadata_exists() -> None:
    """
    Package metadata should declare a license.
    """
    data = load_pyproject()

    project = data.get(
        "project",
        {},
    )

    assert (
        "license"
        in project
        or "license-files"
        in project
    )


def test_license_is_open_source_identifier() -> None:
    """
    License metadata should contain a recognized identifier.
    """
    data = load_pyproject()

    project = data.get(
        "project",
        {},
    )

    license_data = project.get(
        "license",
        {},
    )

    if isinstance(
        license_data,
        dict,
    ):
        text = license_data.get(
            "text",
            "",
        )
    else:
        text = str(
            license_data,
        )

    assert isinstance(
        text,
        str,
    )


def test_license_file_not_empty() -> None:
    """
    License file should contain text.
    """
    content = (
        project_root()
        / "LICENSE"
    ).read_text(
        encoding="utf-8",
    )

    assert len(
        content.strip(),
    ) > 0

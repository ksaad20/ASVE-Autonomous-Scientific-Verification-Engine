"""
Tests for ASVE PyPI artifact validation.

These tests validate release metadata before publishing.
"""

from __future__ import annotations

import zipfile
from pathlib import Path

import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def project_root() -> Path:
    """
    Return repository root.
    """
    return Path(
        __file__,
    ).parents[1]


def load_project_metadata() -> dict:
    """
    Load pyproject metadata.
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


def find_wheel(
    directory: Path,
) -> Path:
    """
    Locate wheel artifact.
    """
    return next(
        directory.glob(
            "*.whl",
        ),
    )


def test_project_has_metadata() -> None:
    """
    Project should define package metadata.
    """
    data = load_project_metadata()

    assert (
        "project"
        in data
    )


def test_package_name_exists() -> None:
    """
    Package name should be defined.
    """
    data = load_project_metadata()

    project = data["project"]

    assert project.get(
        "name",
    )


def test_package_version_exists() -> None:
    """
    Package version should be defined.
    """
    data = load_project_metadata()

    project = data["project"]

    assert project.get(
        "version",
    )


def test_wheel_contains_metadata(
    tmp_path: Path,
) -> None:
    """
    Wheel should contain dist-info metadata.
    """
    import subprocess
    import sys

    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            str(tmp_path),
        ],
        cwd=project_root(),
        check=True,
    )

    wheel = find_wheel(
        tmp_path,
    )

    with zipfile.ZipFile(
        wheel,
    ) as archive:

        files = archive.namelist()

    metadata_files = [
        item
        for item in files
        if ".dist-info/METADATA"
        in item
    ]

    assert len(
        metadata_files,
    ) == 1


def test_wheel_is_valid_archive(
    tmp_path: Path,
) -> None:
    """
    Wheel should be a readable archive.
    """
    import subprocess
    import sys

    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            str(tmp_path),
        ],
        cwd=project_root(),
        check=True,
    )

    wheel = find_wheel(
        tmp_path,
    )

    assert zipfile.is_zipfile(
        wheel,
  )

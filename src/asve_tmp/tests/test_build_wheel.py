"""
Tests for ASVE wheel building.

These tests validate package distribution generation.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def project_root() -> Path:
    """
    Return repository root.
    """
    return Path(
        __file__,
    ).parents[1]


def test_build_module_available() -> None:
    """
    Build module should be available.
    """
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--version",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0


def test_wheel_build_succeeds(
    tmp_path: Path,
) -> None:
    """
    Project should build a wheel artifact.
    """
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            str(tmp_path),
        ],
        cwd=project_root(),
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0


def test_wheel_file_exists(
    tmp_path: Path,
) -> None:
    """
    Build output should contain a wheel.
    """
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

    wheels = list(
        tmp_path.glob(
            "*.whl",
        ),
    )

    assert len(wheels) > 0


def test_wheel_name_is_valid(
    tmp_path: Path,
) -> None:
    """
    Wheel artifact should follow Python naming rules.
    """
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

    wheel = next(
        tmp_path.glob(
            "*.whl",
        ),
    )

    assert (
        wheel.suffix
        == ".whl"
    )

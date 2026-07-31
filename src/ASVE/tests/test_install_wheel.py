"""
Tests for clean wheel installation.

These tests simulate a real user installation.
"""

from __future__ import annotations

import subprocess
import sys
import venv
from pathlib import Path


def create_virtual_environment(
    path: Path,
) -> Path:
    """
    Create isolated Python environment.
    """
    venv.create(
        path,
        with_pip=True,
    )

    if sys.platform == "win32":
        return (
            path
            / "Scripts"
            / "python.exe"
        )

    return (
        path
        / "bin"
        / "python"
    )


def build_wheel(
    root: Path,
    output: Path,
) -> None:
    """
    Build wheel artifact.
    """
    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            str(output),
        ],
        cwd=root,
        check=True,
    )


def test_install_wheel_in_clean_environment(
    tmp_path: Path,
) -> None:
    """
    Wheel should install in a fresh environment.
    """
    root = Path(
        __file__,
    ).parents[1]

    dist = (
        tmp_path
        / "dist"
    )

    dist.mkdir()

    build_wheel(
        root,
        dist,
    )

    python = create_virtual_environment(
        tmp_path / "venv",
    )

    wheel = next(
        dist.glob(
            "*.whl",
        ),
    )

    install = subprocess.run(
        [
            str(python),
            "-m",
            "pip",
            "install",
            str(wheel),
        ],
        capture_output=True,
        text=True,
    )

    assert install.returncode == 0


def test_installed_package_imports(
    tmp_path: Path,
) -> None:
    """
    Installed ASVE should import.
    """
    root = Path(
        __file__,
    ).parents[1]

    dist = (
        tmp_path
        / "dist"
    )

    dist.mkdir()

    build_wheel(
        root,
        dist,
    )

    python = create_virtual_environment(
        tmp_path / "venv",
    )

    wheel = next(
        dist.glob(
            "*.whl",
        ),
    )

    subprocess.run(
        [
            str(python),
            "-m",
            "pip",
            "install",
            str(wheel),
        ],
        check=True,
    )

    result = subprocess.run(
        [
            str(python),
            "-c",
            "import asve",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

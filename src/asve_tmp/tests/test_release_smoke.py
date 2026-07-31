"""
Release smoke tests for ASVE.

These tests validate the package after building
and installing distribution artifacts.
"""

from __future__ import annotations

import subprocess
import sys


def test_package_import_after_install() -> None:
    """
    Installed package should import correctly.
    """
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import asve; print(asve.__version__)",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

    assert result.stdout.strip()


def test_cli_available_after_install() -> None:
    """
    ASVE CLI entry point should work.
    """
    result = subprocess.run(
        [
            "asve",
            "--help",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

    assert (
        "help"
        in result.stdout.lower()
        or "usage"
        in result.stdout.lower()
    )


def test_version_command_works() -> None:
    """
    Installed version should be accessible.
    """
    result = subprocess.run(
        [
            "asve",
            "--version",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0


def test_package_metadata_exists() -> None:
    """
    Distribution metadata should be installed.
    """
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "show",
            "asve",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

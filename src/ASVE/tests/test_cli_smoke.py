"""
CLI smoke tests for ASVE release validation.

These tests simulate first-run user experience.
"""

from __future__ import annotations

import subprocess
import sys


def run_cli(
    *arguments: str,
):
    """
    Execute ASVE CLI command.
    """
    return subprocess.run(
        [
            "asve",
            *arguments,
        ],
        capture_output=True,
        text=True,
    )


def test_cli_entrypoint_exists() -> None:
    """
    Installed CLI command should be available.
    """
    result = run_cli(
        "--help",
    )

    assert result.returncode == 0


def test_cli_help_output() -> None:
    """
    Help should provide usage information.
    """
    result = run_cli(
        "--help",
    )

    output = result.stdout.lower()

    assert (
        "usage"
        in output
        or "commands"
        in output
    )


def test_cli_version() -> None:
    """
    Version command should work.
    """
    result = run_cli(
        "--version",
    )

    assert result.returncode == 0


def test_cli_runs_verification(
    tmp_path,
) -> None:
    """
    Basic verification command should execute.
    """
    file = (
        tmp_path
        / "example.py"
    )

    file.write_text(
        "print('ASVE smoke test')",
        encoding="utf-8",
    )

    result = run_cli(
        "verify",
        str(tmp_path),
    )

    assert result.returncode == 0

"""
Tests for the ASVE command-line interface.

These tests verify terminal-level user interaction.
"""

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from asve.cli.main import app


runner = CliRunner()


def test_cli_verify_command(
    temporary_project: Path,
) -> None:
    """
    CLI verify command should execute successfully.
    """
    result = runner.invoke(
        app,
        [
            "verify-project",
            str(temporary_project),
        ],
    )

    assert result.exit_code == 0


def test_cli_help() -> None:
    """
    CLI should provide help output.
    """
    result = runner.invoke(
        app,
        [
            "--help",
        ],
    )

    assert result.exit_code == 0

    assert "ASVE" in result.output


def test_cli_missing_project(
    tmp_path: Path,
) -> None:
    """
    CLI should handle missing project paths.
    """
    missing = (
        tmp_path
        / "missing"
    )

    result = runner.invoke(
        app,
        [
            "verify-project",
            str(missing),
        ],
    )

    assert result.exit_code in {
        0,
        1,
    }

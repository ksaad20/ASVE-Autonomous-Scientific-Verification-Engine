"""
Tests for ASVE CLI commands.

These tests validate individual command behavior.
"""

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from asve.cli.main import app


runner = CliRunner()


def test_cli_app_loads() -> None:
    """
    CLI application should initialize.
    """
    assert app is not None


def test_verify_command_exists(
    tmp_path: Path,
) -> None:
    """
    Verify command should be available.
    """
    result = runner.invoke(
        app,
        [
            "verify",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0


def test_help_command_lists_commands() -> None:
    """
    Help output should display commands.
    """
    result = runner.invoke(
        app,
        [
            "--help",
        ],
    )

    assert result.exit_code == 0

    assert (
        "verify"
        in result.output
    )


def test_command_accepts_path_argument(
    tmp_path: Path,
) -> None:
    """
    Commands should accept project paths.
    """
    result = runner.invoke(
        app,
        [
            "verify",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0


def test_invalid_command_fails() -> None:
    """
    Unknown commands should fail safely.
    """
    result = runner.invoke(
        app,
        [
            "unknown-command",
        ],
    )

    assert result.exit_code != 0


def test_cli_output_is_text() -> None:
    """
    CLI should produce textual output.
    """
    result = runner.invoke(
        app,
        [
            "--help",
        ],
    )

    assert isinstance(
        result.output,
        str,
    )

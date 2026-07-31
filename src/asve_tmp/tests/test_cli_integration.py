"""
Tests for ASVE CLI integration.

These tests validate the user-facing command interface.
"""

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from asve.cli.main import app


runner = CliRunner()


def test_cli_help() -> None:
    """
    CLI should expose help information.
    """
    result = runner.invoke(
        app,
        [
            "--help",
        ],
    )

    assert result.exit_code == 0

    assert (
        "ASVE"
        in result.output
    )


def test_cli_verify_command(
    tmp_path: Path,
) -> None:
    """
    Verify command should analyze a project.
    """
    result = runner.invoke(
        app,
        [
            "verify",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0


def test_cli_verify_with_artifact(
    tmp_path: Path,
) -> None:
    """
    CLI should process project files.
    """
    file = (
        tmp_path
        / "analysis.py"
    )

    file.write_text(
        "print('experiment')",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "verify",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0


def test_cli_invalid_path() -> None:
    """
    Invalid paths should return failure.
    """
    result = runner.invoke(
        app,
        [
            "verify",
            "/invalid/path/asve",
        ],
    )

    assert result.exit_code != 0

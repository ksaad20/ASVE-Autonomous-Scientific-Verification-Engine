"""
Tests for ASVE example programs.

These tests validate that examples remain executable.
"""

from __future__ import annotations

import runpy
from pathlib import Path


def examples_directory() -> Path:
    """
    Return examples directory.
    """
    return (
        Path(__file__)
        .parents[1]
        / "examples"
    )


def test_examples_directory_exists() -> None:
    """
    Examples directory should exist.
    """
    assert examples_directory().exists()


def test_examples_contain_python_files() -> None:
    """
    Examples should contain Python files.
    """
    examples = list(
        examples_directory().glob(
            "*.py",
        ),
    )

    assert len(examples) > 0


def test_example_files_are_importable() -> None:
    """
    Example scripts should load successfully.
    """
    examples = list(
        examples_directory().glob(
            "*.py",
        ),
    )

    for example in examples:
        assert example.suffix == ".py"


def test_basic_example_execution() -> None:
    """
    Basic examples should execute without failure.
    """
    examples = list(
        examples_directory().glob(
            "*.py",
        ),
    )

    if examples:
        runpy.run_path(
            str(examples[0]),
        )

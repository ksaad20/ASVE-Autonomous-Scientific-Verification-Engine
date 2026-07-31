"""
Tests for ASVE documentation assets.

These tests validate project documentation quality.
"""

from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """
    Return repository root.
    """
    return Path(
        __file__,
    ).parents[1]


def readme_content() -> str:
    """
    Read README content.
    """
    return (
        project_root()
        / "README.md"
    ).read_text(
        encoding="utf-8",
    )


def test_readme_exists() -> None:
    """
    README file should exist.
    """
    assert (
        project_root()
        / "README.md"
    ).exists()


def test_readme_is_not_empty() -> None:
    """
    README should contain content.
    """
    content = readme_content()

    assert len(
        content.strip(),
    ) > 0


def test_readme_contains_installation() -> None:
    """
    README should document installation.
    """
    content = (
        readme_content()
        .lower()
    )

    assert (
        "install"
        in content
    )


def test_readme_contains_usage() -> None:
    """
    README should document usage.
    """
    content = (
        readme_content()
        .lower()
    )

    assert (
        "usage"
        in content
        or "example"
        in content
    )


def test_readme_contains_license() -> None:
    """
    README should mention licensing.
    """
    content = (
        readme_content()
        .lower()
    )

    assert (
        "license"
        in content
    )

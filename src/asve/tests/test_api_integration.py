from __future__ import annotations

import pytest
import pathlib

from pathlib import Path
from asve.api import verify
from asve.core.config import ASVEConfig
from asve.verification.report import VerificationReport


def test_verify_api_returns_report(
    tmp_path: Path,
) -> None:
    """
    Public verify API should return a report.
    """
    report = verify(
        tmp_path,
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_verify_api_with_source_file(
    tmp_path: Path,
) -> None:
    """
    API should analyze project artifacts.
    """
    source = (
        tmp_path
        / "experiment.py"
    )

    source.write_text(
        "value = 42",
        encoding="utf-8",
    )

    report = verify(
        tmp_path,
    )

    assert report is not None


def test_verify_accepts_configuration(
    tmp_path: Path,
) -> None:
    """
    API should accept custom configuration.
    """
    config = ASVEConfig(
        strict_mode=True,
    )

    report = verify(
        tmp_path,
        config=config,
    )

    assert isinstance(
        report,
        VerificationReport,
    )


def test_verify_invalid_path_fails() -> None:
    """
    Invalid project paths should raise errors.
    """
    with pytest.raises(FileNotFoundError):
        verify(
            Path(
                "/invalid/asve/project/path",
            ),
        )

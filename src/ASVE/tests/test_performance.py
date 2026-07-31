"""
Tests for ASVE performance behavior.

These tests validate scalability characteristics.
"""

from __future__ import annotations

import time
from pathlib import Path

from asve.api import verify


def create_test_project(
    path: Path,
    count: int = 50,
) -> None:
    """
    Create a synthetic project.
    """
    for index in range(count):
        file = (
            path
            / f"module_{index}.py"
        )

        file.write_text(
            f"value = {index}",
            encoding="utf-8",
        )


def test_pipeline_handles_many_files(
    tmp_path: Path,
) -> None:
    """
    Pipeline should process many artifacts.
    """
    create_test_project(
        tmp_path,
        count=50,
    )

    report = verify(
        tmp_path,
    )

    assert report is not None


def test_execution_completes_in_reasonable_time(
    tmp_path: Path,
) -> None:
    """
    Basic performance regression check.
    """
    create_test_project(
        tmp_path,
        count=25,
    )

    start = time.perf_counter()

    verify(
        tmp_path,
    )

    duration = (
        time.perf_counter()
        - start
    )

    assert duration < 30


def test_repeated_execution_is_stable(
    tmp_path: Path,
) -> None:
    """
    Repeated runs should remain consistent.
    """
    create_test_project(
        tmp_path,
        count=10,
    )

    first = verify(
        tmp_path,
    )

    second = verify(
        tmp_path,
    )

    assert (
        first.total_findings
        ==
        second.total_findings
    )

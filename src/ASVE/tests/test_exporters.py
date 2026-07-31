"""
Tests for ASVE exporters.

These tests validate report output generation.
"""

from __future__ import annotations

import json
from pathlib import Path

from asve.exporters.json_exporter import JSONExporter
from asve.exporters.text_exporter import TextExporter
from asve.verification.report import VerificationReport


def test_json_exporter_initializes() -> None:
    """
    JSON exporter should initialize.
    """
    exporter = JSONExporter()

    assert exporter is not None


def test_text_exporter_initializes() -> None:
    """
    Text exporter should initialize.
    """
    exporter = TextExporter()

    assert exporter is not None


def test_json_export_creates_output(
    tmp_path: Path,
) -> None:
    """
    JSON exporter should write valid JSON.
    """
    report = VerificationReport()

    output = (
        tmp_path
        / "report.json"
    )

    exporter = JSONExporter()

    exporter.export(
        report,
        output,
    )

    assert output.exists()

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        ),
    )

    assert isinstance(
        data,
        dict,
    )


def test_text_export_creates_output(
    tmp_path: Path,
) -> None:
    """
    Text exporter should write readable output.
    """
    report = VerificationReport()

    output = (
        tmp_path
        / "report.txt"
    )

    exporter = TextExporter()

    exporter.export(
        report,
        output,
    )

    assert output.exists()

    content = output.read_text(
        encoding="utf-8",
    )

    assert len(content) > 0


def test_export_is_repeatable(
    tmp_path: Path,
) -> None:
    """
    Same report should produce stable output.
    """
    report = VerificationReport()

    first = (
        tmp_path
        / "first.json"
    )

    second = (
        tmp_path
        / "second.json"
    )

    exporter = JSONExporter()

    exporter.export(
        report,
        first,
    )

    exporter.export(
        report,
        second,
    )

    assert (
        first.read_text(
            encoding="utf-8",
        )
        ==
        second.read_text(
            encoding="utf-8",
        )
    )

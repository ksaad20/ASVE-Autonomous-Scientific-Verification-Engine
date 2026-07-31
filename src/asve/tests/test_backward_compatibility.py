"""
Tests for ASVE backward compatibility.

These tests validate stability across versions.
"""

from __future__ import annotations

import json

from asve.api import verify
from asve.serialization.json import serialize_json


def test_public_api_remains_available() -> None:
    """
    Public API should remain importable.
    """
    assert callable(
        verify,
    )


def test_current_serialization_is_loadable() -> None:
    """
    Current serialized output should remain valid.
    """
    from asve.verification.report import VerificationReport

    report = VerificationReport()

    data = serialize_json(
        report,
    )

    parsed = json.loads(
        data,
    )

    assert isinstance(
        parsed,
        dict,
    )


def test_empty_project_compatibility(
    tmp_path,
) -> None:
    """
    Empty projects should remain supported.
    """
    report = verify(
        tmp_path,
    )

    assert report is not None


def test_repeated_api_usage_is_stable(
    tmp_path,
) -> None:
    """
    Existing workflows should remain predictable.
    """
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


def test_serialized_schema_has_structure() -> None:
    """
    Serialized objects should retain structure.
    """
    from asve.verification.report import VerificationReport

    report = VerificationReport()

    data = json.loads(
        serialize_json(
            report,
        ),
    )

    assert isinstance(
        data,
        dict,
    )

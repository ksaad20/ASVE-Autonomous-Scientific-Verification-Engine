"""
Tests for the ASVE exception hierarchy.

These tests verify structured error handling.
"""

from __future__ import annotations

import pytest

from asve.core.exceptions import ASVEError
from asve.core.exceptions import ArtifactError
from asve.core.exceptions import ConfigurationError
from asve.core.exceptions import ExtractionError
from asve.core.exceptions import GraphError
from asve.core.exceptions import ParserError
from asve.core.exceptions import ProjectError
from asve.core.exceptions import VerificationError


@pytest.mark.parametrize(
    "exception_type",
    [
        ConfigurationError,
        ProjectError,
        ArtifactError,
        ParserError,
        ExtractionError,
        GraphError,
        VerificationError,
    ],
)
def test_specialized_errors_inherit_from_asve_error(
    exception_type,
) -> None:
    """
    All ASVE exceptions should inherit from ASVEError.
    """
    assert issubclass(
        exception_type,
        ASVEError,
    )


def test_asve_error_can_be_caught() -> None:
    """
    Base ASVEError should catch specialized errors.
    """
    with pytest.raises(ASVEError):
        raise ParserError(
            "Parsing failed",
        )


def test_exception_messages_are_preserved() -> None:
    """
    Exceptions should preserve useful messages.
    """
    error = VerificationError(
        "Verification failed",
    )

    assert str(error) == (
        "Verification failed"
    )

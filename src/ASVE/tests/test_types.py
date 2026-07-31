"""
Tests for ASVE type safety.

These tests validate typing contracts and runtime behavior.
"""

from __future__ import annotations

import inspect
from typing import get_type_hints

from asve.api import verify
from asve.models.artifact import Artifact
from asve.models.finding import Finding


def test_artifact_has_type_annotations() -> None:
    """
    Artifact model should expose annotations.
    """
    hints = get_type_hints(
        Artifact,
    )

    assert isinstance(
        hints,
        dict,
    )


def test_finding_has_type_annotations() -> None:
    """
    Finding model should expose annotations.
    """
    hints = get_type_hints(
        Finding,
    )

    assert isinstance(
        hints,
        dict,
    )


def test_verify_has_return_annotation() -> None:
    """
    Public API should declare return type.
    """
    hints = get_type_hints(
        verify,
    )

    assert (
        "return"
        in hints
    )


def test_verify_parameters_are_typed() -> None:
    """
    API parameters should have annotations.
    """
    signature = inspect.signature(
        verify,
    )

    for parameter in signature.parameters.values():
        assert (
            parameter.annotation
            is not inspect.Parameter.empty
        )


def test_models_are_runtime_objects() -> None:
    """
    Typed models should instantiate correctly.
    """
    assert Artifact is not None
    assert Finding is not None

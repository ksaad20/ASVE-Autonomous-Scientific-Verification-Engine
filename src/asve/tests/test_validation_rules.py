"""
Tests for ASVE validation rule engine.

These tests validate analysis rules and findings.
"""

from __future__ import annotations

from pathlib import Path

from asve.rules.engine import RuleEngine
from asve.rules.base import Rule


class ExampleRule(Rule):
    """
    Minimal validation rule.
    """

    name = "example_rule"

    severity = "medium"

    def evaluate(
        self,
        artifact,
    ) -> bool:
        """
        Evaluate artifact.
        """
        return True


def create_artifact(
    path: Path,
) -> Path:
    """
    Create sample artifact.
    """
    file = (
        path
        / "sample.py"
    )

    file.write_text(
        "x = 1",
        encoding="utf-8",
    )

    return file


def test_rule_engine_initializes() -> None:
    """
    Rule engine should initialize.
    """
    engine = RuleEngine()

    assert engine is not None


def test_rule_registration() -> None:
    """
    Rules should register successfully.
    """
    engine = RuleEngine()

    rule = ExampleRule()

    engine.register(
        rule,
    )

    assert (
        engine.get(
            "example_rule",
        )
        is rule
    )


def test_rule_execution(
    tmp_path: Path,
) -> None:
    """
    Registered rules should execute.
    """
    artifact = create_artifact(
        tmp_path,
    )

    engine = RuleEngine()

    engine.register(
        ExampleRule(),
    )

    results = engine.evaluate(
        artifact,
    )

    assert results is not None


def test_rule_generates_severity() -> None:
    """
    Rules should define severity.
    """
    rule = ExampleRule()

    assert (
        rule.severity
        == "medium"
    )


def test_multiple_runs_are_consistent(
    tmp_path: Path,
) -> None:
    """
    Rule evaluation should be deterministic.
    """
    artifact = create_artifact(
        tmp_path,
    )

    engine = RuleEngine()

    engine.register(
        ExampleRule(),
    )

    first = engine.evaluate(
        artifact,
    )

    second = engine.evaluate(
        artifact,
    )

    assert first == second

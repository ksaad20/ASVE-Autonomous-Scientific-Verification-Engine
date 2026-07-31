"""
Tests for ASVE verification rules.

These tests validate rule registration and execution behavior.
"""

from __future__ import annotations

from asve.rules.base import BaseRule
from asve.rules.registry import RuleRegistry


class DummyRule(BaseRule):
    """
    Minimal verification rule for testing.
    """

    name = "dummy_rule"

    severity = "warning"

    def check(
        self,
        context,
    ) -> list:
        """
        Return a test finding.
        """
        return [
            {
                "rule": self.name,
                "message": "Test finding",
            },
        ]


def test_rule_registry_registers_rule() -> None:
    """
    Registry should store rules.
    """
    registry = RuleRegistry()

    registry.register(
        DummyRule(),
    )

    assert len(registry) == 1


def test_rule_registry_retrieves_rules() -> None:
    """
    Registry should return registered rules.
    """
    registry = RuleRegistry()

    rule = DummyRule()

    registry.register(
        rule,
    )

    rules = registry.rules()

    assert rule in rules


def test_rule_execution_returns_findings() -> None:
    """
    Rules should produce findings.
    """
    rule = DummyRule()

    findings = rule.check(
        None,
    )

    assert len(findings) == 1

    assert (
        findings[0]["rule"]
        == "dummy_rule"
    )


def test_rule_has_metadata() -> None:
    """
    Rules should expose identification data.
    """
    rule = DummyRule()

    assert rule.name == "dummy_rule"
    assert rule.severity == "warning"

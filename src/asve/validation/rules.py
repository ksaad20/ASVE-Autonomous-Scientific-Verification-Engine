"""Validation rule engine for ASVE.

Manages the registration and execution of reproducibility rules.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


class RuleEngine:
    """Engine for registering and executing validation rules.

    Rules are callables that accept arbitrary context and return
    findings or boolean results.

    Examples
    --------
    >>> engine = RuleEngine()
    >>> engine.register("my_rule", lambda ctx: True)
    >>> engine.run({})
    []

    """

    def __init__(self) -> None:
        """Initialize an empty rule engine."""
        self._rules: dict[str, Callable[[Any], Any]] = {}

    def register(
        self,
        name: str,
        rule: Callable[[Any], Any],
    ) -> None:
        """Register a validation rule.

        Parameters
        ----------
        name : str
            Unique identifier for the rule.
        rule : callable
            Function that accepts context and returns results.

        """
        self._rules[name] = rule

    def run(
        self,
        context: Any,
    ) -> list[Any]:
        """Execute all registered rules against *context*.

        Parameters
        ----------
        context : Any
            Analysis context passed to each rule.

        Returns
        -------
        list
            Aggregated results from all rules.

        """
        results: list[Any] = []
        for rule in self._rules.values():
            result = rule(context)
            if result is not None:
                if isinstance(result, list):
                    results.extend(result)
                else:
                    results.append(result)
        return results

    def __repr__(self) -> str:
        return f"RuleEngine(rules={list(self._rules.keys())!r})"


__all__ = [
    "RuleEngine",
]

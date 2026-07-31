"""
Built-in verification rule registration for ASVE.

This module registers verification rules shipped with the ASVE core
package.

External verification rules should be added through a plugin system
rather than modifying this file.
"""

from __future__ import annotations

from asve.verification.engine import VerificationEngine
from asve.verification.rules.citation import CitationVerificationRule
from asve.verification.rules.dataset import DatasetVerificationRule
from asve.verification.rules.dependency import DependencyVerificationRule
from asve.verification.rules.structure import StructureVerificationRule


def register_builtin_rules(
    engine: VerificationEngine,
) -> None:
    """
    Register ASVE built-in verification rules.

    Parameters
    ----------
    engine
        Verification engine instance.
    """
    rules = (
        DependencyVerificationRule(),
        CitationVerificationRule(),
        DatasetVerificationRule(),
        StructureVerificationRule(),
    )

    for rule in rules:
        engine.register(rule)


__all__ = [
    "register_builtin_rules",
]

"""
Built-in parser registration for ASVE.

This module registers parsers shipped with the ASVE core package.

External plugins should not modify this file. They should register
additional parsers through the ASVE plugin mechanism.
"""

from __future__ import annotations

from asve.parsers.json import JSONParser
from asve.parsers.latex import LatexParser
from asve.parsers.markdown import MarkdownParser
from asve.parsers.notebook import NotebookParser
from asve.parsers.python import PythonParser
from asve.parsers.registry import ParserRegistry
from asve.parsers.toml import TOMLParser
from asve.parsers.yaml import YAMLParser
from asve.parsers.csv import CSVParser


def register_builtin_parsers(
    registry: ParserRegistry,
) -> None:
    """
    Register all ASVE built-in parsers.

    Parameters
    ----------
    registry
        Parser registry instance.
    """
    parsers = (
        MarkdownParser(),
        LatexParser(),
        PythonParser(),
        JSONParser(),
        TOMLParser(),
        YAMLParser(),
        CSVParser(),
        NotebookParser(),
    )

    for parser in parsers:
        registry.register(parser)


__all__ = [
    "register_builtin_parsers",
]

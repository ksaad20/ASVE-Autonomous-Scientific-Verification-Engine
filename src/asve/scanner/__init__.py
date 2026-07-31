"""
ASVE artifact discovery subsystem.

The scanner package discovers scientific artifacts inside research
projects and prepares them for parsing and dependency extraction.

Supported artifact types will include:

- source code
- manuscripts
- datasets
- configuration files
- notebooks
- supplementary materials
"""

from __future__ import annotations

from asve.scanner.scanner import ArtifactScanner

__all__ = [
    "ArtifactScanner",
]

"""
ASVE core application layer.

The core package provides high-level orchestration interfaces that
connect scanning, parsing, extraction, graph construction, and
verification into a unified workflow.
"""

from __future__ import annotations

from asve.core.pipeline import ASVEPipeline

__all__ = [
    "ASVEPipeline",
    "AnalysisContext",
     "load_config"
]

"""
ASVE analysis context models.

This module provides the runtime state container shared between
pipeline components during a reproducibility analysis run.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve.graph.graph import ScientificGraph
from asve.models.artifact import Artifact
from asve.models.finding import Finding


class AnalysisContext(BaseModel):
    """
    Runtime context for an ASVE analysis session.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    project_path: Path = Field(
        description="Root project directory.",
    )

    artifacts: list[Artifact] = Field(
        default_factory=list,
        description="Discovered scientific artifacts.",
    )

    graph: ScientificGraph = Field(
        default_factory=ScientificGraph,
        description="Scientific dependency graph.",
    )

    findings: list[Finding] = Field(
        default_factory=list,
        description="Generated verification findings.",
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Analysis metadata.",
    )

    def add_artifact(
        self,
        artifact: Artifact,
    ) -> None:
        """
        Register a discovered artifact.
        """
        self.artifacts.append(artifact)

    def add_finding(
        self,
        finding: Finding,
    ) -> None:
        """
        Register a verification finding.
        """
        self.findings.append(finding)


ASVEContext = AnalysisContext

__all__ = [
    "AnalysisContext",
    "ASVEContext",
]

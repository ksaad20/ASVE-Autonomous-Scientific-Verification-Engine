"""
Configuration models for ASVE.

This module defines the configuration schema used throughout the
Automated Scientific Verification Engine (ASVE).

Configuration objects are immutable, strictly typed, and validated using
Pydantic to ensure consistent behavior across all ASVE components.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ProjectConfig(BaseModel):
    """Project metadata."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    name: str = Field(
        default="Untitled Project",
        description="Human-readable project name.",
    )

    root: Path = Field(
        default=Path.cwd(),
        description="Project root directory.",
    )


class VerificationConfig(BaseModel):
    """Verification module configuration."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    document: bool = True
    software: bool = True
    datasets: bool = True
    references: bool = True
    graph: bool = True


class ReportingConfig(BaseModel):
    """Reporting configuration."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    markdown: bool = True
    json: bool = True
    html: bool = False

    output_directory: Path = Field(
        default=Path("asve-report"),
    )


class RuntimeConfig(BaseModel):
    """Runtime execution settings."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    parallel: bool = True
    workers: int = 4

    profile: Literal[
        "minimal",
        "default",
        "publication",
    ] = "default"


class ASVEConfig(BaseModel):
    """
    Top-level ASVE configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    project: ProjectConfig = ProjectConfig()

    verification: VerificationConfig = (
        VerificationConfig()
    )

    reporting: ReportingConfig = (
        ReportingConfig()
    )

    runtime: RuntimeConfig = (
        RuntimeConfig()
    )


DEFAULT_CONFIG = ASVEConfig()

__all__ = [
    "ProjectConfig",
    "VerificationConfig",
    "ReportingConfig",
    "RuntimeConfig",
    "ASVEConfig",
    "DEFAULT_CONFIG",
]

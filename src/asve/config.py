"""
Configuration models for ASVE.

This module defines validated configuration objects used throughout
the Automated Scientific Verification Engine (ASVE).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import ValidationError

from asve.exceptions import ConfigurationError


class ProjectConfig(BaseModel):
    """Project metadata."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    name: str = "Untitled Project"
    root: Path = Field(
        default_factory=Path.cwd,
    )


class VerificationConfig(BaseModel):
    """Verification settings."""

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
    """Reporting settings."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    markdown: bool = True
    json: bool = True
    html: bool = False
    output_directory: Path = Path("asve-report")


class RuntimeConfig(BaseModel):
    """Runtime settings."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    parallel: bool = True
    workers: int = Field(
        default=4,
        ge=1,
    )

    profile: Literal[
        "minimal",
        "default",
        "publication",
    ] = "default"


@dataclass(frozen=True)
class ASVEConfig:
    """
    Top-level ASVE configuration.

    Invalid configuration raises ConfigurationError.
    """

    project: ProjectConfig = ProjectConfig()
    verification: VerificationConfig = VerificationConfig()
    reporting: ReportingConfig = ReportingConfig()
    runtime: RuntimeConfig = RuntimeConfig()
    strict_mode: bool = False

    def __init__(
        self,
        project: ProjectConfig = ProjectConfig(),
        verification: VerificationConfig = VerificationConfig(),
        reporting: ReportingConfig = ReportingConfig(),
        runtime: RuntimeConfig = RuntimeConfig(),
        strict_mode: object = False,
    ) -> None:
        if not isinstance(strict_mode, bool):
            raise ConfigurationError(
                "strict_mode must be a boolean value."
            )

        object.__setattr__(
            self,
            "project",
            project,
        )

        object.__setattr__(
            self,
            "verification",
            verification,
        )

        object.__setattr__(
            self,
            "reporting",
            reporting,
        )

        object.__setattr__(
            self,
            "runtime",
            runtime,
        )

        object.__setattr__(
            self,
            "strict_mode",
            strict_mode,
        )


DEFAULT_CONFIG = ASVEConfig()


__all__ = [
    "ASVEConfig",
    "DEFAULT_CONFIG",
    "ProjectConfig",
    "ReportingConfig",
    "RuntimeConfig",
    "VerificationConfig",
]

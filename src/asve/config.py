"""
Configuration models for ASVE.

This module defines the configuration schema used throughout the
Automated Scientific Verification Engine (ASVE).

Configuration objects are immutable, strictly typed, and validated to
ensure consistent behavior across all ASVE components.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from asve.exceptions import ConfigurationError


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
        default_factory=Path.cwd,
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
        description="Directory where reports are generated.",
    )


class RuntimeConfig(BaseModel):
    """Runtime execution settings."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    parallel: bool = True

    workers: int = Field(
        default=4,
        ge=1,
        description="Number of worker processes.",
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

    Configuration validation is performed during initialization.
    """

    project: ProjectConfig = field(
        default_factory=ProjectConfig,
    )

    verification: VerificationConfig = field(
        default_factory=VerificationConfig,
    )

    reporting: ReportingConfig = field(
        default_factory=ReportingConfig,
    )

    runtime: RuntimeConfig = field(
        default_factory=RuntimeConfig,
    )

    strict_mode: bool = False

    def __init__(
        self,
        project: ProjectConfig | None = None,
        verification: VerificationConfig | None = None,
        reporting: ReportingConfig | None = None,
        runtime: RuntimeConfig | None = None,
        strict_mode: object = False,
    ) -> None:
        """
        Create validated ASVE configuration.

        Raises:
            ConfigurationError:
                If configuration values are invalid.
        """

        if not isinstance(strict_mode, bool):
            raise ConfigurationError(
                "strict_mode must be a boolean value."
            )

        object.__setattr__(
            self,
            "project",
            (
                project
                if project is not None
                else ProjectConfig()
            ),
        )

        object.__setattr__(
            self,
            "verification",
            (
                verification
                if verification is not None
                else VerificationConfig()
            ),
        )

        object.__setattr__(
            self,
            "reporting",
            (
                reporting
                if reporting is not None
                else ReportingConfig()
            ),
        )

        object.__setattr__(
            self,
            "runtime",
            (
                runtime
                if runtime is not None
                else RuntimeConfig()
            ),
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

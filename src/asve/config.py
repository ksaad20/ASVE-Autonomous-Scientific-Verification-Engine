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

from asve.exceptions import ConfigurationError


class ProjectConfig(BaseModel):
    """Project metadata."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    name: str = Field(
        default="Untitled Project",
    )

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

    workers: int = Field(
        default=4,
        ge=1,
    )

    profile: Literal[
        "minimal",
        "default",
        "publication",
    ] = "default"


class ASVEConfig(BaseModel):
    """
    Top-level ASVE configuration.

    Use ASVEConfig.create() when loading user-provided configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    project: ProjectConfig = Field(
        default_factory=ProjectConfig,
    )

    verification: VerificationConfig = Field(
        default_factory=VerificationConfig,
    )

    reporting: ReportingConfig = Field(
        default_factory=ReportingConfig,
    )

    runtime: RuntimeConfig = Field(
        default_factory=RuntimeConfig,
    )

    strict_mode: bool = False

    @classmethod
    def create(
        cls,
        *,
        strict_mode: object = False,
        **kwargs: object,
    ) -> "ASVEConfig":
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

        return cls(
            strict_mode=strict_mode,
            **kwargs,
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

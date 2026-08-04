"""
Configuration models for ASVE.

This module defines the configuration schema used throughout the
Automated Scientific Verification Engine (ASVE).

Configuration objects are immutable, strictly typed, and validated using
Pydantic to ensure consistent behavior across all ASVE components.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any
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


class ASVEConfig(BaseModel):
    """
    Top-level ASVE configuration.
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

    strict_mode: bool = Field(
        default=False,
        description="Enable strict verification behavior.",
    )

    def __init__(self, **data: Any) -> None:
        """
        Validate configuration and expose ASVE-specific errors.
        """

        strict_mode = data.get("strict_mode")

        if isinstance(strict_mode, str):
            if strict_mode.lower() == "true":
                data["strict_mode"] = True

            elif strict_mode.lower() == "false":
                data["strict_mode"] = False

            else:
                raise ConfigurationError(
                    "strict_mode must be a boolean value."
                )

        try:
            super().__init__(**data)

        except ValidationError as exc:
            raise ConfigurationError(
                f"Invalid ASVE configuration: {exc}"
            ) from exc


DEFAULT_CONFIG = ASVEConfig()


__all__ = [
    "ASVEConfig",
    "DEFAULT_CONFIG",
    "ProjectConfig",
    "ReportingConfig",
    "RuntimeConfig",
    "VerificationConfig",
]

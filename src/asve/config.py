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
from pydantic_core import core_schema

from asve.exceptions import ConfigurationError


class StrictBool:
    """
    Strict boolean configuration type.

    Converts valid boolean values while raising ASVE-specific
    configuration errors for invalid input.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: object,
        handler: object,
    ) -> core_schema.CoreSchema:
        """
        Define Pydantic validation schema.
        """

        def validate(value: object) -> bool:
            if isinstance(value, bool):
                return value

            if isinstance(value, str):
                normalized = value.lower()

                if normalized == "true":
                    return True

                if normalized == "false":
                    return False

            raise ConfigurationError(
                "strict_mode must be a boolean value."
            )

        return core_schema.no_info_plain_validator_function(
            validate,
        )


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

    strict_mode: StrictBool = Field(
        default=False,
        description="Enable strict verification behavior.",
    )


DEFAULT_CONFIG = ASVEConfig()


__all__ = [
    "ASVEConfig",
    "DEFAULT_CONFIG",
    "ProjectConfig",
    "ReportingConfig",
    "RuntimeConfig",
    "StrictBool",
    "VerificationConfig",
]

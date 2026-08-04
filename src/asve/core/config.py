"""
ASVE configuration models.

This module defines user-configurable settings controlling analysis
behavior.

Future versions will support loading configuration from:
- asve.toml
- asve.yaml
- project metadata files
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import model_validator

from asve.exceptions import ConfigurationError


class ASVEConfig(BaseModel):
    """
    Global ASVE analysis configuration.
    """

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    enabled_parsers: tuple[str, ...] = Field(
        default=(),
        description=(
            "Parser identifiers enabled "
            "during analysis."
        ),
    )

    enabled_extractors: tuple[str, ...] = Field(
        default=(),
        description=(
            "Extractor identifiers enabled "
            "during analysis."
        ),
    )

    enabled_rules: tuple[str, ...] = Field(
        default=(),
        description=(
            "Verification rules enabled "
            "during analysis."
        ),
    )

    ignored_paths: tuple[str, ...] = Field(
        default=(
            ".git",
            ".venv",
            "__pycache__",
        ),
        description=(
            "Paths ignored during scanning."
        ),
    )

    include_hidden: bool = Field(
        default=False,
        description=(
            "Whether hidden files should be scanned."
        ),
    )

    strict_mode: bool = Field(
        default=False,
        description=(
            "Enable strict reproducibility checks."
        ),
    )

    @model_validator(mode="before")
    @classmethod
    def validate_strict_mode(
        cls,
        values: object,
    ) -> object:
        """
        Validate strict mode before Pydantic coercion.
        """

        if isinstance(values, dict):
            strict_mode = values.get(
                "strict_mode",
                False,
            )

            if not isinstance(strict_mode, bool):
                raise ConfigurationError(
                    "strict_mode must be a boolean value."
                )

        return values


__all__ = [
    "ASVEConfig",
]

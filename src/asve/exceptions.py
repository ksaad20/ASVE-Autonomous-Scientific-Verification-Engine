"""
Custom exceptions for ASVE.

This module defines the exception hierarchy used throughout the
Automated Scientific Verification Engine (ASVE).

All project-specific exceptions inherit from ``ASVEError``.
Modules should raise these exceptions rather than built-in exceptions
where appropriate, allowing applications to catch a single base class
when handling ASVE-specific failures.
"""

from __future__ import annotations

from typing import Final

__all__ = [
    "ASVEError",
    "ConfigurationError",
    "ProjectNotFoundError",
    "ArtifactError",
    "ArtifactNotFoundError",
    "ParserError",
    "VerificationError",
    "RuleError",
    "PluginError",
    "ReportError",
    "GraphError",
]


class ASVEError(Exception):
    """Base class for all ASVE-specific exceptions."""


class ConfigurationError(ASVEError):
    """Raised when a project configuration is invalid or cannot be loaded."""


class ProjectNotFoundError(ASVEError):
    """Raised when an ASVE project cannot be located."""


class ArtifactError(ASVEError):
    """Base class for artifact-related exceptions."""


class ArtifactNotFoundError(ArtifactError):
    """Raised when a required research artifact is missing."""


class ParserError(ASVEError):
    """Raised when an artifact cannot be parsed successfully."""


class VerificationError(ASVEError):
    """Raised when scientific verification cannot be completed."""


class RuleError(VerificationError):
    """Raised when a verification rule fails or is invalid."""


class PluginError(ASVEError):
    """Raised when a plugin cannot be loaded or executed."""


class ReportError(ASVEError):
    """Raised when report generation fails."""


class GraphError(ASVEError):
    """Raised when the scientific dependency graph is invalid."""


DEFAULT_EXCEPTION_MESSAGE: Final[str] = (
    "An unexpected ASVE error has occurred."
)

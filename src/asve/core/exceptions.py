"""
ASVE exception hierarchy.

This module defines controlled exceptions raised throughout the ASVE
analysis pipeline.

All ASVE-specific exceptions inherit from ASVEError so applications
can catch failures at different levels.
"""

from __future__ import annotations


class ASVEError(Exception):
    """
    Base exception for all ASVE errors.
    """


class ConfigurationError(ASVEError):
    """
    Raised when ASVE configuration is invalid.
    """


class ProjectError(ASVEError):
    """
    Raised when a project cannot be analyzed.
    """


class ArtifactError(ASVEError):
    """
    Raised when artifact discovery or processing fails.
    """


class ParserError(ASVEError):
    """
    Raised when parsing fails.
    """


class ExtractionError(ASVEError):
    """
    Raised when dependency extraction fails.
    """


class GraphError(ASVEError):
    """
    Raised when scientific graph construction fails.
    """


class VerificationError(ASVEError):
    """
    Raised when verification execution fails.
    """


__all__ = [
    "ASVEError",
    "ArtifactError",
    "ConfigurationError",
    "ExtractionError",
    "GraphError",
    "ParserError",
    "ProjectError",
    "VerificationError",
]

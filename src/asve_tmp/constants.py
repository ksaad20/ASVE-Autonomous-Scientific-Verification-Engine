"""
Global constants for ASVE.

This module centralizes immutable project-wide constants used throughout
the ASVE codebase. Keeping constants in one location improves
maintainability, consistency, and type safety.
"""

from __future__ import annotations

from typing import Final

###############################################################################
# Project Metadata
###############################################################################

PROJECT_NAME: Final[str] = "ASVE"
PROJECT_SLUG: Final[str] = "asve"
PROJECT_FULL_NAME: Final[str] = "Automated Scientific Verification Engine"

###############################################################################
# Default Configuration
###############################################################################

DEFAULT_CONFIG_FILE: Final[str] = "asve.yaml"
DEFAULT_REPORT_DIRECTORY: Final[str] = "asve-report"
DEFAULT_REPORT_NAME: Final[str] = "verification-report"

###############################################################################
# Supported Manuscript Formats
###############################################################################

SUPPORTED_DOCUMENT_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".md",
        ".rst",
        ".tex",
        ".txt",
    }
)

###############################################################################
# Supported Dataset Formats
###############################################################################

SUPPORTED_DATASET_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".csv",
        ".tsv",
        ".json",
        ".jsonl",
        ".xlsx",
        ".parquet",
    }
)

###############################################################################
# Supported Notebook Formats
###############################################################################

SUPPORTED_NOTEBOOK_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".ipynb",
    }
)

###############################################################################
# Supported Source Code Formats
###############################################################################

SUPPORTED_SOURCE_EXTENSIONS: Final[frozenset[str]] = frozenset(
    {
        ".py",
        ".R",
        ".jl",
        ".m",
    }
)

###############################################################################
# Report Formats
###############################################################################

SUPPORTED_REPORT_FORMATS: Final[frozenset[str]] = frozenset(
    {
        "markdown",
        "json",
        "html",
    }
)

###############################################################################
# Exit Codes
###############################################################################

EXIT_SUCCESS: Final[int] = 0
EXIT_WARNING: Final[int] = 1
EXIT_ERROR: Final[int] = 2

###############################################################################
# Severity Levels
###############################################################################

SEVERITY_INFO: Final[str] = "info"
SEVERITY_RECOMMENDATION: Final[str] = "recommendation"
SEVERITY_WARNING: Final[str] = "warning"
SEVERITY_ERROR: Final[str] = "error"
SEVERITY_CRITICAL: Final[str] = "critical"

SEVERITY_LEVELS: Final[tuple[str, ...]] = (
    SEVERITY_INFO,
    SEVERITY_RECOMMENDATION,
    SEVERITY_WARNING,
    SEVERITY_ERROR,
    SEVERITY_CRITICAL,
)

###############################################################################
# Default Encoding
###############################################################################

DEFAULT_ENCODING: Final[str] = "utf-8"

###############################################################################
# Public API
###############################################################################

__all__ = [
    "PROJECT_NAME",
    "PROJECT_SLUG",
    "PROJECT_FULL_NAME",
    "DEFAULT_CONFIG_FILE",
    "DEFAULT_REPORT_DIRECTORY",
    "DEFAULT_REPORT_NAME",
    "SUPPORTED_DOCUMENT_EXTENSIONS",
    "SUPPORTED_DATASET_EXTENSIONS",
    "SUPPORTED_NOTEBOOK_EXTENSIONS",
    "SUPPORTED_SOURCE_EXTENSIONS",
    "SUPPORTED_REPORT_FORMATS",
    "EXIT_SUCCESS",
    "EXIT_WARNING",
    "EXIT_ERROR",
    "SEVERITY_INFO",
    "SEVERITY_RECOMMENDATION",
    "SEVERITY_WARNING",
    "SEVERITY_ERROR",
    "SEVERITY_CRITICAL",
    "SEVERITY_LEVELS",
    "DEFAULT_ENCODING",
]

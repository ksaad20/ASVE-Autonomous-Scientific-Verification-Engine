"""
ASVE
====

Automated Scientific Verification Engine.

ASVE is an open-source scientific verification platform for improving
the transparency, consistency, and reproducibility of computational
research.

The package provides tools for automated verification of scientific
artifacts including manuscripts, datasets, software, mathematical
models, statistical analyses, and their relationships.

Example
-------
>>> import asve
>>> print(asve.__version__)
"""

from __future__ import annotations

from asve.version import (
    __version__,
    version_info,
    get_version,
)

__all__: list[str] = [
    "__version__",
    "version_info",
    "get_version",
]

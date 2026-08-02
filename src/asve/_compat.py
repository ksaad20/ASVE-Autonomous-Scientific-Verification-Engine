"""Compatibility shims for older Python versions.

Centralizes backports so the rest of the codebase can import
modern APIs without version checks everywhere.
"""

import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from enum import Enum

    class StrEnum(str, Enum):  # type: ignore[no-redef]
        """Backport of :class:`enum.StrEnum` for Python < 3.11.

        Members are automatically coerced to strings when used in
        string contexts.

        """

        def __str__(self) -> str:
            return self.value

        def __repr__(self) -> str:
            return self.value


__all__ = ["StrEnum"]

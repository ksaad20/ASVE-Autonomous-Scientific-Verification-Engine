"""JSON exporter for ASVE verification reports.

Serializes structured report data to portable JSON files.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from asve.verification.report import VerificationReport


class JSONExporter:
    """Export :class:`VerificationReport` instances to JSON.

    Examples
    --------
    >>> exporter = JSONExporter()
    >>> exporter.export(report, Path("out.json"))

    """

    def export(
        self,
        report: VerificationReport,
        output_path: str | Path,
    ) -> None:
        """Serialize *report* to JSON and write it to *output_path*.

        Parameters
        ----------
        report : VerificationReport
            The report to export.
        output_path : str or pathlib.Path
            Destination file path.

        """
        payload: dict[str, Any] = {
            "total_findings": report.total_findings,
            "findings": [
                f.model_dump() if hasattr(f, "model_dump") else str(f)
                for f in report.findings
            ],
        }
        Path(output_path).write_text(
            json.dumps(payload, indent=2, default=str),
            encoding="utf-8",
        )


__all__ = [
    "JSONExporter",
]

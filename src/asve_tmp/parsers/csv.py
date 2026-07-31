"""
CSV parser for ASVE.

This module implements parsing support for CSV datasets.

The parser validates CSV structure using Python's standard library and
delegates artifact creation to StructuredDataParser.
"""

from __future__ import annotations

import csv
from pathlib import Path

from asve.exceptions import ParserError
from asve.parsers.structured import StructuredDataParser


class CSVParser(StructuredDataParser):
    """
    Parser for CSV datasets.
    """

    @property
    def name(self) -> str:
        """
        Return the parser name.
        """
        return "csv"

    @property
    def supported_extensions(self) -> frozenset[str]:
        """
        Return supported filename extensions.
        """
        return frozenset(
            {
                ".csv",
            }
        )

    def parse_content(self, path: Path) -> None:
        """
        Validate a CSV document.

        Parameters
        ----------
        path
            Path to the CSV file.

        Raises
        ------
        ParserError
            If the CSV file cannot be read or is structurally invalid.
        """
        try:
            with path.open(
                mode="r",
                encoding="utf-8",
                newline="",
            ) as stream:
                sample = stream.read(4096)
                stream.seek(0)

                try:
                    dialect = csv.Sniffer().sniff(sample)
                except csv.Error:
                    dialect = csv.excel

                reader = csv.reader(
                    stream,
                    dialect=dialect,
                )

                expected_columns: int | None = None

                for row_number, row in enumerate(reader, start=1):
                    if expected_columns is None:
                        expected_columns = len(row)
                        continue

                    if len(row) != expected_columns:
                        raise ParserError(
                            "Inconsistent number of columns "
                            f"at row {row_number}."
                        )

        except OSError as exc:
            raise ParserError(
                f"Unable to read CSV file '{path}'."
            ) from exc


__all__ = [
    "CSVParser",
]

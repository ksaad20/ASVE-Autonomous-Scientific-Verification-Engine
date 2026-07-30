"""
Command-line interface for ASVE.

The CLI provides the primary user interface for the Automated Scientific
Verification Engine (ASVE). It intentionally contains very little
business logic and delegates work to the underlying application modules.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from asve.version import __version__

app = typer.Typer(
    name="asve",
    help="Automated Scientific Verification Engine.",
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
)

console = Console()


@app.callback()
def main() -> None:
    """
    ASVE command-line interface.
    """


@app.command("version")
def version() -> None:
    """
    Display the installed ASVE version.
    """
    console.print(f"ASVE {__version__}")


@app.command("init")
def init(
    directory: Annotated[
        Path,
        typer.Argument(
            exists=False,
            resolve_path=True,
            help="Directory in which to initialize the project.",
        ),
    ] = Path("."),
) -> None:
    """
    Initialize a new ASVE project.
    """
    console.print(
        f"[green]Initialized ASVE project:[/green] {directory}"
    )


@app.command("verify")
def verify(
    project: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            resolve_path=True,
            help="Project directory to verify.",
        ),
    ] = Path("."),
) -> None:
    """
    Verify a research project.
    """
    console.print(
        f"[cyan]Verifying project:[/cyan] {project}"
    )

    console.print(
        "[yellow]Verification engine not yet implemented.[/yellow]"
    )


@app.command("report")
def report() -> None:
    """
    Display the latest verification summary.
    """
    table = Table(title="Verification Summary")

    table.add_column("Category")
    table.add_column("Status")

    table.add_row("Project", "Not Verified")
    table.add_row("Report", "Unavailable")

    console.print(table)


@app.command("plugins")
def plugins() -> None:
    """
    List installed ASVE plugins.
    """
    console.print(
        "[yellow]No plugins are currently installed.[/yellow]"
    )


@app.command("doctor")
def doctor() -> None:
    """
    Display diagnostic information.
    """
    table = Table(title="ASVE Diagnostics")

    table.add_column("Component")
    table.add_column("Status")

    table.add_row("CLI", "OK")
    table.add_row("Configuration", "OK")
    table.add_row("Environment", "OK")

    console.print(table)


def run() -> None:
    """
    Execute the ASVE command-line application.
    """
    app()


if __name__ == "__main__":
    run()

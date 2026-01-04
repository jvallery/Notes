#!/usr/bin/env python3
"""
Schema validation utilities for Notes Vault.

Validates extraction and changeplan JSON files against schemas.
"""

import json
import sys
from pathlib import Path
from typing import Optional

import click
import jsonschema
from rich.console import Console
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root, workflow_root


console = Console()


def load_schema(schema_name: str) -> dict:
    """Load a JSON schema by name."""

    schema_path = workflow_root() / "schemas" / f"{schema_name}.schema.json"

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")

    with open(schema_path, "r") as f:
        return json.load(f)


def validate_file(file_path: Path, schema: dict) -> tuple[bool, list[str]]:
    """Validate a JSON file against a schema."""

    errors = []

    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        jsonschema.validate(data, schema)
        return True, []

    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e.msg} at line {e.lineno}")
        return False, errors

    except jsonschema.ValidationError as e:
        errors.append(f"Schema violation: {e.message}")
        if e.path:
            errors.append(f"  Path: {'.'.join(str(p) for p in e.path)}")
        return False, errors

    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def find_json_files(pattern: str = "*.json") -> list[Path]:
    """Find JSON files in the extraction directory."""

    extraction_dir = vault_root() / "Inbox" / "_extraction"

    if not extraction_dir.exists():
        return []

    return list(extraction_dir.glob(pattern))


@click.command()
@click.option(
    "--file",
    "-f",
    "single_file",
    type=click.Path(exists=True),
    help="Validate a single file",
)
@click.option(
    "--type",
    "-t",
    "file_type",
    type=click.Choice(["extraction", "changeplan", "all"]),
    default="all",
    help="Type of files to validate",
)
@click.option("--fix", is_flag=True, help="Attempt to fix simple issues")
def main(single_file: Optional[str], file_type: str, fix: bool):
    """Validate JSON files against schemas."""

    console.print("[bold blue]Schema Validation[/bold blue]")
    console.print("=" * 40)

    # Load schemas
    schemas = {}

    if file_type in ["extraction", "all"]:
        try:
            schemas["extraction"] = load_schema("extraction")
        except FileNotFoundError as e:
            console.print(f"[yellow]Warning: {e}[/yellow]")

    if file_type in ["changeplan", "all"]:
        try:
            schemas["changeplan"] = load_schema("changeplan")
        except FileNotFoundError as e:
            console.print(f"[yellow]Warning: {e}[/yellow]")

    if not schemas:
        console.print("[red]No schemas found to validate against.[/red]")
        return

    # Find files to validate
    if single_file:
        files = [Path(single_file)]
    else:
        files = []
        if "extraction" in schemas:
            files.extend(find_json_files("*.extraction.json"))
        if "changeplan" in schemas:
            files.extend(find_json_files("*.changeplan.json"))

    if not files:
        console.print("[yellow]No files found to validate.[/yellow]")
        return

    console.print(f"Found [bold]{len(files)}[/bold] files to validate\n")

    # Validate files
    results = {"valid": [], "invalid": []}

    table = Table(title="Validation Results")
    table.add_column("File", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Issues", style="red")

    for file in sorted(files):
        # Determine schema to use
        if ".extraction.json" in file.name:
            schema = schemas.get("extraction")
            schema_type = "extraction"
        elif ".changeplan.json" in file.name:
            schema = schemas.get("changeplan")
            schema_type = "changeplan"
        else:
            schema = None
            schema_type = "unknown"

        if not schema:
            table.add_row(
                file.name, "[yellow]Skipped[/yellow]", f"No {schema_type} schema"
            )
            continue

        is_valid, errors = validate_file(file, schema)

        if is_valid:
            results["valid"].append(str(file))
            table.add_row(file.name, "[green]✓ Valid[/green]", "")
        else:
            results["invalid"].append({"file": str(file), "errors": errors})
            table.add_row(
                file.name,
                "[red]✗ Invalid[/red]",
                "\n".join(errors[:2]),  # Show first 2 errors
            )

    console.print(table)

    # Summary
    console.print("\n" + "=" * 40)
    console.print(f"[green]Valid: {len(results['valid'])}[/green]")
    console.print(f"[red]Invalid: {len(results['invalid'])}[/red]")

    # Exit with error if any invalid
    if results["invalid"]:
        sys.exit(1)


if __name__ == "__main__":
    main()

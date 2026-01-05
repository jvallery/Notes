#!/usr/bin/env python3
"""
Plan Phase: Extraction JSON → ChangePlan JSON

Reads extraction files and generates explicit file operation plans.
Uses OpenAI API to determine what changes to make to the vault.

NO FILE MODIFICATIONS HAPPEN HERE - only planning.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
import jsonschema
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    load_config,
    get_model_config,
    vault_root,
    workflow_root,
    list_entity_folders,
    load_aliases,
    resolve_mentions,
)


def get_glossary_context() -> str:
    """Load the people/projects/customers glossary for prompt context."""
    try:
        from utils.cached_prompts import get_glossary_context as _get_glossary
        return _get_glossary(compact=True)  # Compact for planning
    except ImportError:
        return ""


console = Console()


def get_openai_client() -> OpenAI:
    """Get configured OpenAI client."""
    import os
    from dotenv import load_dotenv

    load_dotenv(workflow_root() / ".env")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment")

    return OpenAI(api_key=api_key)


def get_jinja_env() -> Environment:
    """Get Jinja2 environment for prompts."""
    return Environment(
        loader=FileSystemLoader(workflow_root() / "prompts"),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def load_changeplan_schema() -> dict:
    """Load the ChangePlan JSON schema for validation."""
    schema_path = workflow_root() / "schemas" / "changeplan.schema.json"

    with open(schema_path, "r") as f:
        return json.load(f)


def find_pending_extractions() -> list[Path]:
    """Find extraction files that don't have corresponding changeplans."""

    extraction_dir = vault_root() / "Inbox" / "_extraction"

    if not extraction_dir.exists():
        return []

    pending = []

    for extraction_file in extraction_dir.glob("*.extraction.json"):
        changeplan_file = extraction_file.with_name(
            extraction_file.name.replace(".extraction.json", ".changeplan.json")
        )

        if not changeplan_file.exists():
            pending.append(extraction_file)

    return sorted(pending, key=lambda p: p.name)


def build_vault_context() -> dict:
    """Build context about existing vault structure for the planner."""

    return {
        "entities": list_entity_folders(),
        "aliases": load_aliases(),
        "templates_available": [
            "people.md.j2",
            "customer.md.j2",
            "projects.md.j2",
            "rob.md.j2",
            "journal.md.j2",
        ],
    }


def generate_changeplan(
    extraction: dict, client: OpenAI, jinja_env: Environment
) -> dict:
    """Generate a ChangePlan from an extraction."""

    model_config = get_model_config("planning")

    # Build vault context
    vault_context = build_vault_context()

    # Build system prompt
    template = jinja_env.get_template("system-planner.md.j2")
    tomorrow = (datetime.now() + __import__('datetime').timedelta(days=1)).strftime("%Y-%m-%d")
    next_week = (datetime.now() + __import__('datetime').timedelta(days=7)).strftime("%Y-%m-%d")
    
    # Get glossary context for entity resolution
    glossary = get_glossary_context()
    
    system_prompt_template = template.render(
        current_date=datetime.now().strftime("%Y-%m-%d"),
        tomorrow=tomorrow,
        next_week=next_week,
        entity_folders=vault_context.get("entities", {}),
        aliases=vault_context.get("aliases", {}),
        known_entities=vault_context.get("entities", {}),
        extraction=extraction,
    )
    
    # Build final system prompt with glossary first (for prompt caching)
    if glossary:
        system_prompt = f"""## ENTITY GLOSSARY
{glossary}

{system_prompt_template}"""
    else:
        system_prompt = system_prompt_template

    # Resolve entity mentions
    classification = extraction.get("classification", {})
    extracted = extraction.get("extraction", {})
    mentions = classification.get("entities", {})

    resolved_entities = resolve_mentions(mentions) if mentions else {}

    user_prompt = json.dumps(
        {
            "source_file": extraction.get("source_file"),
            "classification": classification,
            "extraction": extracted,
            "resolved_entities": resolved_entities,
        },
        indent=2,
    )

    try:
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=model_config["temperature"],
        )

        changeplan = json.loads(response.choices[0].message.content)

        # Add metadata
        changeplan["version"] = "1.0"
        changeplan["source"] = {
            "file": extraction.get("source_file"),
            "extraction": extraction.get("source_file", "")
            .replace("Inbox/", "Inbox/_extraction/")
            .replace(".md", ".extraction.json"),
            "processed_at": datetime.now().isoformat(),
        }

        return changeplan

    except Exception as e:
        console.print(f"[red]Planning failed: {e}[/red]")
        return {
            "version": "1.0",
            "source": {"file": extraction.get("source_file")},
            "operations": [],
            "validation": {
                "schema_valid": False,
                "conflicts": [],
                "warnings": [f"Planning failed: {str(e)}"],
            },
        }


def validate_changeplan(changeplan: dict) -> tuple[bool, list[str]]:
    """Validate a changeplan against the JSON schema."""

    schema = load_changeplan_schema()
    errors = []

    try:
        jsonschema.validate(changeplan, schema)
        return True, []
    except jsonschema.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def save_changeplan(extraction_file: Path, changeplan: dict) -> Path:
    """Save changeplan to JSON file."""

    # Validate before saving
    is_valid, errors = validate_changeplan(changeplan)

    changeplan["validation"] = changeplan.get("validation", {})
    changeplan["validation"]["schema_valid"] = is_valid

    if errors:
        changeplan["validation"]["warnings"] = (
            changeplan["validation"].get("warnings", []) + errors
        )

    output_path = extraction_file.with_name(
        extraction_file.name.replace(".extraction.json", ".changeplan.json")
    )

    with open(output_path, "w") as f:
        json.dump(changeplan, f, indent=2, ensure_ascii=False)

    return output_path


@click.command()
@click.option(
    "--file",
    "-f",
    "single_file",
    type=click.Path(exists=True),
    help="Process a single extraction file",
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be planned without saving"
)
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
def main(single_file: Optional[str], dry_run: bool, verbose: bool):
    """Generate ChangePlans from extraction files."""

    console.print("[bold blue]Plan Phase[/bold blue]")
    console.print("=" * 40)

    # Find files to process
    if single_file:
        files = [Path(single_file)]
    else:
        files = find_pending_extractions()

    if not files:
        console.print("[yellow]No pending extractions found.[/yellow]")
        return

    console.print(f"Found [bold]{len(files)}[/bold] extractions to plan")

    # Initialize clients
    client = get_openai_client()
    jinja_env = get_jinja_env()

    # Process files
    results = {"success": [], "failed": []}

    for file in files:
        try:
            if verbose:
                console.print(f"\n[dim]Planning: {file.name}[/dim]")

            # Load extraction
            with open(file, "r") as f:
                extraction = json.load(f)

            # Generate plan
            changeplan = generate_changeplan(extraction, client, jinja_env)

            if verbose:
                op_count = len(changeplan.get("operations", []))
                console.print(f"  Generated {op_count} operations")

            if dry_run:
                console.print(json.dumps(changeplan, indent=2))
                continue

            # Save plan
            output_path = save_changeplan(file, changeplan)
            results["success"].append(str(output_path))

            if verbose:
                valid = changeplan.get("validation", {}).get("schema_valid", False)
                status = "[green]✓[/green]" if valid else "[yellow]⚠[/yellow]"
                console.print(f"  {status} → {output_path.name}")

        except Exception as e:
            results["failed"].append({"file": str(file), "error": str(e)})
            console.print(f"[red]Failed: {file.name} - {e}[/red]")

    # Summary
    if not dry_run:
        console.print("\n" + "=" * 40)
        console.print(f"[green]Success: {len(results['success'])}[/green]")
        console.print(f"[red]Failed: {len(results['failed'])}[/red]")


if __name__ == "__main__":
    main()

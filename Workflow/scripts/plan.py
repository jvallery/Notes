#!/usr/bin/env python3
"""
Plan Phase: ExtractionV1 → ChangePlan JSON

Reads extraction files and generates explicit file operation plans.
Uses OpenAI Structured Outputs for schema-enforced planning.

NO FILE MODIFICATIONS HAPPEN HERE - only planning.
LLM generates create/patch/link operations only.
Archive is handled deterministically in apply phase.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).parent.parent))

from models.extraction import ExtractionV1
from models.changeplan import ChangePlan
from scripts.utils import (
    load_config,
    vault_root,
    workflow_root,
    list_all_entity_names,
    list_entity_paths,
    get_entity_metadata,
    load_aliases,
    safe_read_text,
    atomic_write,
    get_client,
    parse_structured,
    check_api_key,
    OpenAIError,
    validate_changeplan,
)


def find_unplanned() -> list[Path]:
    """Find extractions without corresponding .changeplan.json."""
    extraction_dir = vault_root() / "Inbox" / "_extraction"

    if not extraction_dir.exists():
        return []

    unplanned = []
    for f in extraction_dir.glob("*.extraction.json"):
        changeplan_path = f.parent / f.name.replace(".extraction.json", ".changeplan.json")
        if not changeplan_path.exists():
            unplanned.append(f)

    return sorted(unplanned)


def load_extraction(path: Path) -> ExtractionV1:
    """Load extraction JSON from file."""
    content = safe_read_text(path)
    return ExtractionV1.model_validate_json(content)


def gather_vault_context(extraction: ExtractionV1) -> dict:
    """
    Build FILTERED context for the planner.

    CRITICAL: Only includes:
    1. Full metadata for entities mentioned in extraction
    2. Lightweight name-only list for fuzzy matching
    3. Entity name-to-path mapping for correct file paths
    4. Entity name and note type from extraction

    This prevents context window explosion.
    """
    # Collect mentioned entity names
    mentioned = set(extraction.participants)
    
    # Add entities from mentions
    if extraction.mentions:
        for entity_list in [extraction.mentions.people, extraction.mentions.projects, extraction.mentions.accounts]:
            if entity_list:
                mentioned.update(entity_list)
    
    if extraction.entity_name:
        mentioned.add(extraction.entity_name)

    return {
        "mentioned_entities": get_entity_metadata(mentioned),
        "all_entity_names": list_all_entity_names(),
        "entity_paths": list_entity_paths(),  # Name → full path mapping
        "note_type": extraction.note_type,
        "entity_name": extraction.entity_name,
    }


def build_planner_prompt(vault_context: dict, extraction: ExtractionV1) -> str:
    """Build the planner system prompt using Jinja2 template."""
    from datetime import date, timedelta
    from jinja2 import Environment, FileSystemLoader

    prompts_dir = workflow_root() / "prompts"
    env = Environment(
        loader=FileSystemLoader(str(prompts_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Ensure tojson filter exists
    env.filters["tojson"] = lambda v, **kw: json.dumps(v, ensure_ascii=False, **kw)

    template = env.get_template("system-planner.md.j2")
    
    # Calculate date context for base template
    today = date.today()
    
    # Load aliases for entity resolution
    aliases = load_aliases()
    
    # Build template context with all required variables
    return template.render(
        # Base template variables
        current_date=today.isoformat(),
        tomorrow=(today + timedelta(days=1)).isoformat(),
        next_week=(today + timedelta(days=7)).isoformat(),
        known_entities=vault_context["all_entity_names"],
        # Planner-specific variables
        entity_folders=vault_context["all_entity_names"],
        entity_paths=vault_context.get("entity_paths", {}),
        aliases=aliases,
        extraction=extraction.model_dump(mode="json"),
    )


# validate_changeplan is imported from scripts.utils.validation


def generate_plan(extraction_path: Path, client, config) -> tuple[ChangePlan, dict]:
    """Generate ChangePlan from extraction using OpenAI Structured Outputs."""
    extraction = load_extraction(extraction_path)
    vault_context = gather_vault_context(extraction)

    system_prompt = build_planner_prompt(vault_context, extraction)

    # Get planning model config
    models_config = config.get("models", {})
    model_config = models_config.get("planning", {})
    model = model_config.get("model", "gpt-4o")
    temperature = model_config.get("temperature", 0.1)

    plan, metadata = parse_structured(
        client=client,
        model=model,
        system_prompt=system_prompt,
        user_content="Generate the ChangePlan for this extraction.",
        response_model=ChangePlan,
        temperature=temperature,
    )

    # Set source references
    plan.extraction_file = str(extraction_path.name)
    plan.source_file = extraction.source_file
    plan.created_at = datetime.now()

    # Validate
    issues = validate_changeplan(plan)
    if issues:
        plan.warnings.extend(issues)

    return plan, metadata


def save_plan(plan: ChangePlan, output_path: Path) -> None:
    """Save ChangePlan JSON to disk."""
    json_str = plan.model_dump_json(indent=2)
    atomic_write(output_path, json_str)


@click.command()
@click.option(
    "--extraction",
    "extraction_path",
    type=click.Path(exists=True),
    help="Plan from single extraction file",
)
@click.option("--all", "plan_all", is_flag=True, help="Plan all pending extractions")
@click.option("--dry-run", is_flag=True, help="Show what would be planned without saving")
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output")
def main(extraction_path: str | None, plan_all: bool, dry_run: bool, verbose: bool):
    """Generate ChangePlans from extraction files."""
    
    click.echo(click.style("Plan Phase", fg="blue", bold=True))
    click.echo("=" * 40)

    # Find files to process
    if extraction_path:
        files = [Path(extraction_path)]
    elif plan_all:
        files = find_unplanned()
    else:
        click.echo("Specify --extraction or --all")
        return

    if not files:
        click.echo(click.style("No pending extractions found.", fg="yellow"))
        return

    click.echo(f"Found {click.style(str(len(files)), bold=True)} extraction(s) to plan")

    if dry_run:
        for f in files:
            click.echo(f"  Would plan: {f.name}")
        return

    # Check API key only when actually processing
    if not check_api_key():
        click.echo(click.style("Error: OPENAI_API_KEY not set", fg="red"))
        click.echo("Set it with: export OPENAI_API_KEY=sk-...")
        return

    if dry_run:
        for f in files:
            click.echo(f"  Would plan: {f.name}")
        return

    # Load config and initialize client
    config = load_config()
    client = get_client()

    # Process files
    success_count = 0
    failed_count = 0

    for f in files:
        try:
            if verbose:
                click.echo(f"\nPlanning: {f.name}")

            plan, metadata = generate_plan(f, client, config)

            output_path = f.parent / f.name.replace(".extraction.json", ".changeplan.json")
            save_plan(plan, output_path)

            success_count += 1

            # Show summary
            ops_summary = ", ".join(op.op.value for op in plan.operations) if plan.operations else "none"
            latency = metadata.get("latency_ms", "?")
            tokens = metadata.get("total_tokens", "?")

            if verbose:
                click.echo(f"  → {output_path.name}")
                click.echo(f"    Operations: {ops_summary}")
                click.echo(f"    Latency: {latency}ms, Tokens: {tokens}")

                if plan.warnings:
                    for warning in plan.warnings:
                        click.echo(click.style(f"    ⚠ {warning}", fg="yellow"))
            else:
                status = click.style("✓", fg="green") if not plan.warnings else click.style("⚠", fg="yellow")
                click.echo(f"{status} {f.stem} → {len(plan.operations)} ops ({latency}ms)")

        except OpenAIError as e:
            failed_count += 1
            click.echo(click.style(f"✗ {f.name}: {e}", fg="red"))
        except Exception as e:
            failed_count += 1
            click.echo(click.style(f"✗ {f.name}: {e}", fg="red"))
            if verbose:
                import traceback
                traceback.print_exc()

    # Summary
    click.echo("\n" + "=" * 40)
    click.echo(f"{click.style('Success:', fg='green')} {success_count}")
    if failed_count:
        click.echo(f"{click.style('Failed:', fg='red')} {failed_count}")


if __name__ == "__main__":
    main()

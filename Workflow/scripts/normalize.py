#!/usr/bin/env python3
"""
Normalize Phase: Post-extraction entity normalization.

Takes extraction JSON and normalizes entity references:
- Match entity names to canonical forms using aliases
- Validate entity names exist in manifest
- Normalize dates to ISO-8601 format
- Flag unknown entities for review

This runs AFTER extract.py and BEFORE plan.py to ensure
consistent entity references across the vault.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import click
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.utils import vault_root


def load_aliases(config_path: Path | None = None) -> dict[str, str]:
    """Load entity alias mappings from config or entities/aliases.yaml."""
    # Try entities/aliases.yaml first
    aliases_file = vault_root() / "Workflow" / "entities" / "aliases.yaml"
    if aliases_file.exists():
        with open(aliases_file) as f:
            data = yaml.safe_load(f) or {}
            # Flatten to lowercase -> canonical mapping
            result = {}
            for canonical, aliases in data.items():
                result[canonical.lower()] = canonical
                if isinstance(aliases, list):
                    for alias in aliases:
                        result[alias.lower()] = canonical
            return result
    return {}


def load_known_entities(vault: Path) -> dict[str, set[str]]:
    """
    Scan vault for known entity folders.
    
    Returns:
        Dict mapping entity type to set of entity names
        e.g., {"people": {"Jeff Denworth", "Karl Vietmeier"}, ...}
    """
    entities: dict[str, set[str]] = {
        "people": set(),
        "projects": set(),
        "accounts": set(),
    }
    
    # Scan VAST/People and Personal/People
    for people_dir in [vault / "VAST" / "People", vault / "Personal" / "People"]:
        if people_dir.exists():
            for folder in people_dir.iterdir():
                if folder.is_dir() and not folder.name.startswith("."):
                    entities["people"].add(folder.name)
    
    # Scan projects
    for projects_dir in [vault / "VAST" / "Projects", vault / "Personal" / "Projects"]:
        if projects_dir.exists():
            for folder in projects_dir.iterdir():
                if folder.is_dir() and not folder.name.startswith("."):
                    entities["projects"].add(folder.name)
    
    # Scan customers/accounts
    accounts_dir = vault / "VAST" / "Customers and Partners"
    if accounts_dir.exists():
        for folder in accounts_dir.iterdir():
            if folder.is_dir() and not folder.name.startswith("."):
                entities["accounts"].add(folder.name)
    
    return entities


def normalize_entity_name(
    name: str,
    entity_type: str,
    known_entities: dict[str, set[str]],
    aliases: dict[str, str],
) -> tuple[str, bool]:
    """
    Normalize an entity name to canonical form.
    
    Returns:
        (normalized_name, is_known) tuple
    """
    # Check aliases first
    if name.lower() in aliases:
        canonical = aliases[name.lower()]
        is_known = canonical in known_entities.get(entity_type, set())
        return canonical, is_known
    
    # Check if name exists in known entities (case-insensitive)
    known = known_entities.get(entity_type, set())
    for k in known:
        if k.lower() == name.lower():
            return k, True
    
    # Not found - return as-is with unknown flag
    return name, False


def normalize_date(date_str: str) -> str | None:
    """
    Normalize a date string to ISO-8601 format (YYYY-MM-DD).
    
    Handles common formats:
    - YYYY-MM-DD (already normalized)
    - MM/DD/YYYY
    - Month DD, YYYY
    - DD Month YYYY
    """
    if not date_str:
        return None
    
    # Already ISO format
    if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        return date_str
    
    # Try common formats
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%d %B %Y",
        "%b %d, %Y",
        "%d %b %Y",
    ]
    
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    
    # Return original if can't parse
    return date_str


def normalize_extraction(
    extraction: dict[str, Any],
    vault: Path,
) -> tuple[dict[str, Any], list[str]]:
    """
    Normalize entity references in extraction data.
    
    Returns:
        (normalized_extraction, warnings) tuple
    """
    aliases = load_aliases()
    known = load_known_entities(vault)
    warnings: list[str] = []
    
    # Normalize date
    if extraction.get("date"):
        extraction["date"] = normalize_date(extraction["date"]) or extraction["date"]
    
    # Normalize entity_name
    if extraction.get("entity_name") and extraction.get("note_type"):
        entity_type_map = {
            "people": "people",
            "customer": "accounts",
            "partners": "accounts",
            "projects": "projects",
        }
        entity_type = entity_type_map.get(extraction["note_type"], "people")
        name, is_known = normalize_entity_name(
            extraction["entity_name"], entity_type, known, aliases
        )
        extraction["entity_name"] = name
        if not is_known:
            warnings.append(f"Unknown entity: {name} (type: {entity_type})")
    
    # Normalize mentions
    mentions = extraction.get("mentions", {})
    
    # People mentions
    if mentions.get("people"):
        normalized_people = []
        for person in mentions["people"]:
            name, is_known = normalize_entity_name(person, "people", known, aliases)
            normalized_people.append(name)
            if not is_known:
                warnings.append(f"Unknown person: {name}")
        mentions["people"] = normalized_people
    
    # Project mentions
    if mentions.get("projects"):
        normalized_projects = []
        for project in mentions["projects"]:
            name, is_known = normalize_entity_name(project, "projects", known, aliases)
            normalized_projects.append(name)
            if not is_known:
                warnings.append(f"Unknown project: {name}")
        mentions["projects"] = normalized_projects
    
    # Account mentions
    if mentions.get("accounts"):
        normalized_accounts = []
        for account in mentions["accounts"]:
            name, is_known = normalize_entity_name(account, "accounts", known, aliases)
            normalized_accounts.append(name)
            if not is_known:
                warnings.append(f"Unknown account: {name}")
        mentions["accounts"] = normalized_accounts
    
    extraction["mentions"] = mentions
    
    # Normalize person_details keys
    if extraction.get("person_details"):
        normalized_details = {}
        for name, details in extraction["person_details"].items():
            canonical, _ = normalize_entity_name(name, "people", known, aliases)
            normalized_details[canonical] = details
        extraction["person_details"] = normalized_details
    
    # Normalize project_details keys
    if extraction.get("project_details"):
        normalized_details = {}
        for name, details in extraction["project_details"].items():
            canonical, _ = normalize_entity_name(name, "projects", known, aliases)
            normalized_details[canonical] = details
        extraction["project_details"] = normalized_details
    
    # Normalize account_details keys
    if extraction.get("account_details"):
        normalized_details = {}
        for name, details in extraction["account_details"].items():
            canonical, _ = normalize_entity_name(name, "accounts", known, aliases)
            normalized_details[canonical] = details
        extraction["account_details"] = normalized_details
    
    # Normalize task dates
    for task in extraction.get("tasks", []):
        if task.get("due"):
            task["due"] = normalize_date(task["due"])
    
    # Merge warnings
    existing_warnings = extraction.get("warnings", [])
    extraction["warnings"] = list(set(existing_warnings + warnings))
    
    return extraction, warnings


@click.command()
@click.option(
    "--input", "-i",
    type=click.Path(exists=True, path_type=Path),
    help="Path to extraction JSON file to normalize",
)
@click.option(
    "--output", "-o",
    type=click.Path(path_type=Path),
    help="Output path for normalized JSON (default: overwrite input)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Print changes without writing",
)
@click.option(
    "--all",
    "process_all",
    is_flag=True,
    help="Process all extraction files in Inbox/_extraction/",
)
def main(input: Path | None, output: Path | None, dry_run: bool, process_all: bool):
    """Normalize entity references in extraction JSON."""
    vault = vault_root()
    
    if process_all:
        extraction_dir = vault / "Inbox" / "_extraction"
        files = list(extraction_dir.glob("*.extraction.json"))
        if not files:
            click.echo("No extraction files found.")
            return
        
        for extraction_file in files:
            click.echo(f"Processing: {extraction_file.name}")
            with open(extraction_file) as f:
                data = json.load(f)
            
            normalized, warnings = normalize_extraction(data, vault)
            
            if warnings:
                click.echo(f"  Warnings: {len(warnings)}")
                for w in warnings[:5]:
                    click.echo(f"    - {w}")
                if len(warnings) > 5:
                    click.echo(f"    ... and {len(warnings) - 5} more")
            
            if not dry_run:
                with open(extraction_file, "w") as f:
                    json.dump(normalized, f, indent=2, default=str)
                click.echo(f"  Updated: {extraction_file.name}")
    
    elif input:
        with open(input) as f:
            data = json.load(f)
        
        normalized, warnings = normalize_extraction(data, vault)
        
        if warnings:
            click.echo("Warnings:")
            for w in warnings:
                click.echo(f"  - {w}")
        
        if dry_run:
            click.echo(json.dumps(normalized, indent=2, default=str))
        else:
            out_path = output or input
            with open(out_path, "w") as f:
                json.dump(normalized, f, indent=2, default=str)
            click.echo(f"Wrote normalized extraction to: {out_path}")
    
    else:
        click.echo("Provide --input or --all")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

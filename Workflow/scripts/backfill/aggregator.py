"""
Backfill Aggregator: Build README updates from extractions.

This module takes BackfillExtraction results and aggregates them into
ReadmeUpdate plans for each entity. Key responsibilities:

1. Map extractions to entity READMEs (multi-entity support)
2. Sort and deduplicate context entries
3. Calculate last_contact dates
4. Build Recent Context section content
"""

from datetime import datetime
from pathlib import Path
from collections import defaultdict

from . import (
    BackfillExtraction,
    ExtractionBatch,
    ContextEntry,
    ReadmeUpdate,
    BackfillPlan,
)

from utils.config import vault_root


# ─────────────────────────────────────────────────────────────────────────────
# Entity Matching
# ─────────────────────────────────────────────────────────────────────────────

# Canonical entity folders (relative to vault root)
ENTITY_FOLDERS = {
    "VAST/People": "people",
    "VAST/Customers and Partners": "accounts",
    "VAST/Projects": "projects",
    "VAST/ROB": "rob",
    "Personal/People": "people",
    "Personal/Projects": "projects",
}


def normalize_entity_name(name: str) -> str:
    """Normalize entity name for comparison."""
    return name.lower().strip()


def find_matching_entity(mention: str, entity_map: dict[str, str]) -> str | None:
    """
    Find an entity path matching a mention.
    
    Args:
        mention: Name from extraction (e.g., "Jeff Denworth")
        entity_map: Map of normalized names to entity paths
        
    Returns:
        Entity path if found, None otherwise
    """
    normalized = normalize_entity_name(mention)
    
    # Direct match
    if normalized in entity_map:
        return entity_map[normalized]
    
    # Partial match (first name or last name)
    for norm_name, path in entity_map.items():
        name_parts = norm_name.split()
        mention_parts = normalized.split()
        
        # Check if mention matches any part of the name
        if any(part in name_parts for part in mention_parts):
            return path
    
    return None


def build_entity_map(vault: Path) -> dict[str, dict[str, str]]:
    """
    Build maps of entity names to folder paths.
    
    Returns:
        Dict with keys 'people', 'accounts', 'projects', 'rob'
        Each value is a map of normalized names to folder paths
    """
    entity_maps: dict[str, dict[str, str]] = {
        "people": {},
        "accounts": {},
        "projects": {},
        "rob": {},
    }
    
    for folder_prefix, entity_type in ENTITY_FOLDERS.items():
        folder_path = vault / folder_prefix
        if not folder_path.exists():
            continue
            
        for item in folder_path.iterdir():
            if item.is_dir() and not item.name.startswith(("_", ".")):
                normalized = normalize_entity_name(item.name)
                relative_path = str(item.relative_to(vault))
                entity_maps[entity_type][normalized] = relative_path
    
    return entity_maps


# ─────────────────────────────────────────────────────────────────────────────
# Aggregation Logic
# ─────────────────────────────────────────────────────────────────────────────


def map_extraction_to_entities(
    extraction: BackfillExtraction,
    entity_maps: dict[str, dict[str, str]],
) -> list[tuple[str, str | None]]:
    """
    Map an extraction to all relevant entity paths.
    
    Returns:
        List of (entity_path, via_entity) tuples
        via_entity is None for primary entity, set for cross-references
    """
    results: list[tuple[str, str | None]] = []
    
    # Primary entity (where the note lives)
    primary_entity = extraction.entity_path
    if primary_entity:
        results.append((primary_entity, None))
    
    # Get primary entity name for "via" references
    primary_name = Path(primary_entity).name if primary_entity else None
    
    # Mentioned people
    for person in extraction.mentions.people:
        entity_path = find_matching_entity(person, entity_maps.get("people", {}))
        if entity_path and entity_path != primary_entity:
            results.append((entity_path, primary_name))
    
    # Mentioned accounts
    for account in extraction.mentions.accounts:
        entity_path = find_matching_entity(account, entity_maps.get("accounts", {}))
        if entity_path and entity_path != primary_entity:
            results.append((entity_path, primary_name))
    
    # Mentioned projects
    for project in extraction.mentions.projects:
        entity_path = find_matching_entity(project, entity_maps.get("projects", {}))
        if entity_path and entity_path != primary_entity:
            results.append((entity_path, primary_name))
    
    return results


def create_context_entry(
    extraction: BackfillExtraction,
    via_entity: str | None = None,
) -> ContextEntry:
    """Create a ContextEntry from an extraction."""
    return ContextEntry(
        date=extraction.date,
        title=extraction.title,
        note_path=extraction.note_path,
        summary=extraction.summary[:150] if extraction.summary else "",
        via_entity=via_entity,
    )


def aggregate_extractions(
    extractions: list[BackfillExtraction],
    vault: Path | None = None,
    max_entries_per_readme: int = 15,
) -> BackfillPlan:
    """
    Aggregate extractions into README update plan.
    
    This is the main aggregation function that:
    1. Builds entity maps for matching
    2. Maps each extraction to all relevant entities
    3. Deduplicates and sorts entries
    4. Creates ReadmeUpdate for each entity
    
    Args:
        extractions: List of BackfillExtraction from extract phase
        vault: Path to vault root (uses config default if None)
        max_entries_per_readme: Maximum context entries per README
        
    Returns:
        BackfillPlan with all README updates
    """
    if vault is None:
        vault = vault_root()
    
    # Build entity maps for matching mentions to folders
    entity_maps = build_entity_map(vault)
    
    # Aggregate: entity_path -> list of (extraction, via_entity)
    entity_extractions: dict[str, list[tuple[BackfillExtraction, str | None]]] = defaultdict(list)
    
    for extraction in extractions:
        mappings = map_extraction_to_entities(extraction, entity_maps)
        for entity_path, via_entity in mappings:
            entity_extractions[entity_path].append((extraction, via_entity))
    
    # Build ReadmeUpdate for each entity
    updates: list[ReadmeUpdate] = []
    total_entries = 0
    
    for entity_path, ext_list in entity_extractions.items():
        # Create context entries
        entries: list[ContextEntry] = []
        seen_notes: set[str] = set()
        
        for extraction, via_entity in ext_list:
            # Skip duplicates
            if extraction.note_path in seen_notes:
                continue
            seen_notes.add(extraction.note_path)
            
            entry = create_context_entry(extraction, via_entity)
            entries.append(entry)
        
        # Sort by date descending
        entries.sort(key=lambda e: e.date, reverse=True)
        
        # Limit entries
        entries = entries[:max_entries_per_readme]
        
        # Calculate last_contact from most recent entry
        last_contact = entries[0].date if entries else None
        
        # Build update
        readme_path = f"{entity_path}/README.md"
        update = ReadmeUpdate(
            entity_path=entity_path,
            readme_path=readme_path,
            last_contact=last_contact,
            context_entries=entries,
            interaction_count=len(seen_notes),
        )
        
        updates.append(update)
        total_entries += len(entries)
    
    # Sort updates by entity path for consistent output
    updates.sort(key=lambda u: u.entity_path)
    
    return BackfillPlan(
        version="1.0",
        created_at=datetime.now(),
        scope="vault",
        updates=updates,
        total_entities=len(entity_maps["people"]) + len(entity_maps["accounts"]) + 
                       len(entity_maps["projects"]) + len(entity_maps["rob"]),
        entities_with_updates=len(updates),
        total_context_entries=total_entries,
    )


def format_recent_context_section(entries: list[ContextEntry]) -> str:
    """
    Format context entries as markdown for README.
    
    Output format:
    - 2025-11-14: [[2025-11-14 - GDC Alignment]] - Brief summary
    - 2025-10-30: [[2025-10-30 - Weekly 1-1]] - Another summary (via Google)
    """
    lines: list[str] = []
    
    for entry in entries:
        # Build wikilink - use filename without .md
        note_name = Path(entry.note_path).stem
        wikilink = f"[[{note_name}]]"
        
        # Build line
        line = f"- {entry.date}: {wikilink}"
        
        if entry.summary:
            # Truncate summary if too long
            summary = entry.summary[:100]
            if len(entry.summary) > 100:
                summary += "..."
            line += f" - {summary}"
        
        if entry.via_entity:
            line += f" (via {entry.via_entity})"
        
        lines.append(line)
    
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# CLI Integration
# ─────────────────────────────────────────────────────────────────────────────


def load_extractions(path: Path) -> ExtractionBatch:
    """Load ExtractionBatch from JSON file."""
    import json
    
    with open(path) as f:
        data = json.load(f)
    
    return ExtractionBatch.model_validate(data)


def save_plan(plan: BackfillPlan, path: Path) -> None:
    """Save BackfillPlan to JSON file."""
    import json
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w") as f:
        json.dump(plan.model_dump(mode="json"), f, indent=2, default=str)
    
    print(f"Saved backfill plan to: {path}")


def aggregate_from_file(
    extractions_path: Path,
    output_path: Path | None = None,
    vault: Path | None = None,
) -> BackfillPlan:
    """
    Run aggregation from saved extractions file.
    
    Args:
        extractions_path: Path to ExtractionBatch JSON
        output_path: Where to save BackfillPlan (optional)
        vault: Path to vault root
        
    Returns:
        BackfillPlan
    """
    # Load extractions
    batch = load_extractions(extractions_path)
    print(f"Loaded {len(batch.extractions)} extractions from {extractions_path}")
    
    # Aggregate
    plan = aggregate_extractions(batch.extractions, vault)
    
    print("\nAggregation complete:")
    print(f"  Entities with updates: {plan.entities_with_updates}")
    print(f"  Total context entries: {plan.total_context_entries}")
    
    # Save if output path provided
    if output_path:
        save_plan(plan, output_path)
    
    return plan

"""
Entity Management: Auto-creation, manifest maintenance, and enrichment.

Handles:
- Manifest initialization from existing folder structure
- Bidirectional sync between manifests and folders
- Entity discovery and auto-creation
- Web search enrichment for people/customers
- Status tracking for projects (active/inactive)

Manifest files (_MANIFEST.md) are the source of truth for:
- Known entity names and metadata
- Aliases and alternate names
- Status flags (active/inactive for projects)
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader
from openai import OpenAI


# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

ENTITY_CONFIGS = {
    "people": {
        "folder": "VAST/People",
        "template": "readme-person.md.j2",
        "table_header": "| Name | Role | Company | Status | Context |",
        "table_separator": "|------|------|---------|--------|---------|",
        "columns": ["Name", "Role", "Company", "Status", "Context"],
        "default_status": "active",
    },
    "customers": {
        "folder": "VAST/Customers and Partners",
        "template": "readme-customer.md.j2",
        "table_header": "| Name | Type | Industry | Status | Context |",
        "table_separator": "|------|------|----------|--------|---------|",
        "columns": ["Name", "Type", "Industry", "Status", "Context"],
        "default_status": "active",
    },
    "projects": {
        "folder": "VAST/Projects",
        "template": "readme-project.md.j2",
        "table_header": "| Name | Status | Owner | Description |",
        "table_separator": "|------|--------|-------|-------------|",
        "columns": ["Name", "Status", "Owner", "Description"],
        "default_status": "active",
    },
}

MANIFEST_HEADER = """# Entity Manifest

> **Auto-generated manifest** - Synced with folder structure.
> Edit this file to add aliases, change status, or update metadata.
> Run `backfill.py sync-manifests` to sync with folders.

## Entities

"""


# ─────────────────────────────────────────────────────────────────────────────
# Manifest Parsing
# ─────────────────────────────────────────────────────────────────────────────


def parse_manifest_table(content: str) -> list[dict[str, str]]:
    """
    Parse the entity table from manifest content.
    
    Returns:
        List of dicts with column headers as keys
    """
    lines = content.split("\n")
    headers = []
    rows = []
    in_table = False
    
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            if in_table and rows:
                break  # End of table
            continue
        
        cells = [c.strip() for c in line.split("|")[1:-1]]
        
        # Detect header row (has "Name" column)
        if not in_table and "Name" in cells:
            headers = cells
            in_table = True
            continue
        
        if in_table:
            # Skip separator line
            if all(c.startswith("-") or c.startswith(":") or c == "" for c in cells):
                continue
            
            # Parse data row
            if len(cells) >= len(headers):
                row = {}
                for i, header in enumerate(headers):
                    row[header] = cells[i] if i < len(cells) else ""
                rows.append(row)
    
    return rows


def parse_aliases_section(content: str) -> dict[str, str]:
    """
    Parse the aliases section from manifest.
    
    Format:
    ## Aliases
    - "Nick" → Real Name
    - "Nickname" → Real Name
    
    Returns:
        Dict mapping alias to canonical name
    """
    aliases = {}
    in_aliases = False
    
    for line in content.split("\n"):
        if line.strip().lower().startswith("## aliases"):
            in_aliases = True
            continue
        
        if in_aliases:
            if line.strip().startswith("#"):
                break  # Next section
            
            # Parse alias line: - "alias" → canonical
            match = re.match(r'-\s*["\']?([^"\'→]+)["\']?\s*→\s*(.+)', line.strip())
            if match:
                alias = match.group(1).strip()
                canonical = match.group(2).strip()
                aliases[alias.lower()] = canonical
    
    return aliases


# ─────────────────────────────────────────────────────────────────────────────
# Manifest CRUD Operations
# ─────────────────────────────────────────────────────────────────────────────


def get_manifest_path(vault: Path, entity_type: str) -> Path:
    """Get path to manifest file for entity type."""
    config = ENTITY_CONFIGS.get(entity_type)
    if not config:
        raise ValueError(f"Unknown entity type: {entity_type}")
    return vault / config["folder"] / "_MANIFEST.md"


def create_manifest(vault: Path, entity_type: str) -> Path:
    """
    Create a new manifest file for entity type.
    
    Initializes from existing folder structure.
    """
    config = ENTITY_CONFIGS[entity_type]
    manifest_path = get_manifest_path(vault, entity_type)
    entity_dir = vault / config["folder"]
    
    # Build table from existing folders
    rows = []
    if entity_dir.exists():
        for folder in sorted(entity_dir.iterdir()):
            if folder.is_dir() and not folder.name.startswith(("_", ".")):
                # Try to extract metadata from README
                readme = folder / "README.md"
                metadata = extract_readme_metadata(readme) if readme.exists() else {}
                
                row = {"Name": folder.name}
                for col in config["columns"][1:]:  # Skip Name
                    key = col.lower().replace(" ", "_")
                    row[col] = metadata.get(key, config.get("default_status", "") if col == "Status" else "")
                rows.append(row)
    
    # Generate manifest content
    content = MANIFEST_HEADER
    content += config["table_header"] + "\n"
    content += config["table_separator"] + "\n"
    
    for row in rows:
        cells = [row.get(col, "") for col in config["columns"]]
        content += "| " + " | ".join(cells) + " |\n"
    
    content += "\n## Aliases\n\n_Add nickname mappings here:_\n\n"
    content += "<!-- Example: - \"Nick\" → Full Name -->\n"
    
    # Write manifest
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(content)
    
    return manifest_path


def extract_readme_metadata(readme_path: Path) -> dict[str, str]:
    """Extract metadata from README frontmatter."""
    if not readme_path.exists():
        return {}
    
    content = readme_path.read_text()
    metadata = {}
    
    # Parse YAML frontmatter
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end > 0:
            frontmatter = content[4:end]
            for line in frontmatter.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip().lower().replace(" ", "_")
                    value = value.strip().strip('"\'')
                    metadata[key] = value
    
    return metadata


def get_known_entities(vault: Path) -> dict[str, list[str]]:
    """
    Get lists of known entity names from manifests.
    
    Creates manifests from folder structure if they don't exist.
    
    Returns:
        Dict with keys: people, customers, projects
        Values are lists of canonical names
    """
    known = {"people": [], "customers": [], "projects": []}
    
    for entity_type in ENTITY_CONFIGS.keys():
        manifest_path = get_manifest_path(vault, entity_type)
        
        # Create manifest if missing
        if not manifest_path.exists():
            create_manifest(vault, entity_type)
        
        if manifest_path.exists():
            content = manifest_path.read_text()
            rows = parse_manifest_table(content)
            known[entity_type] = [r.get("Name", "") for r in rows if r.get("Name")]
    
    return known


def get_entity_status(vault: Path, entity_type: str, entity_name: str) -> str:
    """Get status of an entity from manifest."""
    manifest_path = get_manifest_path(vault, entity_type)
    if not manifest_path.exists():
        return "unknown"
    
    content = manifest_path.read_text()
    rows = parse_manifest_table(content)
    
    for row in rows:
        if row.get("Name") == entity_name:
            return row.get("Status", "active")
    
    return "unknown"


def get_active_entities(vault: Path, entity_type: str) -> list[str]:
    """Get list of active entities (excludes inactive/archived)."""
    manifest_path = get_manifest_path(vault, entity_type)
    if not manifest_path.exists():
        return []
    
    content = manifest_path.read_text()
    rows = parse_manifest_table(content)
    
    active = []
    for row in rows:
        name = row.get("Name", "")
        status = row.get("Status", "active").lower()
        if name and status not in ("inactive", "archived", "closed"):
            active.append(name)
    
    return active


def resolve_alias(vault: Path, entity_type: str, name: str) -> str:
    """Resolve an alias to canonical name."""
    manifest_path = get_manifest_path(vault, entity_type)
    if not manifest_path.exists():
        return name
    
    content = manifest_path.read_text()
    aliases = parse_aliases_section(content)
    
    return aliases.get(name.lower(), name)


# ─────────────────────────────────────────────────────────────────────────────
# Manifest Updates
# ─────────────────────────────────────────────────────────────────────────────


def add_to_manifest(
    vault: Path,
    entity_type: str,
    entity_name: str,
    metadata: dict | None = None,
) -> bool:
    """
    Add a new entity to the manifest.
    
    Args:
        vault: Path to vault root
        entity_type: One of: people, customers, projects
        entity_name: Name of entity to add
        metadata: Optional metadata dict
    
    Returns:
        True if added, False if already exists
    """
    config = ENTITY_CONFIGS.get(entity_type)
    if not config:
        return False
    
    manifest_path = get_manifest_path(vault, entity_type)
    
    # Create manifest if it doesn't exist
    if not manifest_path.exists():
        create_manifest(vault, entity_type)
    
    content = manifest_path.read_text()
    
    # Check if already exists
    rows = parse_manifest_table(content)
    if any(r.get("Name") == entity_name for r in rows):
        return False
    
    # Build new row
    metadata = metadata or {}
    row_data = [entity_name]
    for col in config["columns"][1:]:  # Skip Name
        key = col.lower().replace(" ", "_")
        default = config.get("default_status", "") if col == "Status" else ""
        row_data.append(metadata.get(key, default))
    
    new_row = "| " + " | ".join(row_data) + " |"
    
    # Find table end and insert
    lines = content.split("\n")
    new_lines = []
    inserted = False
    in_table = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        
        # Track if we're in the table
        if "| Name |" in line:
            in_table = True
            continue
        
        if in_table and line.strip().startswith("|"):
            # Check if next line is end of table
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if not next_line.startswith("|"):
                new_lines.append(new_row)
                inserted = True
                in_table = False
    
    if not inserted:
        # Append at end of table section
        new_lines.append(new_row)
    
    manifest_path.write_text("\n".join(new_lines))
    return True


def update_entity_status(
    vault: Path,
    entity_type: str,
    entity_name: str,
    new_status: str,
) -> bool:
    """Update the status of an entity in manifest."""
    config = ENTITY_CONFIGS.get(entity_type)
    if not config:
        return False
    
    manifest_path = get_manifest_path(vault, entity_type)
    if not manifest_path.exists():
        return False
    
    content = manifest_path.read_text()
    lines = content.split("\n")
    updated = False
    
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and entity_name in line:
            # Parse and update this row
            cells = [c.strip() for c in line.split("|")[1:-1]]
            headers = config["columns"]
            
            if "Status" in headers and len(cells) >= len(headers):
                status_idx = headers.index("Status")
                cells[status_idx] = new_status
                lines[i] = "| " + " | ".join(cells) + " |"
                updated = True
                break
    
    if updated:
        manifest_path.write_text("\n".join(lines))
    
    return updated


# ─────────────────────────────────────────────────────────────────────────────
# Manifest-Folder Sync
# ─────────────────────────────────────────────────────────────────────────────


def sync_manifests(vault: Path, create_missing_folders: bool = False) -> dict[str, Any]:
    """
    Synchronize manifests with folder structure.
    
    - Adds folders not in manifest to manifest
    - Optionally creates folders for manifest entries without folders
    - Reports orphaned entries
    
    Returns:
        Dict with sync results
    """
    results = {
        "added_to_manifest": {"people": [], "customers": [], "projects": []},
        "created_folders": {"people": [], "customers": [], "projects": []},
        "orphaned_manifest_entries": {"people": [], "customers": [], "projects": []},
    }
    
    for entity_type, config in ENTITY_CONFIGS.items():
        entity_dir = vault / config["folder"]
        manifest_path = get_manifest_path(vault, entity_type)
        
        # Create manifest if missing
        if not manifest_path.exists():
            create_manifest(vault, entity_type)
            continue
        
        content = manifest_path.read_text()
        manifest_entries = {r.get("Name") for r in parse_manifest_table(content) if r.get("Name")}
        
        # Get existing folders
        existing_folders = set()
        if entity_dir.exists():
            for folder in entity_dir.iterdir():
                if folder.is_dir() and not folder.name.startswith(("_", ".")):
                    existing_folders.add(folder.name)
        
        # Add folders missing from manifest
        for folder_name in existing_folders - manifest_entries:
            if add_to_manifest(vault, entity_type, folder_name):
                results["added_to_manifest"][entity_type].append(folder_name)
        
        # Handle manifest entries without folders
        for entry_name in manifest_entries - existing_folders:
            if create_missing_folders:
                if create_entity_folder(vault, entity_type, entry_name):
                    results["created_folders"][entity_type].append(entry_name)
            else:
                results["orphaned_manifest_entries"][entity_type].append(entry_name)
    
    return results


# ─────────────────────────────────────────────────────────────────────────────
# Entity Creation
# ─────────────────────────────────────────────────────────────────────────────


def create_entity_folder(
    vault: Path,
    entity_type: str,
    entity_name: str,
    metadata: dict | None = None,
) -> Path | None:
    """
    Create a new entity folder with README.
    
    Args:
        vault: Path to vault root
        entity_type: One of: people, customers, projects
        entity_name: Name for the new entity
        metadata: Optional metadata dict (role, company, description, etc.)
    
    Returns:
        Path to created folder, or None if already exists
    """
    config = ENTITY_CONFIGS.get(entity_type)
    if not config:
        raise ValueError(f"Unknown entity type: {entity_type}")
    
    base = vault / config["folder"]
    folder_name = entity_name.strip()
    folder_path = base / folder_name
    
    if folder_path.exists():
        return None  # Already exists
    
    # Create folder
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Load template
    workflow_root = vault / "Workflow"
    templates_dir = workflow_root / "templates"
    template_path = templates_dir / config["template"]
    
    if template_path.exists():
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        
        # Add custom filters
        def basename_filter(path: str) -> str:
            return Path(path).name
        
        env.filters["basename"] = basename_filter
        
        template = env.get_template(config["template"])
        
        # Build context
        today = datetime.now().strftime("%Y-%m-%d")
        context = {
            "entity_name": entity_name,
            "name": entity_name,
            "title": entity_name,
            "created_date": today,
            "last_contact": "",
            "date": today,
            "type": entity_type.rstrip("s"),
            "context_entries": [],
            "auto_created": True,
            **(metadata or {}),
        }
        
        readme_content = template.render(**context)
    else:
        # Fallback simple README
        readme_content = f"""---
type: {entity_type.rstrip("s")}
title: "{entity_name}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
auto_created: true
tags:
  - type/{entity_type.rstrip("s")}
  - needs-review
---

# {entity_name}

<!-- Auto-created entity - please review and enhance -->

## Recent Context

_No interactions yet._
"""
    
    # Write README
    readme_path = folder_path / "README.md"
    readme_path.write_text(readme_content)
    
    return folder_path


# ─────────────────────────────────────────────────────────────────────────────
# Web Search Enrichment
# ─────────────────────────────────────────────────────────────────────────────


def enrich_entity_with_web_search(
    entity_type: str,
    entity_name: str,
    context: str = "",
    client: OpenAI | None = None,
) -> dict[str, Any]:
    """
    Use OpenAI web search to enrich entity details.
    
    Args:
        entity_type: One of: people, customers, projects
        entity_name: Name of entity to research
        context: Additional context (company, role, etc.)
        client: OpenAI client (creates new if not provided)
    
    Returns:
        Dict with enriched metadata
    """
    if client is None:
        client = OpenAI()
    
    if entity_type == "people":
        query = f"Find information about {entity_name}"
        if context:
            query += f" who works at or is associated with {context}"
        query += ". Look for: current job title, company, LinkedIn profile, location, professional background."
        
        response_format = """Return JSON with these fields:
        {
            "role": "Current job title",
            "company": "Current company",
            "linkedin": "LinkedIn URL if found",
            "location": "City/region",
            "background": "Brief professional background",
            "confidence": 0.0-1.0
        }"""
    
    elif entity_type == "customers":
        query = f"Find information about {entity_name} company"
        if context:
            query += f" in the {context} industry"
        query += ". Look for: industry, headquarters location, company size, key products/services."
        
        response_format = """Return JSON with these fields:
        {
            "industry": "Primary industry",
            "location": "Headquarters location",
            "size": "Company size (employees or revenue)",
            "description": "Brief company description",
            "website": "Company website",
            "confidence": 0.0-1.0
        }"""
    
    else:
        return {}  # No web search for projects
    
    try:
        response = client.responses.create(
            model="gpt-4o",
            tools=[{"type": "web_search_preview"}],
            input=f"{query}\n\n{response_format}",
            store=False,
        )
        
        # Extract JSON from response
        output_text = response.output_text if hasattr(response, 'output_text') else str(response.output)
        
        # Try to parse JSON from response
        json_match = re.search(r'\{[^{}]*\}', output_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        
    except Exception as e:
        print(f"  Web search failed for {entity_name}: {e}")
    
    return {}


def enrich_entities_batch(
    vault: Path,
    entity_type: str,
    entity_names: list[str],
    client: OpenAI | None = None,
) -> dict[str, dict]:
    """
    Enrich multiple entities with web search.
    
    Returns:
        Dict mapping entity name to enriched metadata
    """
    if client is None:
        client = OpenAI()
    
    results = {}
    for name in entity_names:
        # Get existing context from manifest
        manifest_path = get_manifest_path(vault, entity_type)
        context = ""
        if manifest_path.exists():
            rows = parse_manifest_table(manifest_path.read_text())
            for row in rows:
                if row.get("Name") == name:
                    context = row.get("Company", "") or row.get("Industry", "")
                    break
        
        enriched = enrich_entity_with_web_search(entity_type, name, context, client)
        if enriched:
            results[name] = enriched
    
    return results


# ─────────────────────────────────────────────────────────────────────────────
# Discovered Entity Processing
# ─────────────────────────────────────────────────────────────────────────────


def process_discovered_entities(
    vault: Path,
    extractions: list,
    auto_create: bool = True,
    enrich_with_web: bool = False,
    client: OpenAI | None = None,
) -> dict[str, list[str]]:
    """
    Process entities discovered during extraction.
    
    Finds entities mentioned in extractions that don't exist in manifests
    and optionally creates them.
    
    Args:
        vault: Path to vault root
        extractions: List of BackfillExtraction objects
        auto_create: Whether to auto-create discovered entities
        enrich_with_web: Whether to use web search for enrichment
        client: OpenAI client for web search
    
    Returns:
        Dict with lists of created entity names per type
    """
    # Ensure manifests exist
    known = get_known_entities(vault)
    
    discovered = {"people": set(), "customers": set(), "projects": set()}
    created = {"people": [], "customers": [], "projects": []}
    
    # Collect all mentioned entities
    for ext in extractions:
        # From mentions
        for person in ext.mentions.people:
            resolved = resolve_alias(vault, "people", person)
            if resolved not in known["people"]:
                discovered["people"].add(person)
        
        for account in ext.mentions.accounts:
            resolved = resolve_alias(vault, "customers", account)
            if resolved not in known["customers"]:
                discovered["customers"].add(account)
        
        for project in ext.mentions.projects:
            resolved = resolve_alias(vault, "projects", project)
            if resolved not in known["projects"]:
                discovered["projects"].add(project)
        
        # From detail dicts
        for person_name in ext.person_details.keys():
            if person_name not in known["people"]:
                discovered["people"].add(person_name)
        
        for project_name in ext.project_details.keys():
            if project_name not in known["projects"]:
                discovered["projects"].add(project_name)
        
        for customer_name in ext.customer_details.keys():
            if customer_name not in known["customers"]:
                discovered["customers"].add(customer_name)
    
    if not auto_create:
        return {k: list(v) for k, v in discovered.items()}
    
    # Create discovered PEOPLE
    for person in discovered["people"]:
        # Skip first-name-only entries (ambiguous)
        name_parts = person.strip().split()
        if len(name_parts) < 2:
            continue
        
        # Get metadata from extractions
        metadata = {}
        for ext in extractions:
            if person in ext.person_details:
                pd = ext.person_details[person]
                metadata = {
                    "role": pd.role or "",
                    "company": pd.company or "",
                    "status": "active",
                    "context": pd.relationship or "Discovered in notes",
                }
                break
        
        # Web enrichment
        if enrich_with_web and client:
            enriched = enrich_entity_with_web_search(
                "people", person, metadata.get("company", ""), client
            )
            if enriched.get("confidence", 0) > 0.5:
                metadata.update({k: v for k, v in enriched.items() if v and k != "confidence"})
        
        if create_entity_folder(vault, "people", person, metadata):
            add_to_manifest(vault, "people", person, metadata)
            created["people"].append(person)
    
    # Create discovered CUSTOMERS
    for customer in discovered["customers"]:
        metadata = {}
        for ext in extractions:
            if customer in ext.customer_details:
                cd = ext.customer_details[customer]
                metadata = {
                    "type": cd.relationship or "Customer",
                    "industry": cd.industry or "",
                    "status": "active",
                    "context": "Discovered in notes",
                }
                break
        
        # Web enrichment
        if enrich_with_web and client:
            enriched = enrich_entity_with_web_search(
                "customers", customer, metadata.get("industry", ""), client
            )
            if enriched.get("confidence", 0) > 0.5:
                metadata.update({k: v for k, v in enriched.items() if v and k != "confidence"})
        
        if create_entity_folder(vault, "customers", customer, metadata):
            add_to_manifest(vault, "customers", customer, metadata)
            created["customers"].append(customer)
    
    # Create discovered PROJECTS
    for project in discovered["projects"]:
        metadata = {}
        for ext in extractions:
            if project in ext.project_details:
                pd = ext.project_details[project]
                metadata = {
                    "status": pd.status or "active",
                    "owner": pd.owner or "",
                    "description": pd.description or "Discovered in notes",
                }
                break
        
        if create_entity_folder(vault, "projects", project, metadata):
            add_to_manifest(vault, "projects", project, metadata)
            created["projects"].append(project)
    
    return created


# ─────────────────────────────────────────────────────────────────────────────
# File Naming
# ─────────────────────────────────────────────────────────────────────────────


def sanitize_filename(title: str, max_length: int = 60) -> str:
    """
    Sanitize a title for use as a filename.
    
    - Removes/replaces invalid characters
    - Truncates to max_length
    - Preserves readability
    """
    # Replace problematic characters
    title = title.replace("/", "-").replace("\\", "-")
    title = title.replace(":", " -").replace("|", "-")
    title = title.replace("?", "").replace("*", "")
    title = title.replace("<", "").replace(">", "")
    title = title.replace('"', "'")
    
    # Remove or replace other problematic patterns
    title = re.sub(r'\s+', ' ', title)  # Collapse whitespace
    title = title.strip(" .-_")
    
    # Truncate intelligently
    if len(title) > max_length:
        # Try to cut at a word boundary
        truncated = title[:max_length]
        last_space = truncated.rfind(" ")
        if last_space > max_length * 0.6:
            title = truncated[:last_space]
        else:
            title = truncated
    
    return title.strip()


def generate_note_filename(
    date: str,
    suggested_title: str,
    note_type: str = "meeting",
) -> str:
    """
    Generate a consistent filename for a note.
    
    Format: YYYY-MM-DD - {Title}.md
    
    Args:
        date: Date in YYYY-MM-DD format
        suggested_title: AI-suggested title
        note_type: Type of note for context
    
    Returns:
        Sanitized filename
    """
    # Sanitize and truncate title
    clean_title = sanitize_filename(suggested_title, max_length=60)
    
    # Build filename
    filename = f"{date} - {clean_title}.md"
    
    return filename


def rename_note_with_extraction(
    note_path: Path,
    extraction: Any,  # BackfillExtraction
    dry_run: bool = True,
) -> tuple[Path, bool]:
    """
    Rename a note based on extraction data.
    
    Args:
        note_path: Path to the note
        extraction: BackfillExtraction with suggested_title and date
        dry_run: If True, don't actually rename
    
    Returns:
        Tuple of (new_path, was_renamed)
    """
    if not extraction.suggested_title:
        return note_path, False
    
    # Get date from extraction or filename
    date = extraction.date or ""
    if not date:
        # Try to extract from filename
        match = re.match(r"(\d{4}-\d{2}-\d{2})", note_path.name)
        if match:
            date = match.group(1)
        else:
            date = datetime.now().strftime("%Y-%m-%d")
    
    # Generate new filename
    new_filename = generate_note_filename(
        date=date,
        suggested_title=extraction.suggested_title,
        note_type=extraction.note_type,
    )
    
    new_path = note_path.parent / new_filename
    
    # Check if rename needed
    if new_path == note_path:
        return note_path, False
    
    # Check for conflicts
    if new_path.exists():
        # Add suffix to avoid conflict
        stem = new_path.stem
        suffix = 1
        while new_path.exists():
            new_path = note_path.parent / f"{stem} ({suffix}).md"
            suffix += 1
    
    if not dry_run:
        note_path.rename(new_path)
    
    return new_path, True


def batch_rename_notes(
    vault: Path,
    extractions: list,
    dry_run: bool = True,
) -> list[tuple[Path, Path, bool]]:
    """
    Rename multiple notes based on extractions.
    
    Returns:
        List of (old_path, new_path, was_renamed) tuples
    """
    results = []
    
    for ext in extractions:
        # Use note_path (not source_path)
        if not ext.note_path:
            continue
        
        note_path = vault / ext.note_path
        if not note_path.exists():
            continue
        
        new_path, renamed = rename_note_with_extraction(note_path, ext, dry_run)
        results.append((note_path, new_path, renamed))
    
    return results

#!/usr/bin/env python3
"""
Manifest Sync: Build and maintain glossary manifests for prompt caching.

This script:
1. Scans People/Projects/Customers folders for READMEs
2. Extracts key metadata (role, company, email, context)
3. Uses AI to enrich sparse entries from README content
4. Updates _MANIFEST.md files with consistent formatting
5. Generates a combined glossary for prompt caching

Usage:
    python manifest_sync.py scan          # Scan and report missing data
    python manifest_sync.py sync          # Update manifests from READMEs
    python manifest_sync.py enrich        # AI-enrich sparse entries
    python manifest_sync.py build-cache   # Build cached glossary file

The cached glossary is used as a stable prefix for OpenAI API calls,
enabling prompt caching (up to 90% cost reduction on input tokens).
"""

import argparse
import json
import os
import re
import sys
import yaml
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Any

# Add parent dir for imports
sys.path.insert(0, str(Path(__file__).parent))
from utils.ai_client import get_client

# Paths
VAULT_ROOT = Path(__file__).parent.parent.parent
VAST_PEOPLE = VAULT_ROOT / "VAST" / "People"
VAST_PROJECTS = VAULT_ROOT / "VAST" / "Projects"
VAST_CUSTOMERS = VAULT_ROOT / "VAST" / "Customers and Partners"
PEOPLE_MANIFEST = VAST_PEOPLE / "_MANIFEST.md"
PROJECTS_MANIFEST = VAST_PROJECTS / "_MANIFEST.md"
CUSTOMERS_MANIFEST = VAST_CUSTOMERS / "_MANIFEST.md"
CACHE_DIR = VAULT_ROOT / "Workflow" / "_cache"
GLOSSARY_CACHE = CACHE_DIR / "glossary.json"
PERSONA_PATH = VAULT_ROOT / "Workflow" / "profiles" / "jason_persona.yaml"


@dataclass
class PersonEntry:
    """A person in the manifest."""
    name: str
    role: str = ""
    company: str = ""
    email: str = ""
    my_relationship: str = ""  # manager, peer, direct-report, customer, partner, executive, vendor, other
    context: str = ""
    last_contact: str = ""
    
    def is_sparse(self) -> bool:
        """Check if entry needs enrichment."""
        return not self.role or not self.company


@dataclass
class ProjectEntry:
    """A project in the manifest."""
    name: str
    owner: str = ""
    my_role: str = ""  # owner, contributor, stakeholder, informed
    description: str = ""
    status: str = "active"


@dataclass 
class CustomerEntry:
    """A customer/partner in the manifest."""
    name: str
    type: str = ""  # customer, partner, prospect
    industry: str = ""
    my_role: str = ""  # technical-lead, account-owner, support, stakeholder, none
    context: str = ""


# =============================================================================
# ATOMIC SYNC FUNCTIONS (for use by other scripts)
# =============================================================================

def sync_person_to_manifest(
    name: str, 
    updates: Dict[str, Any], 
    rebuild_cache: bool = True
) -> bool:
    """
    Update a single person's entry in the manifest after README changes.
    
    This is called by ingest_emails.py and other scripts after patching a README.
    It ensures the manifest row stays in sync with the README.
    
    Args:
        name: Person's folder name
        updates: Dict of fields that were updated (role, company, email, title, etc.)
        rebuild_cache: Whether to rebuild the glossary cache after
    
    Returns:
        True if manifest was updated
    """
    person_folder = VAST_PEOPLE / name
    if not person_folder.exists():
        return False
    
    # Re-scan this person's README for current state
    readme = person_folder / "README.md"
    if not readme.exists():
        return False
    
    content = readme.read_text()
    fm = parse_frontmatter(content)
    
    # Build updated entry from README + updates
    entry = PersonEntry(
        name=name,
        role=updates.get("role") or updates.get("title") or fm.get("role") or fm.get("title") or "",
        company=updates.get("company") or fm.get("company") or "",
        email=updates.get("email") or fm.get("email") or "",
        my_relationship=updates.get("my_relationship") or fm.get("my_relationship") or "",
        context=extract_context_summary(content, max_chars=100),
        last_contact=updates.get("last_contact") or fm.get("last_contact") or ""
    )
    
    # Load current manifest entries
    people = scan_people_folder()
    
    # Find and update the entry
    updated = False
    for i, p in enumerate(people):
        if p.name == name:
            people[i] = entry
            updated = True
            break
    
    if not updated:
        # New entry - add it
        people.append(entry)
        updated = True
    
    # Regenerate manifest
    manifest_content = generate_people_manifest(people)
    PEOPLE_MANIFEST.write_text(manifest_content)
    
    # Optionally rebuild the glossary cache
    if rebuild_cache:
        glossary = build_glossary_cache()
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        GLOSSARY_CACHE.write_text(json.dumps(glossary, indent=2, default=str))
    
    return True


def sync_customer_to_manifest(
    name: str, 
    updates: Dict[str, Any], 
    rebuild_cache: bool = True
) -> bool:
    """Update a single customer's entry in the manifest after README changes."""
    customer_folder = VAST_CUSTOMERS / name
    if not customer_folder.exists():
        return False
    
    readme = customer_folder / "README.md"
    if not readme.exists():
        return False
    
    content = readme.read_text()
    fm = parse_frontmatter(content)
    
    entry = CustomerEntry(
        name=name,
        type=updates.get("account_type") or fm.get("account_type") or "",
        industry=updates.get("industry") or fm.get("industry") or "",
        context=extract_context_summary(content, max_chars=100)
    )
    
    customers = scan_customers_folder()
    
    updated = False
    for i, c in enumerate(customers):
        if c.name == name:
            customers[i] = entry
            updated = True
            break
    
    if not updated:
        customers.append(entry)
        updated = True
    
    manifest_content = generate_customers_manifest(customers)
    CUSTOMERS_MANIFEST.write_text(manifest_content)
    
    if rebuild_cache:
        glossary = build_glossary_cache()
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        GLOSSARY_CACHE.write_text(json.dumps(glossary, indent=2, default=str))
    
    return True


def sync_project_to_manifest(
    name: str, 
    updates: Dict[str, Any], 
    rebuild_cache: bool = True
) -> bool:
    """Update a single project's entry in the manifest after README changes."""
    project_folder = VAST_PROJECTS / name
    if not project_folder.exists():
        return False
    
    readme = project_folder / "README.md"
    if not readme.exists():
        return False
    
    content = readme.read_text()
    fm = parse_frontmatter(content)
    
    entry = ProjectEntry(
        name=name,
        owner=updates.get("owner") or fm.get("owner") or "",
        status=updates.get("status") or fm.get("status") or "active",
        description=extract_context_summary(content, max_chars=100)
    )
    
    projects = scan_projects_folder()
    
    updated = False
    for i, p in enumerate(projects):
        if p.name == name:
            projects[i] = entry
            updated = True
            break
    
    if not updated:
        projects.append(entry)
        updated = True
    
    manifest_content = generate_projects_manifest(projects)
    PROJECTS_MANIFEST.write_text(manifest_content)
    
    if rebuild_cache:
        glossary = build_glossary_cache()
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        GLOSSARY_CACHE.write_text(json.dumps(glossary, indent=2, default=str))
    
    return True


# =============================================================================
# SCANNING FUNCTIONS
# =============================================================================

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    
    # Find the closing ---
    end_idx = content.find("\n---", 3)
    if end_idx == -1:
        return {}
    
    fm_text = content[4:end_idx]
    try:
        return yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return {}


def extract_profile_section(content: str) -> Dict[str, str]:
    """Extract Role, Company, Email from ## Profile section."""
    result = {"role": "", "company": "", "email": "", "location": "", "relationship": ""}
    
    # Find ## Profile section
    profile_match = re.search(r'^## Profile\s*\n(.*?)(?=\n##|\Z)', content, re.MULTILINE | re.DOTALL)
    if not profile_match:
        return result
    
    profile_text = profile_match.group(1)
    
    # Extract **Role**: ...
    role_match = re.search(r'\*\*Role\*\*:\s*(.+?)(?:\n|$)', profile_text)
    if role_match:
        role_text = role_match.group(1).strip()
        # Parse "Role at Company" format
        if " at " in role_text:
            parts = role_text.split(" at ", 1)
            result["role"] = parts[0].strip()
            result["company"] = parts[1].strip()
        else:
            result["role"] = role_text
    
    # Extract **Email**: ...
    email_match = re.search(r'\*\*Email\*\*:\s*(.+?)(?:\n|$)', profile_text)
    if email_match:
        result["email"] = email_match.group(1).strip()
    
    # Extract **Location**: ...
    location_match = re.search(r'\*\*Location\*\*:\s*(.+?)(?:\n|$)', profile_text)
    if location_match:
        result["location"] = location_match.group(1).strip()
    
    # Extract **Relationship**: ...
    rel_match = re.search(r'\*\*Relationship\*\*:\s*(.+?)(?:\n|$)', profile_text)
    if rel_match:
        result["relationship"] = rel_match.group(1).strip()
    
    return result


def extract_context_summary(content: str, max_chars: int = 200) -> str:
    """Extract a brief context summary from README."""
    # Try Background section first
    bg_match = re.search(r'\*\*Background\*\*:\s*\n(.*?)(?=\n##|\n\*\*|\Z)', content, re.DOTALL)
    if bg_match:
        bg_text = bg_match.group(1).strip()
        # Get first bullet point or paragraph
        lines = [l.strip() for l in bg_text.split('\n') if l.strip()]
        if lines:
            first_line = lines[0].lstrip('- ').strip()
            if len(first_line) > max_chars:
                return first_line[:max_chars-3] + "..."
            return first_line
    
    # Fall back to first Recent Context entry
    context_match = re.search(r'## Recent Context\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if context_match:
        context_text = context_match.group(1).strip()
        lines = [l.strip() for l in context_text.split('\n') if l.strip() and l.startswith('-')]
        if lines:
            first_entry = lines[0].lstrip('- ').strip()
            # Extract just the description part, not the wikilink
            desc_match = re.search(r':\s*(.+?)(?:\[\[|$)', first_entry)
            if desc_match:
                return desc_match.group(1).strip()[:max_chars]
    
    return ""


def scan_people_folder() -> List[PersonEntry]:
    """Scan all People folders and extract manifest data."""
    entries = []
    
    if not VAST_PEOPLE.exists():
        return entries
    
    for folder in sorted(VAST_PEOPLE.iterdir()):
        if not folder.is_dir() or folder.name.startswith(('_', '.')):
            continue
        
        readme = folder / "README.md"
        if not readme.exists():
            # Person folder without README - add sparse entry
            entries.append(PersonEntry(name=folder.name))
            continue
        
        content = readme.read_text()
        fm = parse_frontmatter(content)
        profile = extract_profile_section(content)
        context = extract_context_summary(content)
        
        entries.append(PersonEntry(
            name=folder.name,
            role=profile.get("role", ""),
            company=profile.get("company", ""),
            email=profile.get("email", ""),
            my_relationship=fm.get("my_relationship", ""),
            context=context,
            last_contact=fm.get("last_contact", "")
        ))
    
    return entries


def scan_projects_folder() -> List[ProjectEntry]:
    """Scan all Projects folders and extract manifest data."""
    entries = []
    
    if not VAST_PROJECTS.exists():
        return entries
    
    for folder in sorted(VAST_PROJECTS.iterdir()):
        if not folder.is_dir() or folder.name.startswith(('_', '.')):
            continue
        
        readme = folder / "README.md"
        desc = ""
        owner = ""
        status = "active"
        
        if readme.exists():
            content = readme.read_text()
            fm = parse_frontmatter(content)
            
            # Try to extract description from frontmatter or content
            if fm.get("description"):
                desc = fm["description"]
            
            # Extract owner if present
            owner_match = re.search(r'\*\*Owner\*\*:\s*(.+?)(?:\n|$)', content)
            if owner_match:
                owner = owner_match.group(1).strip()
            
            # Check status
            if fm.get("status"):
                status = fm["status"]
        
        entries.append(ProjectEntry(
            name=folder.name,
            owner=owner,
            my_role=fm.get("my_role", "") if readme.exists() else "",
            description=desc,
            status=status
        ))
    
    return entries


def scan_customers_folder() -> List[CustomerEntry]:
    """Scan all Customers and Partners folders."""
    entries = []
    
    if not VAST_CUSTOMERS.exists():
        return entries
    
    for folder in sorted(VAST_CUSTOMERS.iterdir()):
        if not folder.is_dir() or folder.name.startswith(('_', '.')):
            continue
        
        readme = folder / "README.md"
        entry_type = ""
        industry = ""
        context = ""
        
        if readme.exists():
            content = readme.read_text()
            fm = parse_frontmatter(content)
            
            # Extract type
            if fm.get("account_type"):
                entry_type = fm["account_type"]
            
            # Extract industry
            if fm.get("industry"):
                industry = fm["industry"]
            
            # Brief context
            context = extract_context_summary(content, max_chars=100)
        
        entries.append(CustomerEntry(
            name=folder.name,
            type=entry_type,
            industry=industry,
            my_role=fm.get("my_role", "") if readme.exists() else "",
            context=context
        ))
    
    return entries


def generate_people_manifest(entries: List[PersonEntry]) -> str:
    """Generate markdown manifest for People."""
    lines = [
        "# People Manifest",
        "",
        "> **Glossary of people** - Used for prompt caching in AI calls.",
        "> Updated automatically by `manifest_sync.py`.",
        "> Last sync: " + datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "## Entities",
        "",
        "| Name | Role | Company | Email | My Relationship | Context |",
        "|------|------|---------|-------|-----------------|---------|",
    ]
    
    for e in entries:
        # Escape pipe characters in values
        role = e.role.replace("|", "/") if e.role else ""
        company = e.company.replace("|", "/") if e.company else ""
        email = e.email.replace("|", "/") if e.email else ""
        my_rel = e.my_relationship.replace("|", "/") if e.my_relationship else ""
        context = e.context.replace("|", "/") if e.context else ""
        
        lines.append(f"| {e.name} | {role} | {company} | {email} | {my_rel} | {context} |")
    
    lines.extend([
        "",
        "## Aliases",
        "",
        "_Name mappings for fuzzy matching:_",
        "",
    ])
    
    # Add known aliases
    aliases = [
        ("Jan C. Stefansson", "Jonsi Stephenson"),
        ("Qiu Ke", "Qi Ke"),
        ("Pete Iming", "Pete Emig"),
        ("Pete Eming", "Pete Emig"),
        ("Olivia Borey", "Olivia Bouree"),
        ("Michael Myra", "Michael Myrah"),
        ("Leeraz Ben Or", "Liraz Ben Or"),
        ("Glenn Lockman", "Glenn Lockwood"),
    ]
    
    for alias, canonical in aliases:
        lines.append(f"- \"{alias}\" → {canonical}")
    
    return "\n".join(lines)


def generate_projects_manifest(entries: List[ProjectEntry]) -> str:
    """Generate markdown manifest for Projects."""
    lines = [
        "# Projects Manifest",
        "",
        "> **Glossary of projects and initiatives** - Used for prompt caching in AI calls.",
        "> Updated automatically by `manifest_sync.py`.",
        "> Last sync: " + datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "## Entities",
        "",
        "| Name | Owner | My Role | Status | Description |",
        "|------|-------|---------|--------|-------------|",
    ]
    
    for e in entries:
        desc = e.description.replace("|", "/")[:100] if e.description else ""
        owner = e.owner.replace("|", "/") if e.owner else ""
        my_role = e.my_role.replace("|", "/") if e.my_role else ""
        lines.append(f"| {e.name} | {owner} | {my_role} | {e.status} | {desc} |")
    
    return "\n".join(lines)


def generate_customers_manifest(entries: List[CustomerEntry]) -> str:
    """Generate markdown manifest for Customers."""
    lines = [
        "# Customers and Partners Manifest",
        "",
        "> **Glossary of accounts** - Used for prompt caching in AI calls.",
        "> Updated automatically by `manifest_sync.py`.",
        "> Last sync: " + datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "## Entities",
        "",
        "| Name | Type | Industry | My Role | Context |",
        "|------|------|----------|---------|---------|",
    ]
    
    for e in entries:
        entry_type = e.type.replace("|", "/") if e.type else ""
        industry = e.industry.replace("|", "/") if e.industry else ""
        my_role = e.my_role.replace("|", "/") if e.my_role else ""
        context = e.context.replace("|", "/")[:80] if e.context else ""
        lines.append(f"| {e.name} | {entry_type} | {industry} | {my_role} | {context} |")
    
    return "\n".join(lines)


def ai_enrich_person(entry: PersonEntry, readme_content: str) -> PersonEntry:
    """Use AI to extract role/company from README if missing."""
    if not entry.is_sparse():
        return entry
    
    client = get_client(caller="manifest_sync.enrich")
    
    prompt = f"""Extract the person's role and company from this README.

Person: {entry.name}

README Content:
{readme_content[:3000]}

Return JSON with:
- "role": Their job title/role (e.g., "VP Engineering", "CEO", "Account Manager")
- "company": Their company (e.g., "Microsoft", "VAST Data", "Google")
- "context": A 1-sentence summary of who they are

If not clearly stated, infer from context. Use "VAST Data" for internal colleagues.
If truly unknown, use empty string.

Return ONLY the JSON object, no markdown."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You extract structured data from notes. Return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        store=False
    )
    
    try:
        text = response.choices[0].message.content.strip()
        # Remove markdown code fences if present
        if text.startswith("```"):
            text = re.sub(r'^```\w*\n?', '', text)
            text = re.sub(r'\n?```$', '', text)
        
        data = json.loads(text)
        
        if data.get("role"):
            entry.role = data["role"]
        if data.get("company"):
            entry.company = data["company"]
        if data.get("context") and not entry.context:
            entry.context = data["context"]
            
    except (json.JSONDecodeError, KeyError, IndexError):
        pass
    
    return entry


def build_glossary_cache() -> Dict[str, Any]:
    """Build a combined glossary for prompt caching."""
    people = scan_people_folder()
    projects = scan_projects_folder()
    customers = scan_customers_folder()
    
    # Load persona
    persona_content = ""
    if PERSONA_PATH.exists():
        persona_content = PERSONA_PATH.read_text()
    
    glossary = {
        "version": "1.0",
        "generated_at": datetime.now().isoformat(),
        "people": [asdict(p) for p in people],
        "projects": [asdict(p) for p in projects],
        "customers": [asdict(c) for c in customers],
        "persona_yaml": persona_content,
        "token_estimate": 0  # Will be calculated
    }
    
    # Rough token estimate (4 chars per token average)
    content_str = json.dumps(glossary)
    glossary["token_estimate"] = len(content_str) // 4
    
    return glossary


def format_glossary_for_prompt(glossary: Dict[str, Any]) -> str:
    """Format glossary as a prompt prefix for caching."""
    lines = [
        "=== CONTEXT GLOSSARY (CACHED) ===",
        "",
        "## People Directory",
        "These are the people I work with:",
        ""
    ]
    
    for p in glossary.get("people", [])[:100]:  # Limit to top 100
        if p.get("role") or p.get("company"):
            lines.append(f"- **{p['name']}**: {p.get('role', '')} at {p.get('company', '')}")
            if p.get("email"):
                lines.append(f"  Email: {p['email']}")
        else:
            lines.append(f"- **{p['name']}**: (context unknown)")
    
    lines.extend([
        "",
        "## Projects & Initiatives",
        ""
    ])
    
    for proj in glossary.get("projects", [])[:50]:  # Limit to top 50
        status = proj.get("status", "active")
        desc = proj.get("description", "")[:100]
        lines.append(f"- **{proj['name']}** [{status}]: {desc}")
    
    lines.extend([
        "",
        "## Customers & Partners",
        ""
    ])
    
    for c in glossary.get("customers", []):
        ctype = c.get("type", "")
        industry = c.get("industry", "")
        info = f" ({ctype})" if ctype else ""
        if industry:
            info += f" - {industry}"
        lines.append(f"- **{c['name']}**{info}")
    
    lines.extend([
        "",
        "=== END GLOSSARY ===",
        ""
    ])
    
    return "\n".join(lines)


def cmd_scan(args):
    """Scan folders and report status."""
    print("Scanning People folder...")
    people = scan_people_folder()
    sparse_people = [p for p in people if p.is_sparse()]
    
    print(f"  Found {len(people)} people")
    print(f"  Sparse entries (need enrichment): {len(sparse_people)}")
    if args.verbose and sparse_people:
        for p in sparse_people[:10]:
            print(f"    - {p.name}")
        if len(sparse_people) > 10:
            print(f"    ... and {len(sparse_people) - 10} more")
    
    print("\nScanning Projects folder...")
    projects = scan_projects_folder()
    print(f"  Found {len(projects)} projects")
    
    print("\nScanning Customers folder...")
    customers = scan_customers_folder()
    print(f"  Found {len(customers)} customers/partners")
    
    # Summary
    print("\n=== Summary ===")
    print(f"Total entities: {len(people) + len(projects) + len(customers)}")
    print(f"People needing enrichment: {len(sparse_people)}")
    
    # Estimate cache size
    glossary = build_glossary_cache()
    print(f"Estimated glossary tokens: ~{glossary['token_estimate']}")


def cmd_sync(args):
    """Sync manifests from folder contents."""
    print("Syncing People manifest...")
    people = scan_people_folder()
    manifest_content = generate_people_manifest(people)
    PEOPLE_MANIFEST.write_text(manifest_content)
    print(f"  Wrote {len(people)} entries to {PEOPLE_MANIFEST}")
    
    print("\nSyncing Projects manifest...")
    projects = scan_projects_folder()
    manifest_content = generate_projects_manifest(projects)
    PROJECTS_MANIFEST.write_text(manifest_content)
    print(f"  Wrote {len(projects)} entries to {PROJECTS_MANIFEST}")
    
    print("\nSyncing Customers manifest...")
    customers = scan_customers_folder()
    manifest_content = generate_customers_manifest(customers)
    CUSTOMERS_MANIFEST.write_text(manifest_content)
    print(f"  Wrote {len(customers)} entries to {CUSTOMERS_MANIFEST}")
    
    print("\n✓ Manifests synced")


def cmd_enrich(args):
    """AI-enrich sparse entries."""
    print("Finding sparse people entries...")
    people = scan_people_folder()
    sparse = [p for p in people if p.is_sparse()]
    
    if not sparse:
        print("No sparse entries found!")
        return
    
    print(f"Found {len(sparse)} sparse entries to enrich")
    
    limit = args.limit or 10
    enriched = 0
    
    for entry in sparse[:limit]:
        readme_path = VAST_PEOPLE / entry.name / "README.md"
        if not readme_path.exists():
            print(f"  ⚠ {entry.name}: No README found")
            continue
        
        print(f"  Enriching {entry.name}...", end=" ")
        content = readme_path.read_text()
        
        enriched_entry = ai_enrich_person(entry, content)
        
        if enriched_entry.role or enriched_entry.company:
            print(f"→ {enriched_entry.role} at {enriched_entry.company}")
            
            # Update the entry in our list
            for i, p in enumerate(people):
                if p.name == entry.name:
                    people[i] = enriched_entry
                    break
            
            enriched += 1
        else:
            print("(no data extracted)")
    
    # Rewrite manifest with enriched data
    if enriched > 0:
        manifest_content = generate_people_manifest(people)
        PEOPLE_MANIFEST.write_text(manifest_content)
        print(f"\n✓ Enriched {enriched} entries, manifest updated")


def cmd_build_cache(args):
    """Build the cached glossary file."""
    print("Building glossary cache...")
    
    # Ensure cache directory exists
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    glossary = build_glossary_cache()
    
    # Write JSON cache
    GLOSSARY_CACHE.write_text(json.dumps(glossary, indent=2))
    print(f"  Wrote glossary to {GLOSSARY_CACHE}")
    print(f"  Token estimate: ~{glossary['token_estimate']}")
    
    # Also write a text version for inspection
    text_version = format_glossary_for_prompt(glossary)
    text_path = CACHE_DIR / "glossary.txt"
    text_path.write_text(text_version)
    print(f"  Wrote text version to {text_path}")
    
    print("\n✓ Glossary cache built")


def main():
    parser = argparse.ArgumentParser(
        description="Sync and maintain manifest glossaries for prompt caching"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # scan command
    scan_parser = subparsers.add_parser("scan", help="Scan folders and report status")
    scan_parser.add_argument("-v", "--verbose", action="store_true", help="Show details")
    
    # sync command
    sync_parser = subparsers.add_parser("sync", help="Sync manifests from READMEs")
    
    # enrich command
    enrich_parser = subparsers.add_parser("enrich", help="AI-enrich sparse entries")
    enrich_parser.add_argument("-l", "--limit", type=int, default=10, 
                               help="Max entries to enrich (default: 10)")
    
    # build-cache command
    cache_parser = subparsers.add_parser("build-cache", help="Build cached glossary file")
    
    args = parser.parse_args()
    
    if args.command == "scan":
        cmd_scan(args)
    elif args.command == "sync":
        cmd_sync(args)
    elif args.command == "enrich":
        cmd_enrich(args)
    elif args.command == "build-cache":
        cmd_build_cache(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

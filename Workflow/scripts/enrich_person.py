#!/usr/bin/env python3
"""
Person Enrichment: AI-powered data gathering for People READMEs.

Enrichment Levels:
  L0: Stub       - Just folder name exists
  L1: Contact    - Basic contact info from emails
  L2: README     - AI inference from existing README content
  L3: Web        - OpenAI web search for public info
  L4: Deep       - Multi-source comprehensive research

Usage:
    # Enrich a single person from README content (L2)
    python enrich_person.py "John Smith" --from-readme
    
    # Enrich with web search (L3)
    python enrich_person.py "John Smith" --web
    
    # Deep enrichment (L4)
    python enrich_person.py "John Smith" --deep
    
    # Batch enrich all sparse entries
    python enrich_person.py --all --level 2 --limit 20
    
    # Enrich contacts at a specific company
    python enrich_person.py --company "Microsoft" --level 3
    
    # List sparse entries
    python enrich_person.py --list-sparse

The enrichment system updates both:
1. The person's README.md frontmatter
2. The People _MANIFEST.md row
3. The glossary cache (for prompt caching)
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Any

import yaml

# Add parent dir for imports
sys.path.insert(0, str(Path(__file__).parent))
from utils.ai_client import get_client
from utils.config import get_model_config
from utils.frontmatter import parse_frontmatter, render_frontmatter
from manifest_sync import (
    VAST_PEOPLE, PEOPLE_MANIFEST, CACHE_DIR, GLOSSARY_CACHE,
    PersonEntry, scan_people_folder, generate_people_manifest,
    build_glossary_cache, sync_person_to_manifest, parse_frontmatter as parse_fm
)

# Paths
VAULT_ROOT = Path(__file__).parent.parent.parent
WEB_CACHE_DIR = VAULT_ROOT / "Workflow" / "_cache" / "web_enrichment"


# =============================================================================
# EXPORTED HELPERS (for use by other scripts like process_emails.py)
# =============================================================================

def sync_to_manifest(name: str) -> bool:
    """
    Sync a person's README to the manifest.
    
    Reads the current README frontmatter and updates the manifest row.
    """
    try:
        sync_person_to_manifest(name, updates={}, rebuild_cache=False)
        return True
    except Exception as e:
        print(f"Warning: Could not sync {name} to manifest: {e}")
        return False


def rebuild_glossary_cache() -> None:
    """Rebuild the glossary cache from manifests."""
    import json
    glossary = build_glossary_cache()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    GLOSSARY_CACHE.write_text(json.dumps(glossary, indent=2, default=str))
WEB_CACHE_DIR = VAULT_ROOT / "Workflow" / "_cache" / "web_enrichment"


@dataclass
class EnrichmentResult:
    """Result of enrichment operation."""
    name: str
    level_before: int
    level_after: int
    fields_added: List[str] = field(default_factory=list)
    fields_updated: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    source: str = ""  # "readme", "web", "deep"
    cached: bool = False


def get_enrichment_level(readme_path: Path) -> int:
    """Determine current enrichment level of a person."""
    if not readme_path.exists():
        return 0
    
    content = readme_path.read_text()
    fm = parse_fm(content)
    
    # Explicit level in frontmatter
    if fm.get("enrichment_level"):
        return int(fm.get("enrichment_level"))
    
    # Infer from data present
    has_email = bool(fm.get("email"))
    has_role = bool(fm.get("role") or fm.get("title"))
    has_company = bool(fm.get("company"))
    has_linkedin = bool(fm.get("linkedin"))
    has_bio = bool(fm.get("bio"))
    has_previous_roles = bool(fm.get("previous_roles"))
    
    if has_previous_roles or has_bio:
        return 4  # Deep enrichment
    if has_linkedin:
        return 3  # Web enrichment
    if has_role and has_company:
        return 2  # README enrichment
    if has_email:
        return 1  # Contact info
    return 0  # Stub


def is_sparse(readme_path: Path) -> bool:
    """Check if person needs enrichment (missing role or company)."""
    if not readme_path.exists():
        return True
    
    content = readme_path.read_text()
    fm = parse_fm(content)
    
    has_role = bool(fm.get("role") or fm.get("title"))
    has_company = bool(fm.get("company"))
    
    return not (has_role and has_company)


def list_sparse_entries(limit: int = 50) -> List[Path]:
    """List people folders that need enrichment."""
    sparse = []
    
    for folder in sorted(VAST_PEOPLE.iterdir()):
        if not folder.is_dir() or folder.name.startswith(('_', '.')):
            continue
        
        readme = folder / "README.md"
        if is_sparse(readme):
            sparse.append(readme)
            if len(sparse) >= limit:
                break
    
    return sparse


# =============================================================================
# LEVEL 2: README ENRICHMENT
# =============================================================================

def enrich_from_readme(name: str, dry_run: bool = False) -> EnrichmentResult:
    """
    Level 2 enrichment: Extract role/company from existing README content.
    
    Uses AI to infer role and company from the README body text.
    """
    result = EnrichmentResult(name=name, level_before=0, level_after=0, source="readme")
    
    person_folder = VAST_PEOPLE / name
    readme_path = person_folder / "README.md"
    
    if not readme_path.exists():
        result.errors.append(f"README not found: {readme_path}")
        return result
    
    content = readme_path.read_text()
    result.level_before = get_enrichment_level(readme_path)
    
    # Already at L2 or higher
    if result.level_before >= 2:
        result.level_after = result.level_before
        return result
    
    client = get_client(caller="enrich_person.readme")
    
    prompt = f"""Extract structured information about this person from their README.

Person: {name}

README Content:
{content[:4000]}

Return a JSON object with:
{{
    "role": "Job title (e.g., VP Engineering, CEO, Account Manager)",
    "company": "Company name (e.g., Microsoft, Google, VAST Data)",
    "context": "1-2 sentence summary of who they are and how we know them",
    "expertise": ["list", "of", "expertise", "areas"],
    "relationship": "customer|partner|colleague|vendor|other"
}}

Rules:
- Infer from context if not explicitly stated
- Use "VAST Data" for internal colleagues
- Leave empty string if truly unknown
- Be specific with roles (not just "Engineer" but "Senior Software Engineer")

Return ONLY valid JSON, no markdown."""

    try:
        model_config = get_model_config("enrichment")
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[
                {"role": "system", "content": "Extract structured data from notes. Return only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=model_config.get("temperature", 0.0),
            store=False
        )
        
        text = response.choices[0].message.content.strip()
        if text.startswith("```"):
            text = re.sub(r'^```\w*\n?', '', text)
            text = re.sub(r'\n?```$', '', text)
        
        data = json.loads(text)
        
    except Exception as e:
        result.errors.append(f"AI extraction failed: {e}")
        return result
    
    # Build updates
    updates = {}
    
    if data.get("role"):
        updates["role"] = data["role"]
        result.fields_added.append("role")
    
    if data.get("company"):
        updates["company"] = data["company"]
        result.fields_added.append("company")
    
    if data.get("expertise"):
        updates["expertise"] = data["expertise"]
        result.fields_added.append("expertise")
    
    if data.get("relationship"):
        updates["relationship"] = data["relationship"]
        result.fields_added.append("relationship")
    
    # Mark enrichment level and timestamp
    updates["enrichment_level"] = 2
    updates["last_enriched"] = datetime.now().strftime("%Y-%m-%d")
    
    if not updates or not result.fields_added:
        result.errors.append("No data extracted")
        return result
    
    if dry_run:
        result.level_after = 2
        return result
    
    # Apply updates to README
    fm = parse_fm(content)
    fm.update(updates)
    
    # Find where frontmatter ends
    if content.startswith("---"):
        end_idx = content.find("\n---", 3)
        if end_idx != -1:
            body = content[end_idx + 4:].lstrip("\n")
        else:
            body = ""
    else:
        body = content
    
    # Rebuild frontmatter
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{new_fm}---\n\n{body}"
    
    readme_path.write_text(new_content)
    
    # Sync to manifest
    sync_person_to_manifest(name, updates, rebuild_cache=True)
    
    result.level_after = 2
    return result


# =============================================================================
# LEVEL 3: WEB ENRICHMENT
# =============================================================================

def get_web_cache_path(name: str) -> Path:
    """Get cache path for web enrichment results."""
    safe_name = name.lower().replace(" ", "_").replace("/", "_")[:50]
    return WEB_CACHE_DIR / f"{safe_name}.json"


def is_cache_fresh(cache_path: Path, max_days: int = 30) -> bool:
    """Check if cached data is still fresh."""
    if not cache_path.exists():
        return False
    
    try:
        data = json.loads(cache_path.read_text())
        cached_at = datetime.fromisoformat(data.get("cached_at", "2000-01-01"))
        return (datetime.now() - cached_at).days < max_days
    except Exception:
        return False


def enrich_from_web(name: str, dry_run: bool = False, force: bool = False) -> EnrichmentResult:
    """
    Level 3 enrichment: Use OpenAI web search for public information.
    
    Searches for LinkedIn, company info, public profiles, etc.
    """
    result = EnrichmentResult(name=name, level_before=0, level_after=0, source="web")
    
    person_folder = VAST_PEOPLE / name
    readme_path = person_folder / "README.md"
    
    if not readme_path.exists():
        result.errors.append(f"README not found: {readme_path}")
        return result
    
    content = readme_path.read_text()
    fm = parse_fm(content)
    result.level_before = get_enrichment_level(readme_path)
    
    # Check cache first
    cache_path = get_web_cache_path(name)
    WEB_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    if not force and is_cache_fresh(cache_path):
        # Use cached data
        cached_data = json.loads(cache_path.read_text())
        data = cached_data.get("enrichment", {})
        result.cached = True
    else:
        # Need to do web search
        client = get_client(caller="enrich_person.web")
        
        # Build search context
        existing_company = fm.get("company", "")
        existing_role = fm.get("role") or fm.get("title", "")
        existing_email = fm.get("email", "")
        
        search_hints = []
        if existing_company:
            search_hints.append(f"Company: {existing_company}")
        if existing_role:
            search_hints.append(f"Role: {existing_role}")
        if existing_email:
            # Extract domain for search
            domain = existing_email.split("@")[-1] if "@" in existing_email else ""
            if domain and not domain.endswith(("gmail.com", "yahoo.com", "outlook.com")):
                search_hints.append(f"Email domain: {domain}")
        
        prompt = f"""Research this person using web search and return their professional information.

Person: {name}
Known info: {'; '.join(search_hints) if search_hints else 'None'}

Search for their LinkedIn profile, company info, and public background.

Return a JSON object with:
{{
    "role": "Current job title",
    "company": "Current employer",
    "linkedin": "LinkedIn URL if found",
    "bio": "1-2 sentence professional bio",
    "location": "City, State/Country",
    "previous_roles": [
        {{"title": "...", "company": "...", "years": "2020-2023"}}
    ],
    "education": ["University/Degree"],
    "expertise": ["areas", "of", "expertise"],
    "sources": ["URLs used as sources"]
}}

Important:
- Only include information you can verify from web sources
- Leave fields empty if not found
- Include LinkedIn URL if available
- Be specific about current role vs previous roles

Return ONLY valid JSON."""

        try:
            # Use the Responses API with web_search tool for actual web search
            model_config = get_model_config("web_enrichment")
            response = client.responses.create(
                model=model_config["model"],
                tools=[{"type": "web_search_preview"}],
                input=prompt,
                instructions="You are a professional researcher. Use the web_search tool to find accurate information about people. Return only verified data with source URLs.",
                store=False
            )
            
            # Extract text from response output
            text = ""
            for item in response.output:
                if hasattr(item, 'content'):
                    for content_part in item.content:
                        if hasattr(content_part, 'text'):
                            text = content_part.text
                            break
            
            if not text:
                result.errors.append("No text response from web search")
                return result
            
            text = text.strip()
            if text.startswith("```"):
                text = re.sub(r'^```\w*\n?', '', text)
                text = re.sub(r'\n?```$', '', text)
            
            data = json.loads(text)
            
            # Cache the result
            cache_data = {
                "name": name,
                "cached_at": datetime.now().isoformat(),
                "enrichment": data
            }
            cache_path.write_text(json.dumps(cache_data, indent=2))
            
        except Exception as e:
            result.errors.append(f"Web search failed: {e}")
            return result
    
    # Build updates from web data
    updates = {}
    
    if data.get("role") and not fm.get("role"):
        updates["role"] = data["role"]
        result.fields_added.append("role")
    elif data.get("role") and fm.get("role") != data["role"]:
        updates["role"] = data["role"]
        result.fields_updated.append("role")
    
    if data.get("company") and not fm.get("company"):
        updates["company"] = data["company"]
        result.fields_added.append("company")
    elif data.get("company") and fm.get("company") != data["company"]:
        updates["company"] = data["company"]
        result.fields_updated.append("company")
    
    if data.get("linkedin"):
        updates["linkedin"] = data["linkedin"]
        result.fields_added.append("linkedin")
    
    if data.get("bio"):
        updates["bio"] = data["bio"]
        result.fields_added.append("bio")
    
    if data.get("location"):
        updates["location"] = data["location"]
        result.fields_added.append("location")
    
    if data.get("previous_roles"):
        updates["previous_roles"] = data["previous_roles"]
        result.fields_added.append("previous_roles")
    
    if data.get("education"):
        updates["education"] = data["education"]
        result.fields_added.append("education")
    
    if data.get("expertise"):
        updates["expertise"] = data["expertise"]
        result.fields_added.append("expertise")
    
    # Mark enrichment level
    updates["enrichment_level"] = 3
    updates["last_enriched"] = datetime.now().strftime("%Y-%m-%d")
    
    if dry_run:
        result.level_after = 3
        return result
    
    # Apply updates
    fm.update(updates)
    
    # Rebuild content
    if content.startswith("---"):
        end_idx = content.find("\n---", 3)
        if end_idx != -1:
            body = content[end_idx + 4:].lstrip("\n")
        else:
            body = ""
    else:
        body = content
    
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{new_fm}---\n\n{body}"
    
    readme_path.write_text(new_content)
    
    # Sync to manifest
    sync_person_to_manifest(name, updates, rebuild_cache=True)
    
    result.level_after = 3
    return result


# =============================================================================
# LEVEL 4: DEEP ENRICHMENT
# =============================================================================

def enrich_deep(name: str, dry_run: bool = False) -> EnrichmentResult:
    """
    Level 4 enrichment: Comprehensive multi-source research.
    
    Does multiple web searches and cross-references information.
    """
    result = EnrichmentResult(name=name, level_before=0, level_after=0, source="deep")
    
    # First do L3 enrichment
    l3_result = enrich_from_web(name, dry_run=dry_run, force=True)
    
    if l3_result.errors:
        result.errors.extend(l3_result.errors)
        return result
    
    result.fields_added.extend(l3_result.fields_added)
    result.fields_updated.extend(l3_result.fields_updated)
    result.level_before = l3_result.level_before
    
    # TODO: Additional deep enrichment steps
    # - Company research (size, funding, industry)
    # - Mutual connections analysis
    # - Recent news/mentions
    # - Conference appearances
    # - Publications/patents
    
    person_folder = VAST_PEOPLE / name
    readme_path = person_folder / "README.md"
    
    if not dry_run and readme_path.exists():
        # Update level to 4
        content = readme_path.read_text()
        fm = parse_fm(content)
        fm["enrichment_level"] = 4
        fm["last_enriched"] = datetime.now().strftime("%Y-%m-%d")
        
        if content.startswith("---"):
            end_idx = content.find("\n---", 3)
            body = content[end_idx + 4:].lstrip("\n") if end_idx != -1 else ""
        else:
            body = content
        
        new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        readme_path.write_text(f"---\n{new_fm}---\n\n{body}")
    
    result.level_after = 4
    return result


# =============================================================================
# BATCH OPERATIONS
# =============================================================================

def enrich_batch(
    level: int = 2, 
    limit: int = 20, 
    company_filter: Optional[str] = None,
    dry_run: bool = False
) -> List[EnrichmentResult]:
    """Batch enrich multiple people."""
    
    results = []
    people = scan_people_folder()
    
    # Filter sparse entries
    candidates = []
    for person in people:
        readme = VAST_PEOPLE / person.name / "README.md"
        if not is_sparse(readme):
            continue
        
        # Company filter
        if company_filter:
            if company_filter.lower() not in (person.company or "").lower():
                continue
        
        candidates.append(person.name)
        if len(candidates) >= limit:
            break
    
    print(f"Enriching {len(candidates)} people at level {level}...")
    
    for i, name in enumerate(candidates, 1):
        print(f"\n[{i}/{len(candidates)}] {name}...")
        
        if level == 2:
            result = enrich_from_readme(name, dry_run=dry_run)
        elif level == 3:
            result = enrich_from_web(name, dry_run=dry_run)
        elif level == 4:
            result = enrich_deep(name, dry_run=dry_run)
        else:
            print(f"  Unknown level: {level}")
            continue
        
        results.append(result)
        
        if result.errors:
            print(f"  ❌ Errors: {result.errors}")
        elif result.fields_added or result.fields_updated:
            print(f"  ✅ Added: {result.fields_added}, Updated: {result.fields_updated}")
        else:
            print(f"  ⏭️  No changes (already at L{result.level_before})")
    
    return results


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Enrich People READMEs with AI-gathered information"
    )
    
    parser.add_argument("name", nargs="?", help="Person name to enrich")
    
    # Enrichment level options
    parser.add_argument("--from-readme", action="store_true", 
                        help="Level 2: Enrich from README content")
    parser.add_argument("--web", action="store_true", 
                        help="Level 3: Enrich using web search")
    parser.add_argument("--deep", action="store_true", 
                        help="Level 4: Deep multi-source research")
    
    # Batch options
    parser.add_argument("--all", action="store_true", 
                        help="Enrich all sparse entries")
    parser.add_argument("--level", type=int, default=2, 
                        help="Enrichment level for batch (default: 2)")
    parser.add_argument("--limit", type=int, default=20, 
                        help="Max entries for batch (default: 20)")
    parser.add_argument("--company", type=str, 
                        help="Filter by company for batch")
    
    # Utility options
    parser.add_argument("--list-sparse", action="store_true", 
                        help="List people needing enrichment")
    parser.add_argument("--force", action="store_true", 
                        help="Force refresh (ignore cache)")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Show what would be done")
    
    args = parser.parse_args()
    
    # List sparse entries
    if args.list_sparse:
        sparse = list_sparse_entries(limit=100)
        print(f"Found {len(sparse)} sparse entries:\n")
        for readme in sparse:
            level = get_enrichment_level(readme)
            print(f"  L{level}: {readme.parent.name}")
        return
    
    # Batch enrichment
    if args.all:
        results = enrich_batch(
            level=args.level,
            limit=args.limit,
            company_filter=args.company,
            dry_run=args.dry_run
        )
        
        # Summary
        added = sum(len(r.fields_added) for r in results)
        updated = sum(len(r.fields_updated) for r in results)
        errors = sum(len(r.errors) for r in results)
        
        print(f"\n{'='*50}")
        print(f"Summary: {len(results)} people processed")
        print(f"  Fields added: {added}")
        print(f"  Fields updated: {updated}")
        print(f"  Errors: {errors}")
        return
    
    # Single person enrichment
    if not args.name:
        parser.print_help()
        return
    
    if args.deep:
        result = enrich_deep(args.name, dry_run=args.dry_run)
    elif args.web:
        result = enrich_from_web(args.name, dry_run=args.dry_run, force=args.force)
    else:
        result = enrich_from_readme(args.name, dry_run=args.dry_run)
    
    # Print result
    print(f"\nEnrichment: {result.name}")
    print(f"  Level: L{result.level_before} → L{result.level_after}")
    print(f"  Source: {result.source}")
    if result.cached:
        print(f"  (used cached data)")
    if result.fields_added:
        print(f"  Added: {result.fields_added}")
    if result.fields_updated:
        print(f"  Updated: {result.fields_updated}")
    if result.errors:
        print(f"  Errors: {result.errors}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Customer/Partner Enrichment: Fill account metadata from READMEs (and optional web sources).

Levels:
  L0: Stub       - Folder only
  L1: Contact    - Basic type/industry present
  L2: README     - AI inference from README content (default)

Usage:
    # Enrich a single account from README content (L2)
    python enrich_customer.py "Microsoft" --from-readme

    # Batch enrich sparse accounts
    python enrich_customer.py --all --limit 20 --level 2

    # List sparse accounts (missing type/industry/stage)
    python enrich_customer.py --list-sparse
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

sys.path.insert(0, str(Path(__file__).parent))
from utils.ai_client import get_client
from utils.frontmatter import parse_frontmatter, render_frontmatter
from manifest_sync import (
    VAST_CUSTOMERS,
    CUSTOMERS_MANIFEST,
    CACHE_DIR,
    GLOSSARY_CACHE,
    CustomerEntry,
    scan_customers_folder,
    generate_customers_manifest,
    build_glossary_cache,
    sync_customer_to_manifest,
)


@dataclass
class EnrichmentResult:
    name: str
    level_before: int = 0
    level_after: int = 0
    fields_added: List[str] = field(default_factory=list)
    fields_updated: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    source: str = "readme"
    cached: bool = False


# =============================================================================
# Helpers
# =============================================================================

def get_enrichment_level(fm: Dict[str, Any]) -> int:
    """Roughly infer enrichment level."""
    if fm.get("enrichment_level"):
        try:
            return int(fm.get("enrichment_level"))
        except Exception:
            return 0
    has_type = bool(fm.get("account_type") or fm.get("type"))
    has_industry = bool(fm.get("industry"))
    has_stage = bool(fm.get("status"))
    if has_type and has_industry and has_stage:
        return 2
    if has_type and has_industry:
        return 1
    return 0


def is_sparse_customer(fm: Dict[str, Any]) -> bool:
    """Determine if account is missing key metadata."""
    return not (fm.get("account_type") or fm.get("type")) or not fm.get("industry") or not fm.get("status")


def list_sparse_entries(limit: int = 50) -> List[str]:
    """List sparse account folders."""
    names: List[str] = []
    for entry in scan_customers_folder():
        if entry.is_sparse():
            names.append(entry.name)
            if len(names) >= limit:
                break
    return names


# =============================================================================
# Enrichment (README / Level 2)
# =============================================================================

def enrich_from_readme(name: str, dry_run: bool = False, client: Optional[Any] = None) -> EnrichmentResult:
    """Extract account metadata from README using AI."""
    result = EnrichmentResult(name=name, source="readme")
    customer_dir = VAST_CUSTOMERS / name
    readme_path = customer_dir / "README.md"
    
    if not readme_path.exists():
        result.errors.append(f"README not found: {readme_path}")
        return result
    
    content = readme_path.read_text()
    fm, body = parse_frontmatter(content)
    if fm is None:
        fm = {}
    result.level_before = get_enrichment_level(fm)
    
    client = client or get_client(caller="enrich_customer.readme")
    prompt = f"""Extract structured account metadata from the README.

Account: {name}

README Content:
{content[:4000]}

Return JSON with:
- "account_type": customer|partner|prospect
- "industry": concise industry/vertical (e.g., Hyperscaler, AI, Media)
- "stage": lifecycle status (Active, Prospect, Blocked, Dormant, Churn Risk)
- "my_role": my relationship to this account (account-owner, technical-lead, support, stakeholder)
- "last_contact": most recent contact date if stated (YYYY-MM-DD)
- "context": 1-sentence summary of this account and current focus

Return ONLY the JSON object, no markdown."""
    
    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {"role": "system", "content": "Extract structured JSON. Return JSON only."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        store=False,
    )
    
    try:
        text = response.choices[0].message.content.strip()
        if text.startswith("```"):
            text = text.strip("`")
            text = text.replace("json", "", 1).strip()
        data = json.loads(text)
    except Exception as exc:  # noqa: BLE001
        result.errors.append(f"Parse error: {exc}")
        return result
    
    fields_changed: List[str] = []
    
    def maybe_set(key: str, target_key: str) -> None:
        if data.get(key):
            if fm.get(target_key) != data[key]:
                fields_changed.append(target_key)
            fm[target_key] = data[key]
    
    maybe_set("account_type", "account_type")
    maybe_set("industry", "industry")
    maybe_set("stage", "status")
    maybe_set("my_role", "my_role")
    maybe_set("last_contact", "last_contact")
    
    if data.get("context"):
        fm.setdefault("context_summary", data["context"])
    
    fm["enrichment_level"] = max(result.level_before, 2)
    fm["last_enriched"] = datetime.now().strftime("%Y-%m-%d")
    
    if dry_run:
        result.fields_added = fields_changed
        result.level_after = fm["enrichment_level"]
        return result
    
    new_content = render_frontmatter(fm) + body
    readme_path.write_text(new_content)
    
    sync_customer_to_manifest(
        name,
        updates={
            "account_type": fm.get("account_type"),
            "industry": fm.get("industry"),
            "status": fm.get("status"),
            "my_role": fm.get("my_role"),
            "last_contact": fm.get("last_contact"),
        },
        rebuild_cache=False,
    )
    customers = scan_customers_folder()
    CUSTOMERS_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    manifest_content = generate_customers_manifest(customers)
    CUSTOMERS_MANIFEST.write_text(manifest_content)
    
    glossary = build_glossary_cache()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    GLOSSARY_CACHE.write_text(json.dumps(glossary, indent=2, default=str))
    
    result.fields_added = fields_changed
    result.level_after = fm["enrichment_level"]
    return result


# =============================================================================
# CLI
# =============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich customer/partner manifests")
    parser.add_argument("name", nargs="?", help="Account name (folder)")
    parser.add_argument("--all", action="store_true", help="Enrich all sparse accounts")
    parser.add_argument("--list-sparse", action="store_true", help="List accounts needing enrichment")
    parser.add_argument("--limit", type=int, default=10, help="Limit for --all (default: 10)")
    parser.add_argument("--from-readme", action="store_true", help="Enrich from README content (default)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()
    
    if args.list_sparse:
        names = list_sparse_entries(limit=args.limit)
        if not names:
            print("No sparse accounts found.")
            return
        print("Sparse accounts:")
        for n in names:
            print(f"- {n}")
        return
    
    if args.all:
        targets = list_sparse_entries(limit=args.limit)
        if not targets:
            print("No sparse accounts found.")
            return
        print(f"Enriching {len(targets)} accounts...")
        for name in targets:
            result = enrich_from_readme(name, dry_run=args.dry_run)
            status = "ok" if not result.errors else f"error: {result.errors}"
            print(f"- {name}: {status}")
        return
    
    if not args.name:
        parser.print_help()
        return
    
    result = enrich_from_readme(args.name, dry_run=args.dry_run)
    if result.errors:
        print(f"Errors: {result.errors}")
    else:
        fields = ", ".join(result.fields_added) if result.fields_added else "no changes"
        print(f"✓ Enriched {args.name} to level {result.level_after} ({fields})")


if __name__ == "__main__":
    main()

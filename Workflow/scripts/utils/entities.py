#!/usr/bin/env python3
"""
Entity matching and resolution.

Handles fuzzy matching of names to vault folders and alias resolution.
Uses rapidfuzz for high-quality fuzzy matching.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Optional

import yaml
from rapidfuzz import fuzz, process

from .config import load_config, vault_root, workflow_root


# ─────────────────────────────────────────────────────────────────────────────
# Alias Loading
# ─────────────────────────────────────────────────────────────────────────────


@lru_cache(maxsize=1)
def _load_aliases_raw() -> dict:
    """Load raw aliases from YAML file."""
    config = load_config()
    alias_file = config.get("entity_matching", {}).get("alias_file", "")
    
    if alias_file:
        aliases_path = Path(alias_file)
    else:
        aliases_path = workflow_root() / "entities" / "aliases.yaml"
    
    if not aliases_path.exists():
        return {"people": {}, "accounts": {}, "projects": {}, "rob": {}}
    
    with open(aliases_path) as f:
        return yaml.safe_load(f) or {}


def _load_aliases() -> dict[str, str]:
    """
    Load flattened alias -> canonical mapping.
    
    Supports two YAML formats:
    1. List format: "Canonical Name": ["alias1", "alias2"]
    2. Dict format: "alias": "Canonical Name"
    
    Returns: {"alias_lower": "Canonical Name", ...}
    """
    raw = _load_aliases_raw()
    flat = {}
    
    for category in ["people", "accounts", "projects", "rob", "rob_forums"]:
        if category not in raw:
            continue
        
        cat_aliases = raw[category]
        if not isinstance(cat_aliases, dict):
            continue
        
        for key, value in cat_aliases.items():
            if isinstance(value, list):
                # Format: "Canonical Name": ["alias1", "alias2"]
                for alias in value:
                    flat[alias.lower()] = key
            elif isinstance(value, str):
                # Format: "alias": "Canonical Name"
                flat[key.lower()] = value
    
    return flat


# Public wrapper for loading aliases
def load_aliases() -> dict[str, str]:
    """Load flattened alias -> canonical mapping (public API)."""
    return _load_aliases()


# ─────────────────────────────────────────────────────────────────────────────
# Entity Enumeration
# ─────────────────────────────────────────────────────────────────────────────


def _get_entity_base_path(entity_type: str) -> tuple[str, str]:
    """Get (domain, folder) for entity type."""
    mapping = {
        "person": ("VAST", "People"),
        "people": ("VAST", "People"),
        "account": ("VAST", "Customers and Partners"),
        "accounts": ("VAST", "Customers and Partners"),
        "project": ("VAST", "Projects"),
        "projects": ("VAST", "Projects"),
        "rob": ("VAST", "ROB"),
        "rob_forums": ("VAST", "ROB"),
        "personal_person": ("Personal", "People"),
        "personal_project": ("Personal", "Projects"),
    }
    return mapping.get(entity_type, ("VAST", entity_type.title()))


def list_entities(entity_type: str) -> list[str]:
    """
    List all known entities of a type.
    
    Returns list of entity names (folder names).
    """
    root = vault_root()
    domain, folder = _get_entity_base_path(entity_type)
    base_path = root / domain / folder
    
    if not base_path.exists():
        return []
    
    return [
        d.name for d in base_path.iterdir() 
        if d.is_dir() and not d.name.startswith((".", "_"))
    ]


def list_all_entity_names() -> dict[str, list[str]]:
    """
    List all entity names by type (lightweight for context).
    
    Returns dict with entity lists.
    """
    result = {
        "people": list_entities("people"),
        "accounts": list_entities("accounts"),
        "projects": list_entities("projects"),
        "rob": list_entities("rob"),
    }
    
    # Also include personal entities
    personal_people = list_entities("personal_person")
    personal_projects = list_entities("personal_project")
    
    result["people"].extend(personal_people)
    result["projects"].extend(personal_projects)
    
    return result


def list_entity_folders(entity_type: str = None) -> dict[str, list[str]]:
    """
    List all entity folders in the vault.
    
    Alias for list_all_entity_names() for backwards compatibility.
    If entity_type specified, returns filtered dict.
    """
    all_entities = list_all_entity_names()
    
    if entity_type:
        return {entity_type: all_entities.get(entity_type, [])}
    
    return all_entities


# ─────────────────────────────────────────────────────────────────────────────
# Entity Matching
# ─────────────────────────────────────────────────────────────────────────────


def match_entity(
    name: str,
    entity_type: str,
    threshold: float = 0.8
) -> tuple[str | None, float]:
    """
    Match name to existing entity.
    
    Returns (folder_path, confidence).
    - Exact match: confidence = 1.0
    - Alias match: confidence = 0.95
    - Fuzzy match: confidence = similarity score
    - No match: (None, <best_score>)
    
    Example:
        >>> match_entity("Jeff", "people")
        ("VAST/People/Jeff Denworth", 0.95)
    """
    # Normalize input
    name_lower = name.lower().strip()
    
    # Get base path info
    domain, folder = _get_entity_base_path(entity_type)
    
    # Get known entities
    entities = list_entities(entity_type)
    entities_lower = {e.lower(): e for e in entities}
    
    # 1. Exact match
    if name_lower in entities_lower:
        canonical = entities_lower[name_lower]
        return f"{domain}/{folder}/{canonical}", 1.0
    
    # 2. Alias match
    aliases = _load_aliases()
    if name_lower in aliases:
        canonical = aliases[name_lower]
        # Verify the canonical name exists
        if canonical.lower() in entities_lower:
            canonical = entities_lower[canonical.lower()]
            return f"{domain}/{folder}/{canonical}", 0.95
    
    # 3. Fuzzy match using rapidfuzz
    if not entities:
        return None, 0.0
    
    result = process.extractOne(
        name,
        entities,
        scorer=fuzz.WRatio,
        score_cutoff=threshold * 100
    )
    
    if result:
        matched_name, score, _ = result
        return f"{domain}/{folder}/{matched_name}", score / 100
    
    # Return best score even if below threshold (for diagnostics)
    result = process.extractOne(name, entities, scorer=fuzz.WRatio)
    best_score = result[1] / 100 if result else 0.0
    
    return None, best_score


def match_entity_any_type(
    name: str,
    threshold: float = 0.8
) -> tuple[str | None, str | None, float]:
    """
    Match name across all entity types.
    
    Returns (folder_path, entity_type, confidence) or (None, None, 0.0).
    Tries each type and returns the best match.
    """
    best_path = None
    best_type = None
    best_score = 0.0
    
    for entity_type in ["people", "accounts", "projects", "rob"]:
        path, score = match_entity(name, entity_type, threshold)
        if score > best_score:
            best_path = path
            best_type = entity_type
            best_score = score
    
    return best_path, best_type, best_score


# ─────────────────────────────────────────────────────────────────────────────
# Entity Creation Helpers
# ─────────────────────────────────────────────────────────────────────────────


def suggest_entity_folder(name: str, entity_type: str) -> str:
    """
    Generate folder path for a new entity.
    
    Returns relative path like "VAST/People/New Person".
    """
    domain, folder = _get_entity_base_path(entity_type)
    clean_name = name.strip()
    return f"{domain}/{folder}/{clean_name}"


def get_entity_metadata(entity_names: set[str]) -> dict:
    """
    Get metadata for mentioned entities.
    
    Used by the planning phase to provide context about known entities.
    
    Returns dict with entity info:
        {
            "Jeff": {"path": "VAST/People/Jeff Denworth", "confidence": 0.95, "type": "people"},
            ...
        }
    """
    result = {}
    
    for name in entity_names:
        path, entity_type, confidence = match_entity_any_type(name)
        if path and confidence >= 0.8:
            result[name] = {
                "path": path,
                "confidence": confidence,
                "type": entity_type,
            }
    
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Mention Resolution (for extraction output)
# ─────────────────────────────────────────────────────────────────────────────


def resolve_mentions(mentions: dict[str, list[str]]) -> dict[str, list[dict]]:
    """
    Resolve extracted mentions to vault entities.
    
    Input: {"people": ["Jeff", "someone"], "projects": ["AI thing"]}
    Output: {
        "people": [
            {"name": "Jeff", "match": "VAST/People/Jeff Denworth", "confidence": 0.95},
            {"name": "someone", "match": None, "confidence": 0.0}
        ],
        ...
    }
    """
    resolved = {}
    
    # Map mention types to entity types
    type_mapping = {
        "people": "people",
        "projects": "projects",
        "accounts": "accounts",
    }
    
    for mention_type, names in mentions.items():
        resolved[mention_type] = []
        entity_type = type_mapping.get(mention_type, mention_type)
        
        for name in names:
            path, confidence = match_entity(name, entity_type)
            resolved[mention_type].append({
                "name": name,
                "match": path,
                "type": entity_type,
                "confidence": confidence,
            })
    
    return resolved


# ─────────────────────────────────────────────────────────────────────────────
# CLI/Testing
# ─────────────────────────────────────────────────────────────────────────────


if __name__ == "__main__":
    # Test entity matching
    try:
        from rich import print as rprint
    except ImportError:
        rprint = print
    
    print("Entity folders:")
    all_entities = list_all_entity_names()
    for etype, names in all_entities.items():
        print(f"  {etype}: {len(names)} entities")
        if names:
            print(f"    Examples: {names[:3]}")
    
    print("\nTest matches:")
    test_cases = [
        ("Jeff", "people"),
        ("Google", "accounts"),
        ("GDC", "accounts"),  # Alias test
        ("AI Pipelines", "projects"),
        ("unknown person xyz", "people"),
    ]
    
    for name, etype in test_cases:
        path, conf = match_entity(name, etype)
        print(f"  {name} ({etype}) -> {path} (confidence: {conf:.2f})")

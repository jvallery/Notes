"""
Profile loading and selection utilities.

Profiles are extraction rubrics that control how AI extracts information
from different types of content. They are NOT personas - they define
what to focus on, what to ignore, and how to handle edge cases.
"""

from pathlib import Path
from typing import Any

import yaml


# Profile directory
PROFILES_DIR = Path(__file__).parent.parent.parent / "profiles"

# Cache for loaded profiles
_profile_cache: dict[str, dict[str, Any]] = {}


def load_profile(profile_name: str) -> dict[str, Any]:
    """
    Load a profile by name.
    
    Args:
        profile_name: Name of the profile (without .yaml extension)
        
    Returns:
        Profile dictionary with all configuration
        
    Raises:
        FileNotFoundError: If profile doesn't exist
        ValueError: If profile is invalid
    """
    if profile_name in _profile_cache:
        return _profile_cache[profile_name]
    
    profile_path = PROFILES_DIR / f"{profile_name}.yaml"
    
    if not profile_path.exists():
        available = list_profiles()
        raise FileNotFoundError(
            f"Profile '{profile_name}' not found. "
            f"Available profiles: {', '.join(available)}"
        )
    
    with open(profile_path, "r") as f:
        profile = yaml.safe_load(f)
    
    if not profile or not isinstance(profile, dict):
        raise ValueError(f"Profile '{profile_name}' is empty or invalid")
    
    # Validate required fields
    required_fields = ["name", "focus", "task_rules"]
    for field in required_fields:
        if field not in profile:
            raise ValueError(f"Profile '{profile_name}' missing required field: {field}")
    
    _profile_cache[profile_name] = profile
    return profile


def list_profiles() -> list[str]:
    """
    List all available profile names.
    
    Returns:
        List of profile names (without .yaml extension)
    """
    if not PROFILES_DIR.exists():
        return []
    
    return sorted([
        p.stem for p in PROFILES_DIR.glob("*.yaml")
        if not p.name.startswith("_")  # Skip files starting with underscore
    ])


def select_profile(source_path: str, note_type: str | None = None) -> str:
    """
    Select the appropriate profile based on source path and note type.
    
    Uses path-based heuristics to determine the best profile:
    - VAST/Customers and Partners/* -> work_sales
    - VAST/People/* -> work_sales (defaults to sales context)
    - VAST/Projects/* -> work_engineering
    - VAST/ROB/* -> work_leadership
    - Personal/* -> personal
    
    Note type can override path-based selection:
    - customer/partners -> work_sales
    - projects -> work_engineering
    - rob -> work_leadership
    - journal -> personal
    
    Args:
        source_path: Path to the source file (relative or absolute)
        note_type: Optional note type hint from classification
        
    Returns:
        Profile name to use
    """
    path_lower = source_path.lower()
    
    # Note type overrides
    if note_type:
        type_mapping = {
            "customer": "work_sales",
            "partners": "work_sales",
            "people": "work_sales",  # Default 1:1s to sales context
            "projects": "work_engineering",
            "rob": "work_leadership",
            "journal": "personal",
            "travel": "personal",
        }
        if note_type in type_mapping:
            return type_mapping[note_type]
    
    # Path-based selection
    if "vast/" in path_lower:
        if "customers and partners" in path_lower:
            return "work_sales"
        elif "people/" in path_lower:
            return "work_sales"
        elif "projects/" in path_lower:
            return "work_engineering"
        elif "rob/" in path_lower:
            return "work_leadership"
        else:
            return "work_sales"  # Default work context
    elif "personal/" in path_lower:
        return "personal"
    elif "inbox/" in path_lower:
        # Content in Inbox - try to infer from filename
        if "meeting" in path_lower or "call" in path_lower or "1-1" in path_lower:
            return "work_sales"  # Default meeting context
        else:
            return "work_sales"  # Default to work context
    else:
        return "work_sales"  # Safe default


def get_profile_focus(profile_name: str) -> list[str]:
    """
    Get the focus areas for a profile.
    
    Args:
        profile_name: Name of the profile
        
    Returns:
        List of focus areas
    """
    profile = load_profile(profile_name)
    return profile.get("focus", [])


def get_profile_ignore(profile_name: str) -> list[str]:
    """
    Get the ignore patterns for a profile.
    
    Args:
        profile_name: Name of the profile
        
    Returns:
        List of things to ignore
    """
    profile = load_profile(profile_name)
    return profile.get("ignore", [])


def get_task_rules(profile_name: str) -> dict[str, Any]:
    """
    Get task extraction rules for a profile.
    
    Args:
        profile_name: Name of the profile
        
    Returns:
        Task rules dictionary
    """
    profile = load_profile(profile_name)
    return profile.get("task_rules", {})


def clear_cache():
    """Clear the profile cache. Useful for testing."""
    _profile_cache.clear()

#!/usr/bin/env python3
"""Jinja2 template engine for note rendering."""

import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .config import load_config, workflow_root


# ─────────────────────────────────────────────────────────────────────────────
# Custom Filters
# ─────────────────────────────────────────────────────────────────────────────


def slugify(text: str) -> str:
    """
    Convert text to URL-safe slug.
    
    Example: "Jeff Denworth" -> "jeff-denworth"
    """
    # Lowercase
    slug = text.lower()
    # Replace spaces with hyphens
    slug = slug.replace(" ", "-")
    # Remove non-alphanumeric except hyphens
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    # Collapse multiple hyphens
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def sanitize_path_name(name: str) -> str:
    """
    Sanitize a name for use in file/folder paths.
    
    Preserves readability (unlike slugify which lowercases everything).
    Removes/replaces characters that cause problems in paths:
    - / and \\ -> - (prevent nested directories)
    - : -> - (invalid on Windows, special on macOS)
    - " and ' -> removed (shell escaping issues)
    - & -> and
    - ( ) [ ] -> removed
    
    Example: 
        "Microsoft Comparison Slide (LSv4/LSv5)" -> "Microsoft Comparison Slide - LSv4-LSv5"
        "Fort Meade \"Gemini\" on-prem" -> "Fort Meade Gemini on-prem"
    """
    if not name:
        return name
    
    # Replace path separators and colons with dashes
    result = re.sub(r'[/\\:]', '-', name)
    
    # Replace ampersand with 'and'
    result = result.replace('&', 'and')
    
    # Remove quotes and brackets
    result = re.sub(r'["\'\(\)\[\]]', '', result)
    
    # Collapse multiple dashes/spaces
    result = re.sub(r'-+', '-', result)
    result = re.sub(r'\s+', ' ', result)
    
    # Strip leading/trailing dashes and spaces
    result = result.strip('- ')
    
    return result


def basename(path: str) -> str:
    """Get the basename of a path (filename without directory)."""
    return Path(path).name


def strip_extension(path: str) -> str:
    """Get the basename without extension."""
    return Path(path).stem


# ─────────────────────────────────────────────────────────────────────────────
# Template Environment
# ─────────────────────────────────────────────────────────────────────────────


def get_template_env() -> Environment:
    """
    Create Jinja2 environment with custom filters.
    
    Uses StrictUndefined to fail on missing variables,
    which helps catch template errors early.
    """
    config = load_config()
    template_dir = config.get("paths", {}).get("templates", "")
    
    if not template_dir:
        template_dir = workflow_root() / "templates"
    else:
        template_dir = Path(template_dir)
    
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        undefined=StrictUndefined,  # Fail on undefined variables
        trim_blocks=True,           # Remove first newline after block tag
        lstrip_blocks=True,         # Strip leading whitespace before block tags
    )
    
    # Add custom filters
    env.filters["slugify"] = slugify
    env.filters["basename"] = basename
    env.filters["strip_extension"] = strip_extension
    env.filters["tojson"] = lambda v, **kw: json.dumps(v, ensure_ascii=False, **kw)
    
    return env


def get_prompts_env() -> Environment:
    """
    Create Jinja2 environment for prompt templates.
    
    Separate from note templates to allow different configuration.
    """
    prompts_dir = workflow_root() / "prompts"
    
    env = Environment(
        loader=FileSystemLoader(str(prompts_dir)),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    # Add same filters
    env.filters["slugify"] = slugify
    env.filters["basename"] = basename
    env.filters["strip_extension"] = strip_extension
    env.filters["tojson"] = lambda v, **kw: json.dumps(v, ensure_ascii=False, indent=2, **kw)
    
    return env


# ─────────────────────────────────────────────────────────────────────────────
# Template Rendering
# ─────────────────────────────────────────────────────────────────────────────


# Whitelist of allowed templates to mitigate traversal/LLM-controlled names
ALLOWED_TEMPLATES = {
    "people.md.j2",
    "customer.md.j2",
    "projects.md.j2",
    "rob.md.j2",
    "journal.md.j2",
    "partners.md.j2",
    "readme-migration.md.j2",
}


def render_note(template_name: str, context: dict) -> str:
    """
    Render a note template with given context.
    
    Args:
        template_name: Name of template file (e.g., "people.md.j2")
        context: Dictionary of variables to pass to template
        
    Returns:
        Rendered markdown content
        
    Raises:
        ValueError: If template not in whitelist
        jinja2.UndefinedError: If required variable missing
    """
    if template_name not in ALLOWED_TEMPLATES:
        raise ValueError(f"Template not allowed: {template_name}")
    
    env = get_template_env()
    template = env.get_template(template_name)
    return template.render(**context)


def render_prompt(template_name: str, context: dict) -> str:
    """
    Render a prompt template with given context.
    
    Args:
        template_name: Name of prompt template (e.g., "system-extractor.md.j2")
        context: Dictionary of variables to pass to template
        
    Returns:
        Rendered prompt string
    """
    env = get_prompts_env()
    template = env.get_template(template_name)
    return template.render(**context)


# ─────────────────────────────────────────────────────────────────────────────
# CLI/Testing
# ─────────────────────────────────────────────────────────────────────────────


if __name__ == "__main__":
    # Test the template engine
    print("Template Engine Tests")
    print("=" * 40)
    
    # Test slugify
    tests = [
        ("Jeff Denworth", "jeff-denworth"),
        ("AI Pipelines Collateral", "ai-pipelines-collateral"),
        ("Test 123!@#", "test-123"),
        ("  Multiple   Spaces  ", "multiple-spaces"),
    ]
    
    for input_text, expected in tests:
        result = slugify(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} slugify('{input_text}') = '{result}'")
    
    # Test basename
    assert basename("/path/to/file.md") == "file.md"
    print("✓ basename works")
    
    # Test environment
    env = get_template_env()
    print(f"✓ Template environment created")
    print(f"  Template dir: {env.loader.searchpath}")

#!/usr/bin/env python3
"""
Configuration loader for Notes Vault automation.

Loads settings from config.yaml and .env files.
"""

import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


# Paths
# __file__ is in Workflow/scripts/utils/, so go up 3 levels to vault, 2 levels to Workflow
WORKFLOW_ROOT = Path(__file__).parent.parent.parent  # scripts/utils -> scripts -> Workflow
VAULT_ROOT = WORKFLOW_ROOT.parent                     # Workflow -> Notes (vault root)
CONFIG_PATH = WORKFLOW_ROOT / "config.yaml"
ENV_PATH = WORKFLOW_ROOT / ".env"


def load_config() -> dict[str, Any]:
    """Load configuration from config.yaml with environment variable substitution."""

    # Load environment variables first
    load_dotenv(ENV_PATH)

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    # Substitute environment variables
    config = _substitute_env_vars(config)

    # Resolve relative paths
    config = _resolve_paths(config)

    return config


def _substitute_env_vars(obj: Any) -> Any:
    """Recursively substitute ${VAR} and ${VAR:-default} patterns."""

    if isinstance(obj, str):
        import re

        # Pattern: ${VAR} or ${VAR:-default}
        pattern = r"\$\{([^}:]+)(?::-([^}]*))?\}"

        def replacer(match):
            var_name = match.group(1)
            default = match.group(2) or ""
            return os.environ.get(var_name, default)

        return re.sub(pattern, replacer, obj)

    elif isinstance(obj, dict):
        return {k: _substitute_env_vars(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [_substitute_env_vars(item) for item in obj]

    return obj


def _resolve_paths(config: dict) -> dict:
    """Resolve relative paths in the paths section."""

    vault_root = Path(config.get("paths", {}).get("vault_root", str(VAULT_ROOT)))

    if "paths" in config:
        for section in config["paths"]:
            if section == "vault_root":
                continue

            section_data = config["paths"][section]

            if isinstance(section_data, str):
                # Simple path string
                if not Path(section_data).is_absolute():
                    config["paths"][section] = str(vault_root / section_data)

            elif isinstance(section_data, dict):
                # Nested path dict
                for key, path in section_data.items():
                    if isinstance(path, str) and not Path(path).is_absolute():
                        config["paths"][section][key] = str(vault_root / path)

    return config


def get_model_config(task: str) -> dict[str, Any]:
    """Get model configuration for a specific task."""

    config = load_config()
    models = config.get("models", {})

    task_config = models.get(task, {})

    # Apply defaults
    return {
        "provider": task_config.get(
            "provider", models.get("default_provider", "openai")
        ),
        "model": task_config.get("model", "gpt-4o"),
        "fallback": task_config.get("fallback"),
        "temperature": task_config.get("temperature", 0.2),
        "max_tokens": task_config.get("max_tokens", 4096),
    }


def get_persona(note_type: str, sub_type: str = None) -> str | None:
    """Get persona file for a note type classification."""

    config = load_config()
    mapping = config.get("persona_mapping", {})

    type_config = mapping.get(note_type)

    if type_config is None:
        return None

    if isinstance(type_config, str):
        return type_config

    if isinstance(type_config, dict):
        if sub_type and sub_type in type_config:
            return type_config[sub_type]
        return type_config.get("default")

    return None


# Convenience accessors
def vault_root() -> Path:
    """Get vault root path."""
    return VAULT_ROOT


def workflow_root() -> Path:
    """Get workflow root path."""
    return WORKFLOW_ROOT


if __name__ == "__main__":
    # Test configuration loading
    from rich import print as rprint

    config = load_config()
    rprint("[bold]Configuration loaded:[/bold]")
    rprint(config)

#!/usr/bin/env python3
"""
Configuration loader for Notes Vault automation.

Loads config.yaml and .env, providing a unified interface for all settings.
Supports environment variable substitution in YAML values.

Usage:
    from config import config

    model = config.models.extract_transcript.model
    inbox_path = config.paths.inbox.email
"""

import os
import re
from pathlib import Path
from typing import Any, Optional

import yaml
from dotenv import load_dotenv


class ConfigNode:
    """Allows dot-notation access to nested config dictionaries."""

    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, ConfigNode(value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f"ConfigNode({self.__dict__})"

    def to_dict(self) -> dict:
        """Convert back to dictionary."""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, ConfigNode):
                result[key] = value.to_dict()
            else:
                result[key] = value
        return result


class Config:
    """Main configuration class for Notes Vault automation."""

    def __init__(
        self, config_path: Optional[Path] = None, env_path: Optional[Path] = None
    ):
        # Determine paths - config.yaml is in Workflow/, not Workflow/scripts/
        self.scripts_dir = Path(__file__).parent
        self.workflow_dir = self.scripts_dir.parent
        self.config_path = config_path or self.workflow_dir / "config.yaml"
        self.env_path = env_path or self.workflow_dir / ".env"

        # Load environment variables first
        self._load_env()

        # Load and parse config
        self._raw_config = self._load_yaml()
        self._config = self._substitute_env_vars(self._raw_config)

        # Create dot-notation accessors
        self._create_accessors()

    def _load_env(self):
        """Load .env file if it exists."""
        if self.env_path.exists():
            load_dotenv(self.env_path)

    def _load_yaml(self) -> dict:
        """Load the YAML config file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path) as f:
            return yaml.safe_load(f)

    def _substitute_env_vars(self, obj: Any) -> Any:
        """
        Recursively substitute ${VAR} and ${VAR:-default} patterns.
        """
        if isinstance(obj, str):
            # Pattern: ${VAR} or ${VAR:-default}
            pattern = r"\$\{([^}:]+)(?::-([^}]*))?\}"

            def replace(match):
                var_name = match.group(1)
                default = match.group(2) if match.group(2) is not None else ""
                return os.environ.get(var_name, default)

            return re.sub(pattern, replace, obj)

        elif isinstance(obj, dict):
            return {k: self._substitute_env_vars(v) for k, v in obj.items()}

        elif isinstance(obj, list):
            return [self._substitute_env_vars(item) for item in obj]

        return obj

    def _create_accessors(self):
        """Create dot-notation accessors for config sections."""
        for key, value in self._config.items():
            if isinstance(value, dict):
                setattr(self, key, ConfigNode(value))
            else:
                setattr(self, key, value)

    @property
    def vault_root(self) -> Path:
        """Get the vault root as a Path object."""
        return Path(self.paths.vault_root)

    def get_path(self, *keys: str) -> Path:
        """
        Get a full path by navigating the paths config.

        Example:
            config.get_path('inbox', 'email')
            # Returns: Path('/Users/jason/Documents/Notes/Inbox/Email')
        """
        node = self.paths
        for key in keys:
            node = getattr(node, key)

        path = Path(node)
        if not path.is_absolute():
            path = self.vault_root / path

        return path

    def get_model_config(self, task: str) -> dict:
        """
        Get model configuration for a specific task.

        Example:
            config.get_model_config('extract_transcript')
            # Returns: {'provider': 'openai', 'model': 'gpt-4o', ...}
        """
        model_node = getattr(self.models, task, None)
        if model_node is None:
            raise ValueError(f"Unknown model task: {task}")

        return (
            model_node.to_dict() if isinstance(model_node, ConfigNode) else model_node
        )

    def get_note_type_config(self, note_type: str) -> dict:
        """Get configuration for a specific note type."""
        type_node = getattr(self.note_types, note_type, None)
        if type_node is None:
            raise ValueError(f"Unknown note type: {note_type}")

        return type_node.to_dict() if isinstance(type_node, ConfigNode) else type_node

    def is_feature_enabled(self, feature: str) -> bool:
        """Check if a feature flag is enabled."""
        return getattr(self.features, feature, False)

    def reload(self):
        """Reload configuration from disk."""
        self._load_env()
        self._raw_config = self._load_yaml()
        self._config = self._substitute_env_vars(self._raw_config)
        self._create_accessors()


# Singleton instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get the singleton config instance."""
    global _config
    if _config is None:
        _config = Config()
    return _config


# Convenience alias
config = property(lambda self: get_config())


if __name__ == "__main__":
    # Test the config loader
    cfg = Config()

    print("=== Config Test ===")
    print(f"Vault root: {cfg.vault_root}")
    print(f"Inbox email path: {cfg.get_path('inbox', 'email')}")
    print(f"Extract model: {cfg.get_model_config('extract_transcript')}")
    print(f"Customer note type: {cfg.get_note_type_config('customer')}")
    print(f"Use embeddings: {cfg.is_feature_enabled('use_embeddings')}")

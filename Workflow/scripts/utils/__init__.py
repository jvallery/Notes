"""
Utility modules for Notes Vault automation.
"""

from .config import (
    load_config,
    get_model_config,
    get_persona,
    vault_root,
    workflow_root,
)
from .entities import (
    list_entities,
    list_entity_folders,
    list_all_entity_names,
    match_entity,
    match_entity_any_type,
    suggest_entity_folder,
    get_entity_metadata,
    resolve_mentions,
    load_aliases,
    normalize_person_name,
    normalize_task_owner,
)
from .git_ops import (
    is_git_repo,
    is_dirty,
    is_clean,
    get_status,
    get_changed_files,
    require_clean,
    add_files,
    commit,
    commit_batch,
    get_current_branch,
    get_last_commit,
    revert_last,
    stash_changes,
    pop_stash,
    GitStatus,
    CHECKED_PATHS,
    IGNORED_PATTERNS,
)
from .paths import (
    get_archive_path,
    get_extraction_path,
    get_changeplan_path,
    safe_relative_path,
    ensure_parent_exists,
)
from .fs import (
    atomic_write,
    safe_read_text,
    backup_file,
)
from .templates import (
    slugify,
    sanitize_path_name,
    basename,
    strip_extension,
    get_template_env,
    get_prompts_env,
    render_note,
    render_prompt,
    ALLOWED_TEMPLATES,
)
from .profiles import (
    load_profile,
    list_profiles,
    select_profile,
    get_profile_focus,
    get_profile_ignore,
    get_task_rules,
    clear_cache as clear_profile_cache,
)
from .ai_client import (
    get_client as get_ai_client,
    get_openai_client,
    get_logger as get_ai_logger,
    get_daily_stats as get_ai_stats,
    AILogger,
    InstrumentedClient,
)
from .logging import (
    setup_logging,
    get_logger,
    get_log_file,
    set_context,
    clear_context,
    log_summary,
    ContextLogger,
)

__all__ = [
    # Config
    "load_config",
    "get_model_config",
    "get_persona",
    "vault_root",
    "workflow_root",
    # Entities
    "list_entities",
    "list_entity_folders",
    "list_all_entity_names",
    "match_entity",
    "match_entity_any_type",
    "suggest_entity_folder",
    "get_entity_metadata",
    "resolve_mentions",
    "load_aliases",
    "normalize_person_name",
    "normalize_task_owner",
    # Git
    "is_git_repo",
    "is_dirty",
    "is_clean",
    "get_status",
    "get_changed_files",
    "require_clean",
    "add_files",
    "commit",
    "commit_batch",
    "get_current_branch",
    "get_last_commit",
    "revert_last",
    "stash_changes",
    "pop_stash",
    "GitStatus",
    "CHECKED_PATHS",
    "IGNORED_PATTERNS",
    # Paths
    "get_archive_path",
    "get_extraction_path",
    "get_changeplan_path",
    "safe_relative_path",
    "ensure_parent_exists",
    # File System
    "atomic_write",
    "safe_read_text",
    "backup_file",
    # Templates
    "slugify",
    "sanitize_path_name",
    "basename",
    "strip_extension",
    "get_template_env",
    "get_prompts_env",
    "render_note",
    "render_prompt",
    "ALLOWED_TEMPLATES",
    # Profiles
    "load_profile",
    "list_profiles",
    "select_profile",
    "get_profile_focus",
    "get_profile_ignore",
    "get_task_rules",
    "clear_profile_cache",
    # AI Client
    "get_ai_client",
    "get_openai_client",
    "get_ai_logger",
    "get_ai_stats",
    "AILogger",
    "InstrumentedClient",
    # Logging
    "setup_logging",
    "get_logger",
    "get_log_file",
    "set_context",
    "clear_context",
    "log_summary",
    "ContextLogger",
]

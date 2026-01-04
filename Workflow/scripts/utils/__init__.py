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
    list_entity_paths,
    list_all_entity_names,
    match_entity,
    match_entity_any_type,
    suggest_entity_folder,
    get_entity_metadata,
    resolve_mentions,
    load_aliases,
)
from .git_ops import (
    is_git_repo,
    is_dirty,
    is_clean,
    get_status,
    get_changed_files,
    require_clean,
    add_files,
    stage_content_dirs,
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
from .openai_client import (
    get_client,
    parse_structured,
    check_api_key,
    estimate_tokens,
    OpenAIError,
)
from .logging import (
    setup_logging,
    log_event,
    close_logging,
    get_log_path,
    get_run_id,
)
from .validation import (
    validate_changeplan,
)
from .standards_check import (
    check_frontmatter,
    check_filename,
    check_path,
    validate_before_write,
    validate_for_apply,
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
    "list_entity_paths",
    "list_all_entity_names",
    "match_entity",
    "match_entity_any_type",
    "suggest_entity_folder",
    "get_entity_metadata",
    "resolve_mentions",
    "load_aliases",
    # Git
    "is_git_repo",
    "is_dirty",
    "is_clean",
    "get_status",
    "get_changed_files",
    "require_clean",
    "add_files",
    "stage_content_dirs",
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
    # OpenAI
    "get_client",
    "parse_structured",
    "check_api_key",
    "estimate_tokens",
    "OpenAIError",
    # Logging
    "setup_logging",
    "log_event",
    "close_logging",
    "get_log_path",
    "get_run_id",
    # Validation
    "validate_changeplan",
    # Standards Check
    "check_frontmatter",
    "check_filename",
    "check_path",
    "validate_before_write",
    "validate_for_apply",
]

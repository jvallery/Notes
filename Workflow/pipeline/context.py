"""
Context Bundle - Load context for extraction and output generation.

The ContextBundle provides:
- Persona (my role, priorities, communication style)
- Entity manifests (compact lists of known people/companies/projects)
- Glossary (acronyms, terms)
- Aliases (name normalization)
- Relevant entity READMEs (for entities mentioned in content)

PROMPT CACHING:
OpenAI caches prompt prefixes that are 1024+ tokens and identical across calls.
The ContextBundle structures prompts with static content FIRST (cacheable):
  1. Persona (identity, style, rules)
  2. Entity glossary (people, companies, projects)
  3. Aliases and acronyms

Followed by dynamic content (per-call):
  4. Relevant READMEs for mentioned entities
  5. Source-specific instructions
"""

import sys
import hashlib
from pathlib import Path
from typing import Optional, Tuple, Any
from functools import lru_cache
from pydantic import BaseModel, Field, ConfigDict

sys.path.insert(0, str(Path(__file__).parent.parent))

from .envelope import ContentEnvelope
from .entities import EntityIndex
from scripts.utils.config import load_config

# Optional cached prompt helpers (keeps persona/glossary in cache-friendly format)
try:  # pragma: no cover - helper is optional in runtime
    from scripts.utils.cached_prompts import (  # type: ignore
        get_persona_context as _cached_persona_context,
        get_glossary_context as _cached_glossary_context,
    )
except Exception:  # pragma: no cover
    _cached_persona_context = None
    _cached_glossary_context = None


class ContextBundle(BaseModel):
    """All context needed for extraction and output generation."""
    
    model_config = ConfigDict(extra="ignore")
    
    # Static context (loaded once per session)
    persona: str = ""
    people_manifest: str = ""
    company_manifest: str = ""
    project_manifest: str = ""  # Projects manifest with acronyms/definitions
    project_list: list[str] = Field(default_factory=list)
    glossary: dict[str, str] = Field(default_factory=dict)
    aliases: dict[str, str] = Field(default_factory=dict)
    
    # Dynamic context (per content item)
    relevant_readmes: dict[str, str] = Field(default_factory=dict)
    
    @classmethod
    def load(cls, vault_root: Path, envelope: Optional[ContentEnvelope] = None, entity_index: Optional[EntityIndex] = None, config: Optional[dict[str, Any]] = None) -> "ContextBundle":
        """Load context for extraction.
        
        Args:
            vault_root: Path to vault root
            envelope: Optional ContentEnvelope to load relevant READMEs for
        
        Returns:
            ContextBundle with all context loaded
        """
        bundle = cls()
        cfg = config or load_config(vault_root_override=vault_root)
        paths_cfg = cfg.get("paths", {})
        work_paths = paths_cfg.get("work", {})
        personal_paths = paths_cfg.get("personal", {})
        resources_paths = paths_cfg.get("resources", {})
        
        people_manifest_path = Path(work_paths.get("people", vault_root / "VAST" / "People")) / "_MANIFEST.md"
        company_manifest_path = Path(work_paths.get("accounts", vault_root / "VAST" / "Customers and Partners")) / "_MANIFEST.md"
        project_manifest_path = Path(work_paths.get("projects", vault_root / "VAST" / "Projects")) / "_MANIFEST.md"
        project_paths = [
            Path(work_paths.get("projects", vault_root / "VAST" / "Projects")),
            Path(personal_paths.get("projects", vault_root / "Personal" / "Projects")),
        ]
        
        index = entity_index or EntityIndex(vault_root, config=cfg)
        
        # Load static context
        bundle.persona = _load_persona(vault_root, resources_paths)
        bundle.people_manifest = _load_manifest(people_manifest_path)
        bundle.company_manifest = _load_manifest(company_manifest_path)
        bundle.project_manifest = _load_manifest(project_manifest_path)
        bundle.project_list = _list_projects(project_paths)
        
        # Load glossary from YAML file (legacy) and merge with project manifest acronyms
        bundle.glossary = _load_glossary(vault_root, resources_paths)
        project_acronyms = _extract_acronyms_from_manifest(bundle.project_manifest)
        bundle.glossary.update(project_acronyms)
        
        # Load aliases from YAML file and merge with manifest Aliases column
        bundle.aliases = _load_aliases(vault_root, resources_paths)
        manifest_aliases = _extract_aliases_from_manifest(bundle.people_manifest)
        bundle.aliases.update(manifest_aliases)
        
        # Load dynamic context if envelope provided
        if envelope:
            mentioned = set(_quick_entity_scan(envelope.raw_content, bundle))
            mentioned.update(envelope.participants or [])
            mentioned.update(_extract_candidate_names(envelope.raw_content))
            
            normalized_candidates = {index.normalize_name(name) for name in mentioned if name}
            enriched: set[str] = set()
            for name in normalized_candidates:
                # Try exact matches first
                folder = index.find_person(name) or index.find_company(name) or index.find_project(name)
                if folder:
                    enriched.add(folder.name)
                    continue
                
                # Fuzzy matches by entity type
                fuzzy_person = index.search_person(name, limit=1)
                if fuzzy_person:
                    enriched.add(fuzzy_person[0].name)
                    continue
                fuzzy_company = index.search_company(name, limit=1)
                if fuzzy_company:
                    enriched.add(fuzzy_company[0].name)
                    continue
                fuzzy_project = index.search_project(name, limit=1)
                if fuzzy_project:
                    enriched.add(fuzzy_project[0].name)
            
            enriched.update(normalized_candidates)
            bundle.relevant_readmes = _load_entity_readmes(list(enriched)[:12], vault_root, index)
        
        return bundle
    
    def get_cacheable_prefix(self) -> Tuple[str, str]:
        """Get the cacheable (static) portion of the prompt.
        
        Returns a tuple of (prefix, hash) where:
        - prefix: The static prompt content that should be cached
        - hash: A content hash to verify cache hits
        
        OpenAI caches prompt prefixes >= 1024 tokens that are identical.
        By separating static (persona + glossary) from dynamic (READMEs),
        we get cache hits across different extraction calls.
        """
        sections = []
        
        # 1. Persona (static)
        persona_text = None
        if _cached_persona_context:
            persona_text = _cached_persona_context(include_full=True)
        elif self.persona:
            persona_text = self.persona
        if persona_text:
            sections.append(f"## PERSONA\n{persona_text}")
        
        # 2. Entity glossary (static - changes only when manifests change)
        glossary = None
        if _cached_glossary_context:
            glossary = _cached_glossary_context(compact=True)
        else:
            glossary = self._format_compact_glossary()
        if glossary:
            sections.append(f"## ENTITY GLOSSARY\n{glossary}")
        
        # 3. Aliases (static)
        if self.aliases:
            alias_section = "## NAME ALIASES\n"
            alias_items = [f"- {k} → {v}" for k, v in list(self.aliases.items())]
            alias_section += "\n".join(alias_items)
            sections.append(alias_section)
        
        # 4. Glossary terms (static)
        if self.glossary:
            terms_section = "## TERMS & ACRONYMS\n"
            terms_items = [f"- **{k}**: {v}" for k, v in list(self.glossary.items())]
            terms_section += "\n".join(terms_items)
            sections.append(terms_section)
        
        prefix = "\n\n".join(sections)
        
        # Generate hash for cache verification
        prefix_hash = hashlib.md5(prefix.encode()).hexdigest()[:8]
        
        return prefix, prefix_hash
    
    def get_dynamic_suffix(self) -> str:
        """Get the dynamic (per-call) portion of the prompt.
        
        This includes content-specific READMEs that vary per extraction.
        """
        if not self.relevant_readmes:
            return ""
        
        lines = ["## RELEVANT ENTITY CONTEXT"]
        for name, summary in self.relevant_readmes.items():
            lines.append(f"\n### {name}\n{summary}")
        
        return "\n".join(lines)

    def get_extraction_context(self, compact: bool = True, verbose: bool = False) -> str:
        """Format context for injection into extraction prompt.
        
        Args:
            compact: If True, use compact format for token efficiency
            verbose: If True, log cache info
        
        Returns:
            Formatted context string
        """
        # Get cacheable prefix and dynamic suffix
        prefix, prefix_hash = self.get_cacheable_prefix()
        suffix = self.get_dynamic_suffix()
        
        if verbose:
            prefix_tokens = len(prefix) // 4  # Rough estimate
            suffix_tokens = len(suffix) // 4
            print(f"  Context: prefix={prefix_tokens} tokens (hash:{prefix_hash}), suffix={suffix_tokens} tokens")
            if prefix_tokens >= 1024:
                print("  ✓ Prefix eligible for caching (>= 1024 tokens)")
            else:
                print("  ⚠ Prefix too short for caching (< 1024 tokens)")
        
        # Combine: cacheable prefix first, then dynamic suffix
        if suffix:
            return f"{prefix}\n\n{suffix}"
        return prefix
    
    def _format_compact_glossary(self) -> str:
        """Format glossary in compact form for token efficiency.
        
        Includes relationship info when available to help the LLM:
        - Understand urgency (manager email > random contact)
        - Assign task owners appropriately
        - Craft appropriate tone
        """
        lines = []
        
        # People - include relationship if available
        if self.people_manifest:
            lines.append("**Known People:**")
            # Extract names with relationships from manifest table
            people_info = self._extract_people_with_relationships(self.people_manifest)
            if people_info:
                # Format: "Name (relationship)" or just "Name" if no relationship
                formatted = [
                    f"{name} ({rel})" if rel else name 
                    for name, rel in people_info[:80]
                ]
                lines.append(", ".join(formatted))
            lines.append("")
        
        # Companies - include my_role if available
        if self.company_manifest:
            lines.append("**Known Companies:**")
            company_info = self._extract_companies_with_roles(self.company_manifest)
            if company_info:
                formatted = [
                    f"{name} [{role}]" if role else name
                    for name, role in company_info[:40]
                ]
                lines.append(", ".join(formatted))
            lines.append("")
        
        # Projects (just names for now, could add my_role later)
        if self.project_list:
            lines.append("**Known Projects:**")
            lines.append(", ".join(self.project_list[:50]))
            lines.append("")
        
        # Aliases
        if self.aliases:
            lines.append("**Name Aliases:**")
            alias_items = [f"{k} → {v}" for k, v in list(self.aliases.items())[:30]]
            lines.append(", ".join(alias_items))
        
        return "\n".join(lines)
    
    def _extract_people_with_relationships(self, manifest: str) -> list[tuple[str, str]]:
        """Extract people names and their relationship to me from manifest table."""
        import re
        results = []
        
        # Parse manifest table - find column indices first
        lines = manifest.split('\n')
        header_idx = -1
        rel_col_idx = -1
        
        for i, line in enumerate(lines):
            if '| Name |' in line:
                # Parse header to find My Relationship column
                headers = [h.strip() for h in line.split('|')]
                for j, h in enumerate(headers):
                    if 'My Relationship' in h:
                        rel_col_idx = j
                header_idx = i
                break
        
        if header_idx < 0:
            # Fallback to just names
            for match in re.finditer(r"\|\s*([^|\[]+)\s*\|", manifest):
                name = match.group(1).strip()
                if name and name not in ["Name", "---", ""]:
                    results.append((name, ""))
            return results[:80]
        
        # Parse data rows
        for line in lines[header_idx + 2:]:  # Skip header and separator
            if not line.strip() or not line.startswith('|'):
                continue
            cols = [c.strip() for c in line.split('|')]
            if len(cols) < 2:
                continue
            
            name = cols[1].strip()  # First data column is Name
            rel = ""
            if rel_col_idx > 0 and rel_col_idx < len(cols):
                rel = cols[rel_col_idx].strip()
            
            if name and name not in ["Name", "---"]:
                results.append((name, rel))
        
        return results
    
    def _extract_companies_with_roles(self, manifest: str) -> list[tuple[str, str]]:
        """Extract company names and my role from manifest table."""
        import re
        results = []
        
        lines = manifest.split('\n')
        header_idx = -1
        role_col_idx = -1
        stage_col_idx = -1
        type_col_idx = -1
        
        for i, line in enumerate(lines):
            if '| Name |' in line:
                headers = [h.strip() for h in line.split('|')]
                for j, h in enumerate(headers):
                    if 'My Role' in h:
                        role_col_idx = j
                    if 'Stage' in h:
                        stage_col_idx = j
                    if 'Type' in h:
                        type_col_idx = j
                header_idx = i
                break
        
        if header_idx < 0:
            return results
        
        for line in lines[header_idx + 2:]:
            if not line.strip() or not line.startswith('|'):
                continue
            cols = [c.strip() for c in line.split('|')]
            if len(cols) < 2:
                continue
            
            name = cols[1].strip()
            role = ""
            stage = ""
            account_type = ""
            if role_col_idx > 0 and role_col_idx < len(cols):
                role = cols[role_col_idx].strip()
            if stage_col_idx > 0 and stage_col_idx < len(cols):
                stage = cols[stage_col_idx].strip()
            if type_col_idx > 0 and type_col_idx < len(cols):
                account_type = cols[type_col_idx].strip()
            
            display_role = role or stage or account_type
            
            if name and name not in ["Name", "---"]:
                results.append((name, display_role))
        
        return results
    
    def _format_full_glossary(self) -> str:
        """Format full glossary with details."""
        return self.people_manifest + "\n" + self.company_manifest
    
    def _extract_names_from_manifest(self, manifest: str) -> list[str]:
        """Extract entity names from manifest table."""
        import re
        names = []
        
        # Match table rows: | Name | ... |
        for match in re.finditer(r"\|\s*\[\[([^\]|]+)", manifest):
            name = match.group(1).strip()
            if name and name not in ["Name", "---"]:
                names.append(name)
        
        return names


# =============================================================================
# LOADERS
# =============================================================================

def _load_persona(vault_root: Path, resources_paths: dict) -> str:
    """Load persona from prompts/persona.md."""
    prompts_root = Path(resources_paths.get("prompts", vault_root / "Workflow" / "prompts"))
    persona_path = prompts_root / "persona.md"
    if persona_path.exists():
        return persona_path.read_text()
    return ""


def _load_manifest(manifest_path: Path) -> str:
    """Load entity manifest file."""
    if manifest_path.exists():
        return manifest_path.read_text()
    return ""


def _list_projects(project_paths: list[Path]) -> list[str]:
    """List all project folder names."""
    names: list[str] = []
    for projects_dir in project_paths:
        if not projects_dir.exists():
            continue
        names.extend(
            folder.name for folder in projects_dir.iterdir()
            if folder.is_dir() and not folder.name.startswith("_")
        )
    return names


def _load_glossary(vault_root: Path, resources_paths: dict) -> dict[str, str]:
    """Load glossary of terms and acronyms."""
    glossary_root = Path(resources_paths.get("entities", vault_root / "Workflow" / "entities"))
    glossary_path = glossary_root / "glossary.yaml"
    if not glossary_path.exists():
        return {}
    
    try:
        import yaml
        return yaml.safe_load(glossary_path.read_text()) or {}
    except Exception:
        return {}


@lru_cache(maxsize=1)
def _load_aliases_cached(aliases_path: str) -> dict[str, str]:
    """Load aliases with caching."""
    path = Path(aliases_path)
    if not path.exists():
        return {}
    
    try:
        import yaml
        data = yaml.safe_load(path.read_text()) or {}
        
        # Flatten nested structure
        aliases = {}
        for canonical, variants in data.items():
            aliases[canonical.lower()] = canonical
            if isinstance(variants, list):
                for variant in variants:
                    aliases[variant.lower()] = canonical
            elif isinstance(variants, str):
                aliases[variants.lower()] = canonical
        
        return aliases
    except Exception:
        return {}


def _load_aliases(vault_root: Path, resources_paths: dict) -> dict[str, str]:
    """Load name aliases."""
    aliases_root = Path(resources_paths.get("entities", vault_root / "Workflow" / "entities"))
    aliases_path = aliases_root / "aliases.yaml"
    return _load_aliases_cached(str(aliases_path))


def _extract_aliases_from_manifest(manifest: str) -> dict[str, str]:
    """Extract aliases from People manifest Aliases column.
    
    The Aliases column contains semicolon-separated nicknames/variants.
    Returns a dict mapping each alias (lowercase) to the canonical name.
    
    Example row:
        | Jeff Denworth | ... | Jeff; JD; Jeff D | ... |
    Returns:
        {"jeff": "Jeff Denworth", "jd": "Jeff Denworth", "jeff d": "Jeff Denworth"}
    """
    import re
    aliases = {}
    
    lines = manifest.split('\n')
    header_idx = -1
    alias_col_idx = -1
    
    # Find header and Aliases column index
    for i, line in enumerate(lines):
        if '| Name |' in line:
            headers = [h.strip() for h in line.split('|')]
            for j, h in enumerate(headers):
                if h == 'Aliases':
                    alias_col_idx = j
            header_idx = i
            break
    
    if header_idx < 0 or alias_col_idx < 0:
        return aliases
    
    # Parse data rows
    for line in lines[header_idx + 2:]:  # Skip header and separator
        if not line.strip() or not line.startswith('|'):
            continue
        cols = [c.strip() for c in line.split('|')]
        if len(cols) < alias_col_idx + 1:
            continue
        
        name = cols[1].strip()  # First data column is Name
        alias_str = cols[alias_col_idx].strip() if alias_col_idx < len(cols) else ""
        
        if name and alias_str and name not in ["Name", "---"]:
            # Parse semicolon-separated aliases
            for alias in alias_str.split(';'):
                alias = alias.strip()
                if alias and alias.lower() != name.lower():
                    aliases[alias.lower()] = name
    
    return aliases


def _extract_acronyms_from_manifest(manifest: str) -> dict[str, str]:
    """Extract acronyms and definitions from Projects manifest.
    
    The Projects manifest has Acronym and Definition columns.
    Returns a dict mapping each acronym to its full name/definition.
    
    Example row:
        | Microsoft AI Infrastructure | ... | MAI | Microsoft's AI compute infra | ... |
    Returns:
        {"MAI": {"full_name": "Microsoft AI Infrastructure", "definition": "Microsoft's AI compute infra"}}
    """
    acronyms = {}
    
    lines = manifest.split('\n')
    header_idx = -1
    acronym_col_idx = -1
    definition_col_idx = -1
    
    # Find header and column indices
    for i, line in enumerate(lines):
        if '| Name |' in line:
            headers = [h.strip() for h in line.split('|')]
            for j, h in enumerate(headers):
                if h == 'Acronym':
                    acronym_col_idx = j
                if h == 'Definition':
                    definition_col_idx = j
            header_idx = i
            break
    
    if header_idx < 0:
        return acronyms
    
    # Parse data rows
    for line in lines[header_idx + 2:]:
        if not line.strip() or not line.startswith('|'):
            continue
        cols = [c.strip() for c in line.split('|')]
        if len(cols) < 2:
            continue
        
        name = cols[1].strip()
        acronym = cols[acronym_col_idx].strip() if acronym_col_idx > 0 and acronym_col_idx < len(cols) else ""
        definition = cols[definition_col_idx].strip() if definition_col_idx > 0 and definition_col_idx < len(cols) else ""
        
        if acronym and name not in ["Name", "---"]:
            # Handle multiple acronyms separated by semicolons
            for acr in acronym.split(';'):
                acr = acr.strip()
                if acr:
                    acronyms[acr] = {
                        "full_name": name,
                        "definition": definition
                    }
    
    return acronyms


def _extract_candidate_names(content: str) -> list[str]:
    """Extract likely proper names from free text."""
    import re
    if not content:
        return []
    
    candidates = re.findall(r"\b[A-Z][a-zA-Z\.]+ [A-Z][a-zA-Z\.]+\b", content)
    # Preserve order but dedupe
    seen = set()
    ordered = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            ordered.append(c)
    return ordered[:10]


def _quick_entity_scan(content: str, context: "ContextBundle") -> list[str]:
    """Quick scan for entity mentions in content.
    
    Returns list of entity names that appear in the content.
    """
    import re
    mentioned = []
    content_lower = content.lower()
    
    # Check known people
    people_names = context._extract_names_from_manifest(context.people_manifest)
    for name in people_names:
        canonical = context.aliases.get(name.lower(), name)
        if name.lower() in content_lower or canonical.lower() in content_lower:
            mentioned.append(canonical)
    
    # Check known companies
    company_names = context._extract_names_from_manifest(context.company_manifest)
    for name in company_names:
        canonical = context.aliases.get(name.lower(), name)
        if name.lower() in content_lower or canonical.lower() in content_lower:
            mentioned.append(canonical)
    
    # Check projects
    for project in context.project_list:
        if project.lower() in content_lower:
            mentioned.append(project)
    
    return mentioned[:20]  # Limit for token efficiency


def _load_entity_readmes(entities: list[str], vault_root: Path, entity_index: Optional[EntityIndex] = None) -> dict[str, str]:
    """Load README summaries for mentioned entities."""
    readmes = {}
    
    for entity in entities:
        readme = _find_entity_readme(entity, vault_root, entity_index)
        if readme:
            summary = _summarize_readme(readme)
            if summary:
                readmes[readme.parent.name] = summary
    
    return readmes


def _find_entity_readme(entity: str, vault_root: Path, entity_index: Optional[EntityIndex] = None) -> Optional[Path]:
    """Find README for an entity by name."""
    if entity_index:
        folder = (
            entity_index.find_person(entity)
            or entity_index.find_company(entity)
            or entity_index.find_project(entity)
        )
        if not folder:
            for search in (
                entity_index.search_person,
                entity_index.search_company,
                entity_index.search_project,
            ):
                hits = search(entity, limit=1)
                if hits:
                    folder = hits[0]
                    break
        if folder:
            readme_path = folder / "README.md"
            if readme_path.exists():
                return readme_path
    
    # Try People
    people_path = vault_root / "VAST" / "People" / entity / "README.md"
    if people_path.exists():
        return people_path
    
    # Try Customers
    customers_path = vault_root / "VAST" / "Customers and Partners" / entity / "README.md"
    if customers_path.exists():
        return customers_path
    
    # Try Projects
    projects_path = vault_root / "VAST" / "Projects" / entity / "README.md"
    if projects_path.exists():
        return projects_path
    
    return None


def _summarize_readme(readme_path: Path) -> str:
    """Extract key summary from README."""
    try:
        content = readme_path.read_text()
        
        # Extract frontmatter info
        summary_parts = []
        
        import re
        
        # Get role/title
        role_match = re.search(r"Role.*?:\s*(.+)", content)
        if role_match:
            summary_parts.append(f"Role: {role_match.group(1).strip()}")
        
        # Get company
        company_match = re.search(r"Company.*?:\s*(.+)", content)
        if company_match:
            summary_parts.append(f"Company: {company_match.group(1).strip()}")
        
        # Get key facts (first 3)
        facts_match = re.search(r"## Key Facts\s*\n((?:- .+\n?)+)", content)
        if facts_match:
            facts = facts_match.group(1).strip().split("\n")[:3]
            summary_parts.append("Key Facts: " + "; ".join(f.strip("- ") for f in facts))
        
        return "\n".join(summary_parts) if summary_parts else ""
        
    except Exception:
        return ""

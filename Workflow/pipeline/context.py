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
from typing import Optional, Tuple
from functools import lru_cache
from pydantic import BaseModel, Field, ConfigDict

sys.path.insert(0, str(Path(__file__).parent.parent))

from .envelope import ContentEnvelope
from .entities import EntityIndex

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
    project_list: list[str] = Field(default_factory=list)
    glossary: dict[str, str] = Field(default_factory=dict)
    aliases: dict[str, str] = Field(default_factory=dict)
    
    # Dynamic context (per content item)
    relevant_readmes: dict[str, str] = Field(default_factory=dict)
    
    @classmethod
    def load(cls, vault_root: Path, envelope: Optional[ContentEnvelope] = None, entity_index: Optional[EntityIndex] = None) -> "ContextBundle":
        """Load context for extraction.
        
        Args:
            vault_root: Path to vault root
            envelope: Optional ContentEnvelope to load relevant READMEs for
        
        Returns:
            ContextBundle with all context loaded
        """
        bundle = cls()
        index = entity_index or EntityIndex(vault_root)
        
        # Load static context
        bundle.persona = _load_persona(vault_root)
        bundle.people_manifest = _load_manifest(vault_root / "VAST" / "People" / "_MANIFEST.md")
        bundle.company_manifest = _load_manifest(vault_root / "VAST" / "Customers and Partners" / "_MANIFEST.md")
        bundle.project_list = _list_projects(vault_root)
        bundle.glossary = _load_glossary(vault_root)
        bundle.aliases = _load_aliases(vault_root)
        
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
        
        for i, line in enumerate(lines):
            if '| Name |' in line:
                headers = [h.strip() for h in line.split('|')]
                for j, h in enumerate(headers):
                    if 'My Role' in h:
                        role_col_idx = j
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
            if role_col_idx > 0 and role_col_idx < len(cols):
                role = cols[role_col_idx].strip()
            
            if name and name not in ["Name", "---"]:
                results.append((name, role))
        
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

def _load_persona(vault_root: Path) -> str:
    """Load persona from prompts/persona.md."""
    persona_path = vault_root / "Workflow" / "prompts" / "persona.md"
    if persona_path.exists():
        return persona_path.read_text()
    return ""


def _load_manifest(manifest_path: Path) -> str:
    """Load entity manifest file."""
    if manifest_path.exists():
        return manifest_path.read_text()
    return ""


def _list_projects(vault_root: Path) -> list[str]:
    """List all project folder names."""
    projects_dir = vault_root / "VAST" / "Projects"
    if not projects_dir.exists():
        return []
    
    return [
        folder.name for folder in projects_dir.iterdir()
        if folder.is_dir() and not folder.name.startswith("_")
    ]


def _load_glossary(vault_root: Path) -> dict[str, str]:
    """Load glossary of terms and acronyms."""
    glossary_path = vault_root / "Workflow" / "entities" / "glossary.yaml"
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


def _load_aliases(vault_root: Path) -> dict[str, str]:
    """Load name aliases."""
    aliases_path = vault_root / "Workflow" / "entities" / "aliases.yaml"
    return _load_aliases_cached(str(aliases_path))


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

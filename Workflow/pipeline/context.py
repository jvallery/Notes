"""
Context Bundle - Load context for extraction and output generation.

The ContextBundle provides:
- Persona (my role, priorities, communication style)
- Entity manifests (compact lists of known people/companies/projects)
- Glossary (acronyms, terms)
- Aliases (name normalization)
- Relevant entity READMEs (for entities mentioned in content)
"""

import sys
from pathlib import Path
from typing import Optional
from functools import lru_cache
from pydantic import BaseModel, Field, ConfigDict

sys.path.insert(0, str(Path(__file__).parent.parent))

from .envelope import ContentEnvelope


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
    def load(cls, vault_root: Path, envelope: Optional[ContentEnvelope] = None) -> "ContextBundle":
        """Load context for extraction.
        
        Args:
            vault_root: Path to vault root
            envelope: Optional ContentEnvelope to load relevant READMEs for
        
        Returns:
            ContextBundle with all context loaded
        """
        bundle = cls()
        
        # Load static context
        bundle.persona = _load_persona(vault_root)
        bundle.people_manifest = _load_manifest(vault_root / "VAST" / "People" / "_MANIFEST.md")
        bundle.company_manifest = _load_manifest(vault_root / "VAST" / "Customers and Partners" / "_MANIFEST.md")
        bundle.project_list = _list_projects(vault_root)
        bundle.glossary = _load_glossary(vault_root)
        bundle.aliases = _load_aliases(vault_root)
        
        # Load dynamic context if envelope provided
        if envelope:
            mentioned = _quick_entity_scan(envelope.raw_content, bundle)
            bundle.relevant_readmes = _load_entity_readmes(mentioned, vault_root)
        
        return bundle
    
    def get_extraction_context(self, compact: bool = True) -> str:
        """Format context for injection into extraction prompt.
        
        Args:
            compact: If True, use compact format for token efficiency
        
        Returns:
            Formatted context string
        """
        sections = []
        
        # Persona (always include if available)
        if self.persona:
            sections.append(f"## PERSONA\n{self.persona}")
        
        # Entity glossary
        if compact:
            glossary = self._format_compact_glossary()
        else:
            glossary = self._format_full_glossary()
        
        if glossary:
            sections.append(f"## ENTITY GLOSSARY\n{glossary}")
        
        # Relevant READMEs (for mentioned entities)
        if self.relevant_readmes:
            readme_section = "## RELEVANT ENTITIES\n"
            for name, summary in self.relevant_readmes.items():
                readme_section += f"\n### {name}\n{summary}\n"
            sections.append(readme_section)
        
        return "\n\n".join(sections)
    
    def _format_compact_glossary(self) -> str:
        """Format glossary in compact form for token efficiency."""
        lines = []
        
        # People (just names)
        if self.people_manifest:
            lines.append("**Known People:**")
            # Extract just names from manifest table
            names = self._extract_names_from_manifest(self.people_manifest)
            if names:
                lines.append(", ".join(names[:100]))  # Limit for tokens
            lines.append("")
        
        # Companies (just names)
        if self.company_manifest:
            lines.append("**Known Companies:**")
            names = self._extract_names_from_manifest(self.company_manifest)
            if names:
                lines.append(", ".join(names[:50]))
            lines.append("")
        
        # Projects (just names)
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
        if name.lower() in content_lower:
            mentioned.append(name)
    
    # Check known companies
    company_names = context._extract_names_from_manifest(context.company_manifest)
    for name in company_names:
        if name.lower() in content_lower:
            mentioned.append(name)
    
    # Check projects
    for project in context.project_list:
        if project.lower() in content_lower:
            mentioned.append(project)
    
    return mentioned[:20]  # Limit for token efficiency


def _load_entity_readmes(entities: list[str], vault_root: Path) -> dict[str, str]:
    """Load README summaries for mentioned entities."""
    readmes = {}
    
    for entity in entities:
        readme = _find_entity_readme(entity, vault_root)
        if readme:
            summary = _summarize_readme(readme)
            if summary:
                readmes[entity] = summary
    
    return readmes


def _find_entity_readme(entity: str, vault_root: Path) -> Optional[Path]:
    """Find README for an entity by name."""
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

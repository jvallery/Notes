"""
Entity Index - Centralized entity lookup and management.

Provides fast lookups by:
- Email address (primary key for people)
- Full name (exact and partial matching)
- Company name
- Project name

This replaces the duplicated index-building code in ingest_emails.py and ingest_transcripts.py.
"""

import sys
from difflib import get_close_matches
from pathlib import Path
from typing import Optional, Tuple
from functools import lru_cache

sys.path.insert(0, str(Path(__file__).parent.parent))


class EntityIndex:
    """Centralized entity index for fast lookups.
    
    Caches indices on first use, rebuilds if vault changes.
    """
    
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self._email_index: Optional[dict[str, Path]] = None
        self._name_index: Optional[dict[str, Path]] = None
        self._company_index: Optional[dict[str, Path]] = None
        self._project_index: Optional[dict[str, Path]] = None
        self._aliases: Optional[dict[str, str]] = None
        self._search_cache: dict[tuple[str, str], list[Path]] = {}
    
    def find_person(self, name: str, email: Optional[str] = None) -> Optional[Path]:
        """Find existing person folder.
        
        Lookup order:
        1. Exact email match (if email provided)
        2. Alias resolution (name → canonical name)
        3. Exact name match
        4. Partial name match (first AND last name must match)
        
        Args:
            name: Person's name to search for
            email: Optional email address (preferred lookup key)
        
        Returns:
            Path to person folder, or None if not found
        """
        self._ensure_indices()
        
        # 1. Email match (highest priority)
        if email:
            email_lower = email.strip().lower()
            if email_lower in self._email_index:
                return self._email_index[email_lower]
        
        # 2. Normalize name via aliases
        normalized = self.normalize_name(name)
        
        # 3. Exact name match
        name_lower = normalized.lower()
        if name_lower in self._name_index:
            return self._name_index[name_lower]
        
        # 4. Partial match (first AND last name must match)
        name_parts = name_lower.split()
        if len(name_parts) >= 2:
            for folder_name, folder_path in self._name_index.items():
                folder_parts = folder_name.split()
                if len(folder_parts) >= 2:
                    first_initial = name_parts[0].strip(".")
                    if name_parts[0] == folder_parts[0] and name_parts[-1] == folder_parts[-1]:
                        return folder_path
                    if first_initial and first_initial[0] == folder_parts[0][0] and name_parts[-1] == folder_parts[-1]:
                        return folder_path
        
        # Fuzzy match fallback
        fuzzy = self.search_person(name, limit=1, cutoff=0.82)
        if fuzzy:
            return fuzzy[0]
        
        return None
    
    def find_company(self, company: str) -> Optional[Path]:
        """Find existing company/customer folder.
        
        Args:
            company: Company name to search for
        
        Returns:
            Path to company folder, or None if not found
        """
        self._ensure_indices()
        
        company_lower = company.lower().strip()
        
        # Exact match
        if company_lower in self._company_index:
            return self._company_index[company_lower]
        
        # Partial match
        for folder_name, folder_path in self._company_index.items():
            if company_lower in folder_name or folder_name in company_lower:
                return folder_path
        
        # Fuzzy match fallback
        fuzzy = self.search_company(company, limit=1, cutoff=0.78)
        if fuzzy:
            return fuzzy[0]
        
        return None
    
    def find_project(self, project: str) -> Optional[Path]:
        """Find existing project folder.
        
        Args:
            project: Project name to search for
        
        Returns:
            Path to project folder, or None if not found
        """
        self._ensure_indices()
        
        project_lower = project.lower().strip()
        
        # Exact match
        if project_lower in self._project_index:
            return self._project_index[project_lower]
        
        # Partial match
        for folder_name, folder_path in self._project_index.items():
            if project_lower in folder_name or folder_name in project_lower:
                return folder_path
        
        # Fuzzy match fallback
        fuzzy = self.search_project(project, limit=1)
        if fuzzy:
            return fuzzy[0]
        
        return None
    
    def search_person(self, name: str, limit: int = 3, cutoff: float = 0.72) -> list[Path]:
        """Fuzzy search for a person by name."""
        self._ensure_indices()
        normalized = self.normalize_name(name)
        cache_key = ("person", normalized.lower())
        if cache_key in self._search_cache:
            return self._search_cache[cache_key]
        
        if normalized.lower() in self._name_index:
            match = [self._name_index[normalized.lower()]]
            self._search_cache[cache_key] = match
            return match
        
        matches = self._fuzzy_match(normalized, list(self._name_index.keys()), limit, cutoff)
        paths = [self._name_index[m] for m in matches]
        self._search_cache[cache_key] = paths
        return paths
    
    def search_company(self, company: str, limit: int = 3, cutoff: float = 0.7) -> list[Path]:
        """Fuzzy search for a company by name."""
        self._ensure_indices()
        cache_key = ("company", company.lower().strip())
        if cache_key in self._search_cache:
            return self._search_cache[cache_key]
        
        matches = self._fuzzy_match(company, list(self._company_index.keys()), limit, cutoff)
        paths = [self._company_index[m] for m in matches]
        self._search_cache[cache_key] = paths
        return paths
    
    def search_project(self, project: str, limit: int = 3, cutoff: float = 0.65) -> list[Path]:
        """Fuzzy search for a project by name."""
        self._ensure_indices()
        cache_key = ("project", project.lower().strip())
        if cache_key in self._search_cache:
            return self._search_cache[cache_key]
        
        matches = self._fuzzy_match(project, list(self._project_index.keys()), limit, cutoff)
        paths = [self._project_index[m] for m in matches]
        self._search_cache[cache_key] = paths
        return paths
    
    def find_similar_people(self, name: str, limit: int = 2, cutoff: float = 0.82) -> list[str]:
        """Return similar people names for duplicate detection."""
        self._ensure_indices()
        normalized = self.normalize_name(name).lower()
        matches = [
            m for m in self._fuzzy_match(normalized, list(self._name_index.keys()), limit + 1, cutoff)
            if m != normalized
        ]
        return [self._name_index[m].name for m in matches[:limit]]
    
    def find_similar_companies(self, name: str, limit: int = 2, cutoff: float = 0.8) -> list[str]:
        """Return similar company names for duplicate detection."""
        self._ensure_indices()
        name_lower = name.lower().strip()
        matches = [
            m for m in self._fuzzy_match(name_lower, list(self._company_index.keys()), limit + 1, cutoff)
            if m != name_lower
        ]
        return [self._company_index[m].name for m in matches[:limit]]
    
    def find_similar_projects(self, name: str, limit: int = 2, cutoff: float = 0.8) -> list[str]:
        """Return similar project names for duplicate detection."""
        self._ensure_indices()
        name_lower = name.lower().strip()
        matches = [
            m for m in self._fuzzy_match(name_lower, list(self._project_index.keys()), limit + 1, cutoff)
            if m != name_lower
        ]
        return [self._project_index[m].name for m in matches[:limit]]
    
    def normalize_name(self, name: str) -> str:
        """Normalize a name using aliases.
        
        Args:
            name: Name to normalize
        
        Returns:
            Canonical name if alias exists, otherwise original
        """
        self._ensure_aliases()
        
        name_lower = name.lower().strip()
        return self._aliases.get(name_lower, name)
    
    def list_people(self) -> list[str]:
        """List all known people names."""
        self._ensure_indices()
        return list(self._name_index.keys())
    
    def list_companies(self) -> list[str]:
        """List all known company names."""
        self._ensure_indices()
        return list(self._company_index.keys())
    
    def list_projects(self) -> list[str]:
        """List all known project names."""
        self._ensure_indices()
        return list(self._project_index.keys())
    
    def invalidate(self):
        """Invalidate cached indices (call after creating entities)."""
        self._email_index = None
        self._name_index = None
        self._company_index = None
        self._project_index = None
        self._search_cache = {}
    
    # =========================================================================
    # PRIVATE METHODS
    # =========================================================================
    def _fuzzy_match(self, query: str, choices: list[str], limit: int, cutoff: float) -> list[str]:
        """Return close matches using difflib for lightweight fuzzy search."""
        if not query or not choices:
            return []
        normalized = " ".join(query.lower().replace(".", " ").split())
        choice_map = {" ".join(c.split()): c for c in choices}
        matches = get_close_matches(normalized, list(choice_map.keys()), n=limit, cutoff=cutoff)
        return [choice_map[m] for m in matches]
    
    def _ensure_indices(self):
        """Build indices if not already cached."""
        if self._email_index is None:
            self._build_person_index()
        if self._company_index is None:
            self._build_company_index()
        if self._project_index is None:
            self._build_project_index()
    
    def _ensure_aliases(self):
        """Load aliases if not already cached."""
        if self._aliases is None:
            self._load_aliases()
    
    def _build_person_index(self):
        """Build email and name indices for people."""
        from scripts.utils.frontmatter import parse_frontmatter
        
        self._email_index = {}
        self._name_index = {}
        
        people_dirs = [
            self.vault_root / "VAST" / "People",
            self.vault_root / "Personal" / "People"
        ]
        
        for people_dir in people_dirs:
            if not people_dir.exists():
                continue
            
            for folder in people_dir.iterdir():
                if not folder.is_dir() or folder.name.startswith("_"):
                    continue
                
                readme = folder / "README.md"
                if not readme.exists():
                    continue
                
                # Index by folder name
                self._name_index[folder.name.lower()] = folder
                
                # Parse frontmatter for email
                try:
                    content = readme.read_text()
                    fm, _ = parse_frontmatter(content)
                    if fm and fm.get("email"):
                        email = fm["email"].strip().lower()
                        if email and email != "''":
                            self._email_index[email] = folder
                except Exception:
                    pass
    
    def _build_company_index(self):
        """Build index for companies/customers."""
        self._company_index = {}
        
        customers_dir = self.vault_root / "VAST" / "Customers and Partners"
        if not customers_dir.exists():
            return
        
        for folder in customers_dir.iterdir():
            if folder.is_dir() and not folder.name.startswith("_"):
                self._company_index[folder.name.lower()] = folder
    
    def _build_project_index(self):
        """Build index for projects."""
        self._project_index = {}
        
        projects_dir = self.vault_root / "VAST" / "Projects"
        if not projects_dir.exists():
            return
        
        for folder in projects_dir.iterdir():
            if folder.is_dir() and not folder.name.startswith("_"):
                self._project_index[folder.name.lower()] = folder
    
    def _load_aliases(self):
        """Load name aliases from YAML file."""
        import yaml
        
        self._aliases = {}
        aliases_path = self.vault_root / "Workflow" / "entities" / "aliases.yaml"
        
        if not aliases_path.exists():
            return
        
        try:
            data = yaml.safe_load(aliases_path.read_text()) or {}
            
            # Flatten nested structure
            for canonical, variants in data.items():
                self._aliases[canonical.lower()] = canonical
                if isinstance(variants, list):
                    for variant in variants:
                        self._aliases[variant.lower()] = canonical
                elif isinstance(variants, str):
                    self._aliases[variants.lower()] = canonical
        except Exception:
            pass


# Singleton pattern for module-level access
_entity_index: Optional[EntityIndex] = None


def get_entity_index(vault_root: Optional[Path] = None) -> EntityIndex:
    """Get or create the entity index singleton.
    
    Args:
        vault_root: Vault root path. Required on first call.
    
    Returns:
        EntityIndex instance
    """
    global _entity_index
    
    if _entity_index is None:
        if vault_root is None:
            # Try to get from utils
            from scripts.utils import vault_root as get_vault_root
            vault_root = get_vault_root()
        _entity_index = EntityIndex(vault_root)
    
    return _entity_index

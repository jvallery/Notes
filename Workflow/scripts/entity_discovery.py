#!/usr/bin/env python3
"""
Entity Discovery Service

Unified service for discovering, classifying, and enriching entities across all
ingestion flows (email, transcript, document).

Uses OpenAI web search to:
1. Classify entity type (person, company, project, unknown)
2. Gather enrichment data (role, company, industry, etc.)
3. Determine correct vault destination

Usage:
    from entity_discovery import discover_entity, EntityType
    
    result = discover_entity("Tesla", context="email about credits expiring", client=openai_client)
    # Returns: EntityDiscovery(entity_type=EntityType.COMPANY, name="Tesla, Inc.", ...)
"""

import json
import os
import sys
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, Field

sys.path.insert(0, str(Path(__file__).parent))
from utils import vault_root, workflow_root


class EntityType(str, Enum):
    """Classification of entity types in the vault."""
    PERSON = "person"
    COMPANY = "company"
    PROJECT = "project"
    UNKNOWN = "unknown"


class EntityDiscovery(BaseModel):
    """Result of entity discovery and classification."""
    
    # Classification
    original_name: str = Field(description="The original name as provided")
    entity_type: EntityType = Field(description="Classified type of entity")
    confidence: float = Field(description="Confidence in classification (0-1)")
    
    # Enrichment
    canonical_name: str = Field(description="Proper/full name of entity")
    description: Optional[str] = Field(default=None, description="Brief description")
    
    # Person-specific
    title: Optional[str] = Field(default=None, description="Job title if person")
    company: Optional[str] = Field(default=None, description="Company if person")
    linkedin_url: Optional[str] = Field(default=None, description="LinkedIn URL if found")
    
    # Company-specific
    industry: Optional[str] = Field(default=None, description="Industry if company")
    website: Optional[str] = Field(default=None, description="Website if company")
    company_type: Optional[str] = Field(default=None, description="Type: customer, partner, competitor")
    
    # Project-specific
    project_owner: Optional[str] = Field(default=None, description="Owner org if project")
    
    # Vault routing
    suggested_path: Optional[str] = Field(default=None, description="Suggested vault path")
    
    # Metadata
    sources: List[str] = Field(default_factory=list, description="Sources of information")
    discovered_at: str = Field(default_factory=lambda: datetime.now().isoformat())


class EntityClassificationRequest(BaseModel):
    """Request to classify an entity."""
    name: str
    context: Optional[str] = None
    source_type: Optional[str] = None  # email, transcript, document


# Known entities that don't need web search
KNOWN_COMPANIES = {
    "microsoft", "google", "amazon", "aws", "meta", "facebook", "apple",
    "nvidia", "openai", "anthropic", "tesla", "ibm", "dell", "hp", "hpe",
    "intel", "amd", "cisco", "oracle", "salesforce", "vmware", "netapp",
    "pure storage", "vast", "vast data", "coreweave", "lambda", "crusoe",
    "databricks", "snowflake", "walmart", "target", "costco", "kroger",
    "goldman sachs", "jpmorgan", "morgan stanley", "citadel", "blackrock",
    "nebius", "yandex", "alibaba", "tencent", "baidu", "samsung", "lg",
    # Add common customer/partner names
    "slice", "kodeon", "ey", "deloitte", "pwc", "kpmg", "accenture",
    "mckinsey", "bain", "bcg", "infosys", "tcs", "wipro", "cognizant"
}

# Known project indicators
PROJECT_INDICATORS = [
    "project", "initiative", "program", "mvp", "poc", "pilot",
    "implementation", "migration", "deployment", "rollout"
]

# Patterns that indicate a company vs person
COMPANY_SUFFIXES = [
    "inc", "inc.", "corp", "corp.", "corporation", "llc", "ltd", "ltd.",
    "limited", "co", "co.", "company", "group", "holdings", "partners",
    "technologies", "systems", "solutions", "services", "labs", "ai"
]


def _quick_classify(name: str, context: Optional[str] = None) -> Optional[EntityType]:
    """Quick classification without API call for obvious cases."""
    
    name_lower = name.lower().strip()
    
    # Check known companies (exact match)
    if name_lower in KNOWN_COMPANIES:
        return EntityType.COMPANY
    
    # Check if name starts with a known company name (e.g., "Slice Team" -> "slice")
    for company in KNOWN_COMPANIES:
        if name_lower.startswith(company + " ") or name_lower.startswith(company + ","):
            return EntityType.COMPANY
    
    # Check company suffixes
    for suffix in COMPANY_SUFFIXES:
        if name_lower.endswith(f" {suffix}") or name_lower.endswith(f", {suffix}"):
            return EntityType.COMPANY
    
    # Check project indicators in context
    if context:
        context_lower = context.lower()
        for indicator in PROJECT_INDICATORS:
            if indicator in context_lower and name_lower in context_lower:
                return EntityType.PROJECT
    
    # Check if it looks like a full person name (First Last pattern)
    parts = name.split()
    if len(parts) >= 2:
        # All parts are capitalized words, no company suffixes
        if all(p[0].isupper() and p[1:].islower() for p in parts if len(p) > 1):
            if not any(p.lower() in COMPANY_SUFFIXES for p in parts):
                return EntityType.PERSON
    
    return None


def _build_search_query(name: str, context: Optional[str] = None) -> str:
    """Build a search query to identify the entity."""
    
    query = f'"{name}"'
    
    if context:
        # Add context keywords
        context_keywords = []
        context_lower = context.lower()
        
        if "ceo" in context_lower or "founder" in context_lower or "executive" in context_lower:
            context_keywords.append("executive OR founder OR CEO")
        if "microsoft" in context_lower:
            context_keywords.append("Microsoft")
        if "google" in context_lower:
            context_keywords.append("Google")
        if "vast" in context_lower:
            context_keywords.append("VAST Data OR storage")
        
        if context_keywords:
            query += " " + " ".join(context_keywords[:2])
    
    return query


def discover_entity(
    name: str,
    context: Optional[str] = None,
    source_type: Optional[str] = None,
    client = None,
    use_cache: bool = True
) -> EntityDiscovery:
    """
    Discover and classify an entity using web search.
    
    Args:
        name: Name of the entity to classify
        context: Additional context (email subject, transcript snippet, etc.)
        source_type: Type of source (email, transcript, document)
        client: OpenAI client (will create if not provided)
        use_cache: Whether to use cached discoveries
    
    Returns:
        EntityDiscovery with classification and enrichment
    """
    
    # Try quick classification first
    quick_type = _quick_classify(name, context)
    if quick_type == EntityType.COMPANY:
        # Known company - return immediately with basic info
        return EntityDiscovery(
            original_name=name,
            entity_type=EntityType.COMPANY,
            confidence=0.95,
            canonical_name=name.title() if name.islower() else name,
            suggested_path=f"VAST/Customers and Partners/{name.title() if name.islower() else name}",
            sources=["known_entity_list"]
        )
    
    # Check cache
    cache_dir = workflow_root() / "_cache" / "entity_discovery"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    cache_key = name.lower().replace(" ", "_").replace("/", "_")[:50]
    cache_file = cache_dir / f"{cache_key}.json"
    
    if use_cache and cache_file.exists():
        try:
            cached = json.loads(cache_file.read_text())
            # Check if cache is recent (within 30 days)
            cached_at = datetime.fromisoformat(cached.get("discovered_at", "2000-01-01"))
            if (datetime.now() - cached_at).days < 30:
                return EntityDiscovery(**cached)
        except Exception:
            pass
    
    # Need to use OpenAI web search
    if client is None:
        from utils.ai_client import get_openai_client
        try:
            client = get_openai_client("entity_discovery")
        except ValueError:
            # Fall back to heuristic classification
            return _heuristic_classify(name, context)
    
    # Build search and classification prompt
    search_query = _build_search_query(name, context)
    
    system_prompt = """You are an entity classification assistant. Given a name and context, determine:
1. What type of entity this is (person, company, or project)
2. Key information about the entity

Return a JSON object with these fields:
{
    "entity_type": "person" | "company" | "project" | "unknown",
    "confidence": 0.0-1.0,
    "canonical_name": "Proper full name",
    "description": "Brief 1-2 sentence description",
    "title": "Job title if person, null otherwise",
    "company": "Employer if person, null otherwise", 
    "industry": "Industry if company, null otherwise",
    "website": "Website if company, null otherwise",
    "company_type": "customer" | "partner" | "competitor" | null,
    "reasoning": "Brief explanation of classification"
}

Key rules:
- Tesla, Microsoft, Google, OpenAI, etc. are COMPANIES, not people
- "Slice" (the pizza company) is a COMPANY
- kodeON is a COMPANY (coding platform)
- Names like "John Smith" with job titles are PEOPLE
- Internal initiatives like "Cloud Marketplace MVP" are PROJECTS
"""
    
    user_prompt = f"""Classify this entity:

Name: {name}
Context: {context or 'No additional context provided'}
Source type: {source_type or 'Unknown'}

Use web search if needed to identify this entity."""

    try:
        # Use chat completions with web search tool
        # Note: web_search_preview may not be available in all versions
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        
        # Parse the response
        response_text = response.choices[0].message.content
        
        # Extract JSON from response
        json_match = None
        if "```json" in response_text:
            start = response_text.find("```json") + 7
            end = response_text.find("```", start)
            json_match = response_text[start:end].strip()
        elif "{" in response_text:
            start = response_text.find("{")
            end = response_text.rfind("}") + 1
            json_match = response_text[start:end]
        
        if json_match:
            result = json.loads(json_match)
            
            # Map to EntityType
            entity_type_str = result.get("entity_type", "unknown").lower()
            entity_type = EntityType(entity_type_str) if entity_type_str in [e.value for e in EntityType] else EntityType.UNKNOWN
            
            # Build suggested path
            suggested_path = None
            canonical_name = result.get("canonical_name", name)
            
            if entity_type == EntityType.PERSON:
                suggested_path = f"VAST/People/{canonical_name}"
            elif entity_type == EntityType.COMPANY:
                suggested_path = f"VAST/Customers and Partners/{canonical_name}"
            elif entity_type == EntityType.PROJECT:
                suggested_path = f"VAST/Projects/{canonical_name}"
            
            discovery = EntityDiscovery(
                original_name=name,
                entity_type=entity_type,
                confidence=result.get("confidence", 0.8),
                canonical_name=canonical_name,
                description=result.get("description"),
                title=result.get("title"),
                company=result.get("company"),
                industry=result.get("industry"),
                website=result.get("website"),
                company_type=result.get("company_type"),
                suggested_path=suggested_path,
                sources=["openai_web_search"]
            )
            
            # Cache the result
            cache_file.write_text(discovery.model_dump_json(indent=2))
            
            return discovery
            
    except Exception as e:
        print(f"Web search failed for '{name}': {e}")
    
    # Fall back to heuristic
    return _heuristic_classify(name, context)


def _heuristic_classify(name: str, context: Optional[str] = None) -> EntityDiscovery:
    """Heuristic classification when API is unavailable."""
    
    quick_type = _quick_classify(name, context)
    
    if quick_type:
        entity_type = quick_type
        confidence = 0.7
    else:
        # Default based on name structure
        parts = name.split()
        if len(parts) >= 2 and len(parts) <= 4:
            entity_type = EntityType.PERSON
            confidence = 0.5
        else:
            entity_type = EntityType.UNKNOWN
            confidence = 0.3
    
    # Build suggested path
    suggested_path = None
    if entity_type == EntityType.PERSON:
        suggested_path = f"VAST/People/{name}"
    elif entity_type == EntityType.COMPANY:
        suggested_path = f"VAST/Customers and Partners/{name}"
    elif entity_type == EntityType.PROJECT:
        suggested_path = f"VAST/Projects/{name}"
    
    return EntityDiscovery(
        original_name=name,
        entity_type=entity_type,
        confidence=confidence,
        canonical_name=name,
        suggested_path=suggested_path,
        sources=["heuristic_classification"]
    )


def find_or_create_entity(
    name: str,
    context: Optional[str] = None,
    email: Optional[str] = None,
    client = None,
    dry_run: bool = False
) -> tuple[Path, EntityDiscovery]:
    """
    Find existing entity folder or create new one with proper classification.
    
    Returns:
        Tuple of (folder_path, discovery_result)
    """
    
    vault = vault_root()
    
    # First, check if entity already exists
    existing = _find_existing_entity(name, email)
    if existing:
        # Return existing with minimal discovery
        entity_type = _infer_type_from_path(existing)
        return existing, EntityDiscovery(
            original_name=name,
            entity_type=entity_type,
            confidence=1.0,
            canonical_name=existing.name,
            suggested_path=str(existing.relative_to(vault)),
            sources=["existing_entity"]
        )
    
    # Discover and classify
    discovery = discover_entity(name, context=context, client=client)
    
    # Create folder based on classification
    if discovery.suggested_path:
        folder_path = vault / discovery.suggested_path
    else:
        # Default to People with needs-review
        folder_path = vault / "VAST" / "People" / discovery.canonical_name
    
    if not dry_run:
        folder_path.mkdir(parents=True, exist_ok=True)
    
    return folder_path, discovery


def _find_existing_entity(name: str, email: Optional[str] = None) -> Optional[Path]:
    """Find existing entity by name or email."""
    
    vault = vault_root()
    name_lower = name.lower()
    
    # Search People
    people_dir = vault / "VAST" / "People"
    if people_dir.exists():
        for folder in people_dir.iterdir():
            if folder.is_dir():
                if folder.name.lower() == name_lower:
                    return folder
                # Check email in frontmatter
                if email:
                    readme = folder / "README.md"
                    if readme.exists():
                        content = readme.read_text()
                        if email.lower() in content.lower():
                            return folder
    
    # Search Customers
    customers_dir = vault / "VAST" / "Customers and Partners"
    if customers_dir.exists():
        for folder in customers_dir.iterdir():
            if folder.is_dir():
                if folder.name.lower() == name_lower or name_lower in folder.name.lower():
                    return folder
    
    # Search Projects
    projects_dir = vault / "VAST" / "Projects"
    if projects_dir.exists():
        for folder in projects_dir.iterdir():
            if folder.is_dir():
                if folder.name.lower() == name_lower or name_lower in folder.name.lower():
                    return folder
    
    return None


def _infer_type_from_path(path: Path) -> EntityType:
    """Infer entity type from vault path."""
    
    path_str = str(path).lower()
    
    if "/people/" in path_str:
        return EntityType.PERSON
    elif "/customers" in path_str or "/partners" in path_str:
        return EntityType.COMPANY
    elif "/projects/" in path_str:
        return EntityType.PROJECT
    else:
        return EntityType.UNKNOWN


# CLI for testing
if __name__ == "__main__":
    import click
    from rich.console import Console
    from rich.table import Table
    
    console = Console()
    
    @click.command()
    @click.argument("name")
    @click.option("--context", "-c", default=None, help="Additional context")
    @click.option("--no-cache", is_flag=True, help="Skip cache")
    def main(name: str, context: Optional[str], no_cache: bool):
        """Discover and classify an entity."""
        
        console.print(f"[bold]Discovering: {name}[/bold]")
        if context:
            console.print(f"[dim]Context: {context}[/dim]")
        
        result = discover_entity(name, context=context, use_cache=not no_cache)
        
        table = Table(title="Entity Discovery Result")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Original Name", result.original_name)
        table.add_row("Entity Type", result.entity_type.value)
        table.add_row("Confidence", f"{result.confidence:.0%}")
        table.add_row("Canonical Name", result.canonical_name)
        table.add_row("Description", result.description or "-")
        table.add_row("Suggested Path", result.suggested_path or "-")
        table.add_row("Sources", ", ".join(result.sources))
        
        if result.entity_type == EntityType.PERSON:
            table.add_row("Title", result.title or "-")
            table.add_row("Company", result.company or "-")
        elif result.entity_type == EntityType.COMPANY:
            table.add_row("Industry", result.industry or "-")
            table.add_row("Website", result.website or "-")
            table.add_row("Company Type", result.company_type or "-")
        
        console.print(table)
    
    main()

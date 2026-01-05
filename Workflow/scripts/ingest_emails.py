#!/usr/bin/env python3
"""
Email Ingest Pipeline: Extract → Plan → Apply

Extracts structured knowledge from emails and patches it back to the vault:

1. EXTRACT - Pull structured data from email (contacts, tasks, facts, context)
2. PLAN - Generate patches for vault (update People READMEs, add tasks, etc.)
3. APPLY - Execute patches (update files, create entities if needed)

This is the "knowledge capture" step that ensures emails update our knowledge base.

Usage:
    python scripts/ingest_emails.py                # Process all pending emails
    python scripts/ingest_emails.py --file X.md   # Process single email
    python scripts/ingest_emails.py --dry-run     # Show what would be changed
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Tuple

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_config, get_model_config, vault_root, workflow_root
from utils.patch_primitives import upsert_frontmatter, append_under_heading, ensure_wikilinks
from utils.frontmatter import parse_frontmatter, render_frontmatter
from models.email_extraction import (
    EmailExtraction, ContactInfo, TaskItem, KeyFact, 
    VaultPatch, EmailChangePlan
)


console = Console()


def get_openai_client():
    """Get configured OpenAI client with logging instrumentation."""
    from utils.ai_client import get_openai_client as get_instrumented_client
    return get_instrumented_client("ingest_emails")


# =============================================================================
# STEP 1: EXTRACT - Pull structured data from email
# =============================================================================

def extract_from_email(email_path: Path, content: str, client) -> EmailExtraction:
    """
    Extract structured knowledge from an email.
    
    Returns EmailExtraction with contacts, tasks, facts, etc.
    """
    
    model_config = get_model_config("extraction")
    
    # Parse basic metadata from email format
    email_date = _extract_date_from_content(content, email_path.name)
    subject = _extract_subject(content)
    
    system_prompt = """You are extracting structured knowledge from an email for a personal knowledge management system.

Extract ALL of the following as JSON:

{
    "sender": {
        "name": "Full Name",
        "email": "email@example.com",
        "phone": "phone if mentioned",
        "title": "job title if mentioned",
        "company": "company name if known",
        "linkedin": "linkedin url if mentioned"
    },
    "contacts_mentioned": [
        {"name": "...", "email": "...", "phone": "...", "title": "...", "company": "...", "linkedin": "..."}
    ],
    "summary": "1-2 sentence summary of what this email is about",
    "topics": ["list", "of", "main", "topics"],
    "tasks": [
        {
            "text": "action item description",
            "owner": "Myself or person name",
            "due": "YYYY-MM-DD or null",
            "priority": "high/medium/low",
            "related_person": "person name if relevant",
            "related_project": "project name if relevant"
        }
    ],
    "questions": ["questions asked that need answers"],
    "decisions": ["decisions mentioned or made"],
    "commitments": ["commitments made by anyone (e.g., 'I will send X by Friday')"],
    "key_facts": [
        {
            "fact": "interesting fact or information",
            "about": "person or company this is about",
            "fact_type": "preference|background|relationship|project|general"
        }
    ],
    "people_mentioned": ["list of people names mentioned"],
    "companies_mentioned": ["list of companies mentioned"],
    "projects_mentioned": ["list of projects or initiatives mentioned"],
    "requires_response": true/false,
    "urgency": "low|medium|high|critical",
    "email_type": "request|information|follow_up|introduction|scheduling|other"
}

IMPORTANT:
- Extract REAL contact info (emails, phones, titles) - don't make them up
- For tasks, use "Myself" if I need to do it, otherwise use the person's name
- Be specific about facts - they should be actionable/memorable
- Only set requires_response=true if there's a direct question or request to me
- Include ALL people mentioned, even in passing
- For companies, include both specific companies and general industry mentions

Return ONLY valid JSON, no markdown fences."""

    user_prompt = f"""Extract knowledge from this email:

{content[:8000]}"""

    try:
        response = client.chat.completions.create(
            model=model_config.get("model", "gpt-4o"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
        )
        
        result = response.choices[0].message.content.strip()
        
        # Parse JSON
        if result.startswith("```"):
            result = re.sub(r'^```\w*\n?', '', result)
            result = re.sub(r'\n?```$', '', result)
        
        data = json.loads(result)
        
        # Build EmailExtraction
        extraction = EmailExtraction(
            source_file=str(email_path),
            processed_at=datetime.now(),
            email_date=email_date,
            subject=subject,
            sender=ContactInfo(**data.get("sender", {"name": "Unknown"})),
            contacts_mentioned=[ContactInfo(**c) for c in data.get("contacts_mentioned", [])],
            summary=data.get("summary", ""),
            topics=data.get("topics", []),
            tasks=[TaskItem(**t) for t in data.get("tasks", [])],
            questions=data.get("questions", []),
            decisions=data.get("decisions", []),
            commitments=data.get("commitments", []),
            key_facts=[KeyFact(**f) for f in data.get("key_facts", [])],
            people_mentioned=data.get("people_mentioned", []),
            companies_mentioned=data.get("companies_mentioned", []),
            projects_mentioned=data.get("projects_mentioned", []),
            requires_response=data.get("requires_response", False),
            urgency=data.get("urgency", "medium"),
            email_type=data.get("email_type", "other")
        )
        
        return extraction
        
    except json.JSONDecodeError as e:
        console.print(f"[yellow]JSON parse error: {e}[/yellow]")
        # Return minimal extraction
        return EmailExtraction(
            source_file=str(email_path),
            processed_at=datetime.now(),
            email_date=email_date,
            subject=subject,
            sender=ContactInfo(name="Unknown"),
            summary="Failed to extract"
        )
    except Exception as e:
        console.print(f"[red]Extraction failed: {e}[/red]")
        raise


def _extract_date_from_content(content: str, filename: str) -> str:
    """Extract date from email content or filename."""
    
    # Try to find date in content (## YYYY-MM-DD format)
    date_match = re.search(r'##\s*(\d{4}-\d{2}-\d{2})', content)
    if date_match:
        return date_match.group(1)
    
    # Try filename (YYYY-MM-DD_HHMMSS_...)
    filename_match = re.match(r'^(\d{4}-\d{2}-\d{2})', filename)
    if filename_match:
        return filename_match.group(1)
    
    return datetime.now().strftime("%Y-%m-%d")


def _extract_subject(content: str) -> str:
    """Extract subject from email content."""
    
    lines = content.split('\n')
    if lines and lines[0].startswith('# '):
        return lines[0][2:].strip()
    
    return "Unknown Subject"


# =============================================================================
# STEP 2: PLAN - Generate patches for vault
# =============================================================================

def generate_patches(extraction: EmailExtraction, openai_client = None) -> EmailChangePlan:
    """
    Generate vault patches based on extraction.
    
    Creates patches to:
    - Update/create People READMEs with contact info
    - Update/create Customer/Company READMEs (properly classified)
    - Add tasks to appropriate locations
    - Add context entries for interactions
    - Add key facts to relevant entities
    - Cross-link related entities
    
    Entity classification uses entity_discovery service to properly route:
    - People → VAST/People/
    - Companies → VAST/Customers and Partners/
    - Projects → VAST/Projects/
    """
    
    vault = vault_root()
    patches = []
    warnings = []
    entities_to_create = []
    
    # Track entities we'll update
    people_to_update = set()
    
    # 1. SENDER PATCHES - Always update sender's info
    sender = extraction.sender
    # Skip system/automated senders
    skip_senders = ["unknown", "noreply", "no-reply", "ai companion", "notifications", "support", "info"]
    if sender.name and sender.name.lower() not in skip_senders:
        sender_patches = _generate_person_patches(
            sender, 
            extraction,
            is_sender=True,
            openai_client=openai_client
        )
        patches.extend(sender_patches["patches"])
        warnings.extend(sender_patches["warnings"])
        if sender_patches.get("create"):
            entities_to_create.append(sender_patches["create"])
        people_to_update.add(sender.name)
    
    # 2. MENTIONED CONTACTS - Update their info too
    for contact in extraction.contacts_mentioned:
        if contact.name and contact.name.lower() not in ["unknown"]:
            if contact.name not in people_to_update:
                contact_patches = _generate_person_patches(
                    contact,
                    extraction,
                    is_sender=False,
                    openai_client=openai_client
                )
                patches.extend(contact_patches["patches"])
                warnings.extend(contact_patches["warnings"])
                if contact_patches.get("create"):
                    entities_to_create.append(contact_patches["create"])
                people_to_update.add(contact.name)
    
    # 3. CUSTOMER/COMPANY PATCHES
    for company in extraction.companies_mentioned:
        company_patches = _generate_customer_patches(company, extraction)
        patches.extend(company_patches["patches"])
        warnings.extend(company_patches["warnings"])
    
    # 4. TASK PATCHES - Add tasks to relevant people/projects
    for task in extraction.tasks:
        task_patches = _generate_task_patches(task, extraction)
        patches.extend(task_patches)
    
    # Build change plan
    plan = EmailChangePlan(
        source_file=extraction.source_file,
        extraction_file=extraction.source_file.replace(".md", ".email_extraction.json"),
        created_at=datetime.now(),
        patches=patches,
        entities_to_create=entities_to_create,
        warnings=warnings
    )
    
    return plan


def _find_person_folder(name: str) -> Optional[Path]:
    """Find existing person folder in vault."""
    
    vault = vault_root()
    
    # Check VAST/People
    vast_people = vault / "VAST" / "People"
    if vast_people.exists():
        for folder in vast_people.iterdir():
            if folder.is_dir() and folder.name.lower() == name.lower():
                return folder
            # Also check partial matches (first name, last name)
            name_parts = name.lower().split()
            folder_parts = folder.name.lower().split()
            if any(part in folder_parts for part in name_parts if len(part) > 2):
                # Loose match - check if it's close enough
                if len(name_parts) > 0 and name_parts[0] in folder.name.lower():
                    return folder
    
    # Check Personal/People
    personal_people = vault / "Personal" / "People"
    if personal_people.exists():
        for folder in personal_people.iterdir():
            if folder.is_dir() and folder.name.lower() == name.lower():
                return folder
    
    return None


def _find_customer_folder(company: str) -> Optional[Path]:
    """Find existing customer folder in vault."""
    
    vault = vault_root()
    customers = vault / "VAST" / "Customers and Partners"
    
    if not customers.exists():
        return None
    
    company_lower = company.lower()
    
    for folder in customers.iterdir():
        if folder.is_dir():
            folder_lower = folder.name.lower()
            if company_lower in folder_lower or folder_lower in company_lower:
                return folder
    
    return None


def _generate_person_patches(
    contact: ContactInfo, 
    extraction: EmailExtraction,
    is_sender: bool,
    openai_client = None
) -> dict:
    """Generate patches for a person's README (or company if classified as such)."""
    
    from entity_discovery import discover_entity, find_or_create_entity, EntityType
    
    patches = []
    warnings = []
    create_info = None
    
    # First check if entity already exists
    person_folder = _find_person_folder(contact.name)
    company_folder = _find_customer_folder(contact.name) if person_folder is None else None
    
    if person_folder is not None:
        # Existing person - use as-is
        entity_type = EntityType.PERSON
        entity_folder = person_folder
    elif company_folder is not None:
        # Existing company - use as-is
        # Generate company patches and return early (different patch format)
        from entity_discovery import EntityDiscovery, EntityType as ET
        
        # Create a mock discovery object for existing company
        discovery = EntityDiscovery(
            original_name=contact.name,
            entity_type=ET.COMPANY,
            canonical_name=company_folder.name,
            confidence=1.0,
            source="existing_folder"
        )
        return _generate_company_patches_from_discovery(discovery, extraction, company_folder)
    else:
        # New entity - use discovery service to classify
        # Check if we should auto-create
        name_parts = contact.name.split()
        is_full_name = len(name_parts) >= 2 and all(len(p) > 1 for p in name_parts)
        has_email = bool(contact.email and "@" in contact.email)
        
        if not is_full_name and not has_email:
            # Skip - need either full name or email to index
            warnings.append(f"Skipping '{contact.name}' - need full name or email to create entity")
            return {"patches": patches, "warnings": warnings, "create": None}
        
        # Build context from email for better classification
        context = f"Email about: {extraction.subject}. {extraction.summary[:200]}"
        
        # Discover and classify entity
        discovery = discover_entity(
            name=contact.name,
            context=context,
            source_type="email",
            client=openai_client
        )
        
        entity_type = discovery.entity_type
        
        warnings.append(f"Entity '{contact.name}' classified as {entity_type.value} (confidence: {discovery.confidence:.0%})")
        
        # Create folder based on classification
        vault = vault_root()
        
        if entity_type == EntityType.COMPANY:
            entity_folder = vault / "VAST" / "Customers and Partners" / discovery.canonical_name
            entity_folder.mkdir(parents=True, exist_ok=True)
            
            # Create company README
            readme_content = _create_company_readme(discovery, extraction)
            readme_path = entity_folder / "README.md"
            if not readme_path.exists():
                readme_path.write_text(readme_content)
                console.print(f"  [green]Created: Customers and Partners/{entity_folder.name}/README.md[/green]")
            
            create_info = {
                "type": "company",
                "name": discovery.canonical_name,
                "discovery": discovery.model_dump(),
                "source": extraction.source_file
            }
            
            # Return early - companies get different patch treatment
            return _generate_company_patches_from_discovery(discovery, extraction, entity_folder)
        
        elif entity_type == EntityType.PROJECT:
            entity_folder = vault / "VAST" / "Projects" / discovery.canonical_name
            entity_folder.mkdir(parents=True, exist_ok=True)
            
            # Create project README
            readme_content = _create_project_readme(discovery, extraction)
            readme_path = entity_folder / "README.md"
            if not readme_path.exists():
                readme_path.write_text(readme_content)
                console.print(f"  [green]Created: Projects/{entity_folder.name}/README.md[/green]")
            
            create_info = {
                "type": "project",
                "name": discovery.canonical_name,
                "discovery": discovery.model_dump(),
                "source": extraction.source_file
            }
            
            # Return with basic project patches
            return {"patches": patches, "warnings": warnings, "create": create_info}
        
        else:
            # Default to person (including UNKNOWN with low confidence)
            entity_folder = vault / "VAST" / "People" / contact.name
            entity_folder.mkdir(parents=True, exist_ok=True)
            
            # Create person README (original behavior)
            readme_content = _create_person_readme(contact, extraction)
            readme_path = entity_folder / "README.md"
            if not readme_path.exists():
                readme_path.write_text(readme_content)
                console.print(f"  [green]Created: People/{entity_folder.name}/README.md[/green]")
            
            create_info = {
                "type": "person",
                "name": contact.name,
                "contact": contact.model_dump(),
                "source": extraction.source_file
            }
        
        person_folder = entity_folder
    
    readme_path = person_folder / "README.md"
    if not readme_path.exists():
        warnings.append(f"README not found for {contact.name}")
        return {"patches": patches, "warnings": warnings, "create": create_info}
    
    target_path = str(readme_path.relative_to(vault_root()))
    
    # 1. Update contact info in frontmatter if we have new info
    frontmatter_updates = {}
    if contact.email:
        frontmatter_updates["email"] = contact.email
    if contact.phone:
        frontmatter_updates["phone"] = contact.phone
    if contact.title:
        frontmatter_updates["title"] = contact.title
    if contact.company:
        frontmatter_updates["company"] = contact.company
    if contact.linkedin:
        frontmatter_updates["linkedin"] = contact.linkedin
    
    # Always update last_contact for sender
    if is_sender:
        frontmatter_updates["last_contact"] = extraction.email_date
    
    if frontmatter_updates:
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=contact.name,
            operation="upsert_frontmatter",
            frontmatter=frontmatter_updates
        ))
    
    # 2. Add context entry for this interaction
    if is_sender:
        context_entry = f"- {extraction.email_date}: Email re: {extraction.subject[:50]} - {extraction.summary[:100]}"
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=contact.name,
            operation="append_under_heading",
            heading="## Recent Context",
            content=context_entry
        ))
    
    # 3. Add key facts about this person
    person_facts = [f for f in extraction.key_facts if f.about.lower() == contact.name.lower()]
    for fact in person_facts:
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=contact.name,
            operation="append_under_heading",
            heading="## Key Facts",
            content=f"- {fact.fact}"
        ))
    
    # 4. Add wikilinks to mentioned entities
    wikilinks = []
    for company in extraction.companies_mentioned:
        if company.lower() != contact.company.lower() if contact.company else True:
            wikilinks.append(f"[[{company}]]")
    for project in extraction.projects_mentioned:
        wikilinks.append(f"[[{project}]]")
    
    if wikilinks:
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=contact.name,
            operation="ensure_wikilinks",
            wikilinks=wikilinks
        ))
    
    return {"patches": patches, "warnings": warnings, "create": create_info}


def _generate_customer_patches(company: str, extraction: EmailExtraction) -> dict:
    """Generate patches for a customer/company README."""
    
    patches = []
    warnings = []
    
    customer_folder = _find_customer_folder(company)
    
    if customer_folder is None:
        # Skip companies we don't track
        return {"patches": patches, "warnings": warnings}
    
    readme_path = customer_folder / "README.md"
    if not readme_path.exists():
        return {"patches": patches, "warnings": warnings}
    
    target_path = str(readme_path.relative_to(vault_root()))
    
    # Add context entry
    context_entry = f"- {extraction.email_date}: {extraction.summary[:100]}"
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=company,
        operation="append_under_heading",
        heading="## Recent Context",
        content=context_entry
    ))
    
    # Add key facts about this company
    company_facts = [f for f in extraction.key_facts if company.lower() in f.about.lower()]
    for fact in company_facts:
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=company,
            operation="append_under_heading",
            heading="## Key Facts",
            content=f"- {fact.fact}"
        ))
    
    return {"patches": patches, "warnings": warnings}


def _generate_task_patches(task: TaskItem, extraction: EmailExtraction) -> List[VaultPatch]:
    """Generate patches to add a task to relevant location."""
    
    patches = []
    
    # Format task in Obsidian Tasks format
    task_line = f"- [ ] {task.text}"
    if task.owner:
        task_line += f" @{task.owner}"
    if task.due:
        task_line += f" 📅 {task.due}"
    
    priority_map = {
        "highest": "🔺",
        "high": "⏫", 
        "medium": "🔼",
        "low": "🔽",
        "lowest": "⏬"
    }
    if task.priority in priority_map:
        task_line += f" {priority_map[task.priority]}"
    
    task_line += " #task #proposed #auto"
    
    # Determine where to add the task
    if task.related_person:
        person_folder = _find_person_folder(task.related_person)
        if person_folder:
            readme = person_folder / "README.md"
            if readme.exists():
                patches.append(VaultPatch(
                    target_path=str(readme.relative_to(vault_root())),
                    target_entity=task.related_person,
                    operation="append_under_heading",
                    heading="## Open Tasks",
                    content=task_line
                ))
    
    return patches


def _create_person_readme(contact: ContactInfo, extraction: EmailExtraction) -> str:
    """Create a new person README from template."""
    
    return f"""---
type: people
title: "{contact.name}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
last_contact: "{extraction.email_date}"
email: "{contact.email or ''}"
phone: "{contact.phone or ''}"
company: "{contact.company or ''}"
title: "{contact.title or ''}"
tags:
  - "type/people"
  - "needs-review"
---

# {contact.name}

## Profile

**Role**: {contact.title or '_Unknown_'}
**Company**: {contact.company or '_Unknown_'}
**Email**: {contact.email or '_Unknown_'}

## Key Facts

## Recent Context

- {extraction.email_date}: First contact via email re: {extraction.subject[:50]}

## Open Tasks

## Related

"""


def _create_company_readme(discovery, extraction: EmailExtraction) -> str:
    """Create a new company README from entity discovery."""
    
    from entity_discovery import EntityDiscovery
    
    tags = ["type/customer", "needs-review"]
    if discovery.industry:
        safe_industry = discovery.industry.lower().replace(" ", "-").replace("/", "-")
        tags.append(f"industry/{safe_industry}")
    
    return f"""---
type: customer
title: "{discovery.canonical_name}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
last_contact: "{extraction.email_date}"
industry: "{discovery.industry or ''}"
website: "{discovery.website or ''}"
company_type: "{discovery.company_type or 'customer'}"
tags:
  - "{tags[0]}"
  - "{tags[1]}"
---

# {discovery.canonical_name}

## Overview

{discovery.description or f'Customer/partner organization discovered from email.'}

## Key Contacts

## Key Facts

## Recent Context

- {extraction.email_date}: First contact via email re: {extraction.subject[:50]}

## Open Tasks

## Related

"""


def _create_project_readme(discovery, extraction: EmailExtraction) -> str:
    """Create a new project README from entity discovery."""
    
    from entity_discovery import EntityDiscovery
    
    return f"""---
type: projects
title: "{discovery.canonical_name}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
status: "active"
tags:
  - "type/projects"
  - "needs-review"
---

# {discovery.canonical_name}

## Overview

{discovery.description or 'Project discovered from email correspondence.'}

## Goals

## Key Facts

## Recent Context

- {extraction.email_date}: First mention via email re: {extraction.subject[:50]}

## Open Tasks

## Related

"""


def _generate_company_patches_from_discovery(discovery, extraction: EmailExtraction, entity_folder: Path) -> dict:
    """Generate patches for a company that was discovered and classified."""
    
    from entity_discovery import EntityDiscovery
    
    patches = []
    warnings = []
    
    readme_path = entity_folder / "README.md"
    if not readme_path.exists():
        return {"patches": patches, "warnings": warnings, "create": {
            "type": "company",
            "name": discovery.canonical_name,
            "discovery": discovery.model_dump() if hasattr(discovery, 'model_dump') else {},
            "source": extraction.source_file
        }}
    
    target_path = str(readme_path.relative_to(vault_root()))
    
    # Update frontmatter
    frontmatter_updates = {"last_contact": extraction.email_date}
    if discovery.industry:
        frontmatter_updates["industry"] = discovery.industry
    if discovery.website:
        frontmatter_updates["website"] = discovery.website
    
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=discovery.canonical_name,
        operation="upsert_frontmatter",
        frontmatter=frontmatter_updates
    ))
    
    # Add context entry
    context_entry = f"- {extraction.email_date}: Email re: {extraction.subject[:50]} - {extraction.summary[:100]}"
    patches.append(VaultPatch(
        target_path=target_path,
        target_entity=discovery.canonical_name,
        operation="append_under_heading",
        heading="## Recent Context",
        content=context_entry
    ))
    
    # Add company facts
    company_facts = [f for f in extraction.key_facts if discovery.canonical_name.lower() in f.about.lower()]
    for fact in company_facts:
        patches.append(VaultPatch(
            target_path=target_path,
            target_entity=discovery.canonical_name,
            operation="append_under_heading",
            heading="## Key Facts",
            content=f"- {fact.fact}"
        ))
    
    return {
        "patches": patches, 
        "warnings": warnings, 
        "create": {
            "type": "company",
            "name": discovery.canonical_name,
            "discovery": discovery.model_dump() if hasattr(discovery, 'model_dump') else {},
            "source": extraction.source_file
        }
    }


# =============================================================================
# STEP 3: APPLY - Execute patches
# =============================================================================

def apply_patches(plan: EmailChangePlan, dry_run: bool = False) -> dict:
    """Apply all patches from the change plan."""
    
    vault = vault_root()
    results = {
        "applied": 0,
        "skipped": 0,
        "errors": []
    }
    
    for patch in plan.patches:
        try:
            target_path = vault / patch.target_path
            
            if not target_path.exists():
                results["skipped"] += 1
                results["errors"].append(f"File not found: {patch.target_path}")
                continue
            
            if dry_run:
                console.print(f"  [dim]Would {patch.operation}: {patch.target_entity}[/dim]")
                results["applied"] += 1
                continue
            
            content = target_path.read_text()
            
            if patch.operation == "upsert_frontmatter":
                fm_patches = [{"key": k, "value": v} for k, v in patch.frontmatter.items()]
                content = upsert_frontmatter(content, fm_patches)
            
            elif patch.operation == "append_under_heading":
                # Check for duplicate content before appending
                if patch.content not in content:
                    content = append_under_heading(content, patch.heading, patch.content)
            
            elif patch.operation == "ensure_wikilinks":
                content = ensure_wikilinks(content, patch.wikilinks)
            
            elif patch.operation == "add_task":
                task_line = f"- [ ] {patch.task.text}"
                if patch.task.owner:
                    task_line += f" @{patch.task.owner}"
                if patch.task.due:
                    task_line += f" 📅 {patch.task.due}"
                task_line += " #task #proposed #auto"
                
                if task_line not in content:
                    content = append_under_heading(content, "## Open Tasks", task_line)
            
            # Write back
            target_path.write_text(content)
            results["applied"] += 1
            
        except Exception as e:
            results["errors"].append(f"{patch.target_path}: {e}")
            results["skipped"] += 1
    
    return results


# =============================================================================
# CLI
# =============================================================================

def find_pending_emails() -> List[Path]:
    """Find emails that haven't been ingested yet."""
    
    email_dir = vault_root() / "Inbox" / "Email"
    extraction_dir = vault_root() / "Inbox" / "_extraction"
    
    if not email_dir.exists():
        return []
    
    pending = []
    
    for email_file in email_dir.glob("*.md"):
        # Check if already extracted
        extraction_file = extraction_dir / f"{email_file.stem}.email_extraction.json"
        if not extraction_file.exists():
            pending.append(email_file)
    
    return sorted(pending, key=lambda p: p.name)


@click.command()
@click.option(
    "--file", "-f", "single_file",
    type=click.Path(exists=True),
    help="Process a single email file"
)
@click.option("--dry-run", is_flag=True, help="Show what would be changed without applying")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
@click.option("--limit", "-n", type=int, default=None, help="Limit number of emails to process")
def main(single_file: Optional[str], dry_run: bool, verbose: bool, limit: Optional[int]):
    """Ingest emails into the vault knowledge base."""
    
    console.print(Panel.fit(
        "[bold blue]Email Ingest Pipeline[/bold blue]\n"
        "[dim]Extract → Plan → Apply[/dim]",
        border_style="blue"
    ))
    
    # Find emails to process
    if single_file:
        emails = [Path(single_file)]
    else:
        emails = find_pending_emails()
        if limit:
            emails = emails[:limit]
    
    if not emails:
        console.print("[yellow]No pending emails to ingest.[/yellow]")
        return
    
    console.print(f"Found [bold]{len(emails)}[/bold] emails to ingest")
    
    if dry_run:
        console.print("[yellow]DRY RUN - no changes will be made[/yellow]")
    
    # Get OpenAI client
    client = get_openai_client()
    
    # Ensure extraction dir exists
    extraction_dir = vault_root() / "Inbox" / "_extraction"
    extraction_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each email
    total_patches = 0
    total_entities = 0
    failed_emails = []
    
    for i, email_path in enumerate(emails):
        console.print(f"\n[cyan]━━━ [{i+1}/{len(emails)}] {email_path.name[:50]} ━━━[/cyan]")
        
        try:
            content = email_path.read_text()
            
            # Step 1: Extract
            console.print("  [dim]Step 1: Extracting knowledge...[/dim]")
            extraction = extract_from_email(email_path, content, client)
            
            if verbose:
                table = Table(show_header=False, box=None, padding=(0, 1))
                table.add_column("Key", style="dim")
                table.add_column("Value")
                table.add_row("Sender", f"{extraction.sender.name} <{extraction.sender.email or 'n/a'}>")
                table.add_row("Topics", ", ".join(extraction.topics[:3]))
                table.add_row("Tasks", str(len(extraction.tasks)))
                table.add_row("Facts", str(len(extraction.key_facts)))
                table.add_row("People", ", ".join(extraction.people_mentioned[:5]))
                console.print(table)
            
            # Save extraction
            extraction_file = extraction_dir / f"{email_path.stem}.email_extraction.json"
            extraction_file.write_text(extraction.model_dump_json(indent=2))
            
            # Step 2: Plan patches (with entity discovery/classification)
            console.print("  [dim]Step 2: Planning vault updates (with entity classification)...[/dim]")
            plan = generate_patches(extraction, openai_client=client)
            
            if verbose or plan.warnings:
                for warning in plan.warnings:
                    console.print(f"    [yellow]⚠ {warning}[/yellow]")
            
            console.print(f"    Patches planned: {len(plan.patches)}")
            console.print(f"    New entities: {len(plan.entities_to_create)}")
            
            # Save plan
            plan_file = extraction_dir / f"{email_path.stem}.email_changeplan.json"
            plan_file.write_text(plan.model_dump_json(indent=2))
            
            # Step 3: Apply patches
            console.print("  [dim]Step 3: Applying patches...[/dim]")
            results = apply_patches(plan, dry_run=dry_run)
            
            if results["errors"] and verbose:
                for error in results["errors"]:
                    console.print(f"    [red]✗ {error}[/red]")
            
            console.print(f"    [green]✓ Applied {results['applied']} patches[/green]")
            
            total_patches += results["applied"]
            total_entities += len(plan.entities_to_create)
            
        except Exception as e:
            console.print(f"    [red]✗ Failed: {e}[/red]")
            failed_emails.append((email_path.name, str(e)))
            continue
    
    # Summary
    console.print(f"\n[bold green]━━━ Ingested {len(emails) - len(failed_emails)} emails ━━━[/bold green]")
    console.print(f"  Total patches applied: {total_patches}")
    console.print(f"  New entities created: {total_entities}")
    
    if failed_emails:
        console.print(f"\n[yellow]Failed emails ({len(failed_emails)}):[/yellow]")
        for name, error in failed_emails[:5]:
            console.print(f"  • {name[:40]}: {error[:60]}")
        if len(failed_emails) > 5:
            console.print(f"  ... and {len(failed_emails) - 5} more")
    
    if dry_run:
        console.print("\n[dim]This was a dry run. Run without --dry-run to apply changes.[/dim]")


if __name__ == "__main__":
    main()

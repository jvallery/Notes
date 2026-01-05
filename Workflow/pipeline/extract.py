"""
Unified Extractor - Extract structured knowledge from any content type.

Uses LLM with rich context (persona, manifests, glossary) to produce
UnifiedExtraction for downstream patching and output generation.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from .envelope import ContentEnvelope, ContentType
from .context import ContextBundle
from .models import (
    UnifiedExtraction, ContactInfo, Fact, TaskItem, 
    MentionedEntity, EntityRef, SuggestedOutputs
)
from scripts.utils import get_logger, get_model_config


class UnifiedExtractor:
    """Extract structured knowledge from content.
    
    Features:
    - Rich context injection (persona, manifests, glossary)
    - Content-type specific guidance
    - Entity-attached facts for smart patching
    - Suggested outputs (replies, calendar, tasks)
    - Prompt caching for token efficiency
    """
    
    def __init__(self, vault_root: Path, verbose: bool = False):
        self.vault_root = vault_root
        self.verbose = verbose
        self._client = None
        self._context: Optional[ContextBundle] = None
        self.logger = get_logger("unified_extractor")
    
    @property
    def client(self):
        """Get OpenAI client lazily."""
        if self._client is None:
            from scripts.utils.ai_client import get_openai_client
            self._client = get_openai_client("unified_extractor")
        return self._client
    
    def extract(self, envelope: ContentEnvelope, context: Optional[ContextBundle] = None) -> UnifiedExtraction:
        """Extract structured knowledge from content.
        
        Args:
            envelope: ContentEnvelope with normalized content
            context: Optional ContextBundle (loaded if not provided)
        
        Returns:
            UnifiedExtraction with all extracted knowledge
        """
        # Load context if not provided
        if context is None:
            context = ContextBundle.load(self.vault_root, envelope)
        
        # Build prompt - pass verbose flag for cache logging
        system_prompt = self._build_system_prompt(envelope, context)
        user_prompt = self._build_user_prompt(envelope)
        
        if self.verbose:
            _, prefix_hash = context.get_cacheable_prefix()
            self.logger.info(f"System prompt length={len(system_prompt)} chars, cacheable prefix hash={prefix_hash}")
        
        # Select model based on content type if configured (e.g., extract_email, extract_transcript)
        task_key = f"extract_{envelope.content_type.value}"
        model_config = get_model_config(task_key)
        
        # Call LLM with prompt caching enabled
        try:
            with self.logger.context(phase="extract", file=str(envelope.source_path)):
                response = self.client.chat.completions.create(
                    model=model_config.get("model", "gpt-4o"),
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.0,
                    # Prompt caching: static context (persona/glossary/aliases) is first in system prompt.
                )
            
            # Log cache stats if available (OpenAI returns cached_tokens in usage)
            if self.verbose and hasattr(response, 'usage') and response.usage:
                usage = response.usage
                prompt_tokens = getattr(usage, 'prompt_tokens', 0)
                cached_tokens = getattr(usage, 'cached_tokens', 0) or getattr(getattr(usage, 'prompt_tokens_details', {}), 'cached_tokens', 0)
                if cached_tokens > 0:
                    cache_pct = (cached_tokens / prompt_tokens * 100) if prompt_tokens > 0 else 0
                    self.logger.info(f"Cache HIT: {cached_tokens}/{prompt_tokens} tokens ({cache_pct:.0f}%)")
                else:
                    self.logger.info(f"Cache miss: {prompt_tokens} prompt tokens")
            
            result = response.choices[0].message.content.strip()
            
            # Parse JSON
            if result.startswith("```"):
                result = re.sub(r'^```\w*\n?', '', result)
                result = re.sub(r'\n?```$', '', result)
            
            data = json.loads(result)
            
            return self._build_extraction(envelope, data)
            
        except json.JSONDecodeError as e:
            return self._build_minimal_extraction(envelope, f"JSON parse error: {e}")
        except Exception as e:
            self.logger.error("Extraction failed", exc_info=True)
            raise RuntimeError(f"Extraction failed: {e}")
    
    def _build_system_prompt(self, envelope: ContentEnvelope, context: ContextBundle) -> str:
        """Build system prompt with context and extraction instructions.
        
        PROMPT CACHING: OpenAI caches identical prompt prefixes >= 1024 tokens.
        We structure the prompt so static content (persona, glossary) comes FIRST,
        followed by content-type-specific instructions (dynamic).
        """
        
        # Get formatted context - static portion first for caching
        # Pass verbose flag to show cache eligibility info
        context_section = context.get_extraction_context(compact=True, verbose=self.verbose)
        
        # Content-type specific guidance (dynamic, comes after cached prefix)
        type_guidance = self._get_type_guidance(envelope.content_type)
        
        instructions = f"""You are extracting structured knowledge from content for a personal knowledge management system.

{context_section}

## CONTENT TYPE
This is a {envelope.content_type.value}. {type_guidance}

## EXTRACTION SCHEMA
Return a JSON object with this exact structure:

{{
    "note_type": "customer|people|projects|rob|journal",
    "primary_entity": {{"entity_type": "person|company|project", "name": "...", "confidence": 0.9}} or null,
    
    "title": "Brief descriptive title",
    "summary": "1-3 sentence summary",
    
    "participants": ["Person 1", "Person 2"],
    "contacts": [
        {{"name": "...", "email": "...", "phone": "...", "title": "...", "company": "...", "linkedin": "..."}}
    ],
    
    "facts": [
        {{"text": "fact about someone/something", "about_entity": {{"entity_type": "person", "name": "..."}}, "fact_type": "background|preference|technical|relationship", "confidence": 0.8}}
    ],
    "decisions": ["Decision 1", "Decision 2"],
    "topics": ["Topic 1", "Topic 2"],
    
    "tasks": [
        {{"text": "action item", "owner": "Myself or person name", "due": "YYYY-MM-DD", "priority": "high|medium|low", "related_person": "...", "related_project": "...", "related_customer": "..."}}
    ],
    "questions": ["Question needing answer"],
    "commitments": ["Commitment made by anyone"],
    
    "mentioned_entities": [
        {{"entity_type": "person|company|project", "name": "...", "role": "discussed|action_owner|mentioned", "facts_about": ["fact 1", "fact 2"], "confidence": 0.8}}
    ],
    
    "email_requires_response": true|false,
    "email_urgency": "low|medium|high|critical",
    "email_type": "request|information|follow_up|introduction|scheduling|other",
    
    "suggested_outputs": {{
        "needs_reply": true|false,
        "reply_urgency": "urgent|normal|low",
        "reply_context": "Key points to address in reply",
        "calendar_invite": {{"title": "...", "proposed_date": "YYYY-MM-DD", "attendees": [...], "duration_minutes": 30}} or null,
        "follow_up_reminder": {{"text": "...", "remind_date": "YYYY-MM-DD"}} or null
    }},
    
    "confidence": 0.85
}}

## CRITICAL RULES

1. **FACTS ABOUT ENTITIES**: When you learn something about a person/company/project, 
   add it to both the `facts` array AND the entity's `facts_about` in `mentioned_entities`.
   This is how we know which entities to update.

2. **TASK OWNERSHIP**: 
   - If the speaker (me) commits to something → owner is "Myself"
   - If someone else commits → use their full name (from ENTITY GLOSSARY if possible)
   - If unclear → owner is "TBD"

3. **ENTITY MATCHING**: Use names from the ENTITY GLOSSARY when possible to ensure consistency.
   If you see a name that's similar to a known entity, use the known entity's name.

4. **PRIMARY ENTITY**:
   - 1:1 meetings → the other person is primary_entity (type: person)
   - Customer meetings → the customer/company is primary_entity (type: company)
   - Project discussions → the project is primary_entity (type: project)
   - General updates → primary_entity can be null

5. **NOTE_TYPE CLASSIFICATION** (based on MEETING FORMAT, not content):
   - "people" = 1:1 meetings or small group with VAST colleagues. The primary_entity is the other person.
     Even if discussing projects/customers, a 1:1 with Jeff goes under Jeff's folder.
   - "customer" = external customer/partner meeting (multiple people from customer org present)
   - "projects" = internal project-focused group discussion (3+ VAST people)
   - "rob" = recurring team sync (Rhythm of Business) - weekly, biweekly standups
   - "journal" = personal reflection

   **CRITICAL**: Look at WHO is in the meeting, not WHAT is discussed:
   - 1:1 with Jeff Denworth discussing Microsoft → note_type: "people", primary_entity: Jeff Denworth
   - Group call with Microsoft team → note_type: "customer", primary_entity: Microsoft
   - Internal project standup → note_type: "projects", primary_entity: project name

6. **VERBOSITY - ALL FACTS/DECISIONS/TOPICS MUST BE SELF-CONTAINED**:
   Every extracted fact, decision, topic, and task MUST be fully understandable 6 months 
   from now WITHOUT reading the source document. Never use vague references.
   
   ALWAYS include:
   - WHO: Full names of people (not just "he" or "they" or first names only)
   - WHAT: Specific project, product, or initiative name (not "the project" or "this")
   - WHICH: Specific customer/company when relevant (not "the customer")
   - CONTEXT: Enough detail that the statement stands alone
   
   BAD EXAMPLES (vague, useless later):
   - "Use the same concepts from previous CSP projects" → Which projects? What concepts?
   - "Discussed storage architecture" → Whose storage? Which architecture?
   - "Follow up on pricing" → Which customer? What pricing tier?
   - "He mentioned the timeline" → Who? What timeline for what?
   
   GOOD EXAMPLES (self-contained, useful later):
   - "Apply Microsoft Azure marketplace SKU patterns from LSv4 launch to GCP offer design"
   - "Discussed VAST storage architecture for Google GDC RFP encryption requirements"
   - "Follow up with Kanchan Mehrotra on Microsoft Apollo project pricing proposal"
   - "Jeff Denworth mentioned Q1 2026 timeline for MAI unified cache GA"
   
   If you don't know a specific name, say so: "Unknown Microsoft contact mentioned..."

Return ONLY valid JSON, no markdown fences or explanation."""

        return instructions
    
    def _get_type_guidance(self, content_type: ContentType) -> str:
        """Get content-type specific extraction guidance."""
        
        guidance = {
            ContentType.EMAIL: """
Pay special attention to:
- Sender and recipient information (extract all contact details)
- Whether a response is needed (direct questions, requests)
- Urgency signals (deadline mentions, "urgent", "ASAP")
- Commitments made by sender or requested from me
- Any scheduling/calendar mentions for calendar_invite suggestion""",
            
            ContentType.TRANSCRIPT: """
This is a meeting transcript with speaker labels.
Pay special attention to:
- **PARTICIPANT COUNT**: How many distinct speakers/people are in this meeting?
  - 2 people (1:1) → note_type: "people", primary_entity is the OTHER person
  - Multiple VAST employees → note_type: "projects" 
  - External customer/partner present → note_type: "customer"
- Identify all participants from speaker labels and mentions
- Capture action items with clear owners
- Note decisions made during the meeting  
- Extract facts learned about people, companies, or projects
- Summarize the main discussion points as topics""",
            
            ContentType.DOCUMENT: """
This is a document or article.
Pay special attention to:
- Key information and facts
- Relevant entities mentioned
- Any action items or recommendations
- The main topics covered""",
            
            ContentType.VOICE: """
This is a voice memo transcription.
Pay special attention to:
- Tasks and reminders mentioned
- Ideas or thoughts to capture
- References to people or projects
- Follow-up items""",
        }
        
        return guidance.get(content_type, "Extract all relevant information.")
    
    def _build_user_prompt(self, envelope: ContentEnvelope) -> str:
        """Build user prompt with content."""
        
        # Truncate very long content
        content = envelope.raw_content
        if len(content) > 12000:
            content = content[:12000] + "\n\n[... content truncated ...]"
        
        return f"""Extract knowledge from this {envelope.content_type.value}:

Date: {envelope.date}
Title: {envelope.title}
Participants: {', '.join(envelope.participants) if envelope.participants else 'Unknown'}

---

{content}"""
    
    def _build_extraction(self, envelope: ContentEnvelope, data: dict) -> UnifiedExtraction:
        """Build UnifiedExtraction from parsed JSON data."""
        
        # Parse primary entity
        primary_entity = None
        if data.get("primary_entity"):
            pe = data["primary_entity"]
            primary_entity = EntityRef(
                entity_type=pe.get("entity_type", "person"),
                name=pe.get("name", ""),
                confidence=pe.get("confidence", 0.8)
            )
        
        # Parse contacts
        contacts = []
        for c in data.get("contacts", []):
            contacts.append(ContactInfo(**c))
        
        # Parse facts
        facts = []
        for f in data.get("facts", []):
            about = None
            if f.get("about_entity"):
                about = EntityRef(**f["about_entity"])
            facts.append(Fact(
                text=f.get("text", ""),
                about_entity=about,
                fact_type=f.get("fact_type", "general"),
                confidence=f.get("confidence", 0.8)
            ))
        
        # Parse tasks
        tasks = []
        for t in data.get("tasks", []):
            tasks.append(TaskItem(**t))
        
        # Parse mentioned entities
        mentioned = []
        for m in data.get("mentioned_entities", []):
            mentioned.append(MentionedEntity(
                entity_type=m.get("entity_type", "person"),
                name=m.get("name", ""),
                role=m.get("role"),
                facts_about=m.get("facts_about", []),
                confidence=m.get("confidence", 0.8)
            ))
        
        # Parse suggested outputs
        suggested = SuggestedOutputs()
        if data.get("suggested_outputs"):
            so = data["suggested_outputs"]
            suggested = SuggestedOutputs(
                needs_reply=so.get("needs_reply", False),
                reply_urgency=so.get("reply_urgency", "normal"),
                reply_context=so.get("reply_context"),
            )
        
        # Build legacy mentions for compatibility
        mentions = {
            "people": data.get("participants", []),
            "projects": [e["name"] for e in data.get("mentioned_entities", []) if e.get("entity_type") == "project"],
            "accounts": [e["name"] for e in data.get("mentioned_entities", []) if e.get("entity_type") == "company"],
        }
        
        return UnifiedExtraction(
            source_file=str(envelope.source_path),
            content_type=envelope.content_type.value,
            processed_at=datetime.now(),
            note_type=data.get("note_type", "people"),
            primary_entity=primary_entity,
            date=envelope.date,
            title=data.get("title", envelope.title),
            summary=data.get("summary", ""),
            participants=data.get("participants", envelope.participants),
            contacts=contacts,
            facts=facts,
            decisions=data.get("decisions", []),
            topics=data.get("topics", []),
            tasks=tasks,
            questions=data.get("questions", []),
            commitments=data.get("commitments", []),
            mentioned_entities=mentioned,
            mentions=mentions,
            email_requires_response=data.get("email_requires_response", False),
            email_urgency=data.get("email_urgency", "medium"),
            email_type=data.get("email_type", "other"),
            suggested_outputs=suggested,
            confidence=data.get("confidence", 0.8)
        )
    
    def _build_minimal_extraction(self, envelope: ContentEnvelope, error: str) -> UnifiedExtraction:
        """Build minimal extraction when parsing fails."""
        return UnifiedExtraction(
            source_file=str(envelope.source_path),
            content_type=envelope.content_type.value,
            processed_at=datetime.now(),
            note_type="people",
            date=envelope.date,
            title=envelope.title,
            summary=f"Extraction failed: {error}",
            participants=envelope.participants,
            confidence=0.0
        )

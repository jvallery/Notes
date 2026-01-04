#!/usr/bin/env python3
"""
Pre-extraction content classification.

Determines note_type and likely domain path prefix for Inbox sources
where the vault destination is not yet known.

Uses heuristics based on:
1. Source folder (Transcripts vs Email)
2. Filename patterns (1-1, ROB, customer names)
3. Content patterns (participant counts, keywords)

Can be upgraded to an LLM classifier later if needed.
"""

import re
from pathlib import Path


# Known patterns for classification
PEOPLE_PATTERNS = [
    r"1[-:]1",
    r"1:1",
    r"one[-\s]on[-\s]one",
    r"weekly\s+with",
    r"sync\s+with",
    r"check[-\s]in\s+with",
]

ROB_PATTERNS = [
    r"office\s+hours",
    r"team\s+sync",
    r"all[-\s]hands",
    r"standup",
    r"retro",
    r"planning\s+meeting",
    r"weekly\s+sync",
    r"leadership\s+sync",
    r"flight\s+school",
]

CUSTOMER_PATTERNS = [
    r"rfp",
    r"proposal",
    r"deal\s+review",
    r"customer\s+meeting",
    r"partner\s+meeting",
    r"qbr",
    r"business\s+review",
]

PROJECT_PATTERNS = [
    r"sprint",
    r"architecture",
    r"design\s+review",
    r"code\s+review",
    r"technical\s+discussion",
]

# Known customer/account names for matching
KNOWN_ACCOUNTS = [
    "google",
    "microsoft",
    "openai",
    "walmart",
    "silk",
]


def classify(source_path: str, content: str | None = None) -> dict:
    """
    Classify content to determine note_type and likely domain path.
    
    Args:
        source_path: Path to the source file
        content: Optional content for deeper analysis
        
    Returns:
        {
            "note_type": "people|customer|partners|projects|rob|journal",
            "likely_domain_path_prefix": "VAST/People" or similar,
            "confidence": 0.0-1.0,
            "reason": "explanation"
        }
    """
    path_lower = source_path.lower()
    filename = Path(source_path).stem.lower()
    
    # Combine filename and content for pattern matching
    text_to_analyze = filename
    if content:
        # Only use first ~1000 chars for classification
        text_to_analyze = f"{filename} {content[:1000]}".lower()
    
    # Check for ROB patterns first (team meetings)
    for pattern in ROB_PATTERNS:
        if re.search(pattern, text_to_analyze, re.IGNORECASE):
            return {
                "note_type": "rob",
                "likely_domain_path_prefix": "VAST/ROB",
                "confidence": 0.85,
                "reason": f"Matched ROB pattern: {pattern}",
            }
    
    # Check for customer/account patterns
    for pattern in CUSTOMER_PATTERNS:
        if re.search(pattern, text_to_analyze, re.IGNORECASE):
            return {
                "note_type": "customer",
                "likely_domain_path_prefix": "VAST/Customers and Partners",
                "confidence": 0.80,
                "reason": f"Matched customer pattern: {pattern}",
            }
    
    # Check for known account names
    for account in KNOWN_ACCOUNTS:
        if account in text_to_analyze:
            return {
                "note_type": "customer",
                "likely_domain_path_prefix": "VAST/Customers and Partners",
                "confidence": 0.85,
                "reason": f"Found account name: {account}",
            }
    
    # Check for 1:1 / people patterns
    for pattern in PEOPLE_PATTERNS:
        if re.search(pattern, text_to_analyze, re.IGNORECASE):
            return {
                "note_type": "people",
                "likely_domain_path_prefix": "VAST/People",
                "confidence": 0.85,
                "reason": f"Matched 1:1 pattern: {pattern}",
            }
    
    # Check for project patterns
    for pattern in PROJECT_PATTERNS:
        if re.search(pattern, text_to_analyze, re.IGNORECASE):
            return {
                "note_type": "projects",
                "likely_domain_path_prefix": "VAST/Projects",
                "confidence": 0.75,
                "reason": f"Matched project pattern: {pattern}",
            }
    
    # Default based on source folder
    if "transcripts" in path_lower:
        # Default transcript to people (most common case)
        return {
            "note_type": "people",
            "likely_domain_path_prefix": "VAST/People",
            "confidence": 0.60,
            "reason": "Default for transcript without clear pattern",
        }
    elif "email" in path_lower:
        # Emails default to customer context
        return {
            "note_type": "customer",
            "likely_domain_path_prefix": "VAST/Customers and Partners",
            "confidence": 0.60,
            "reason": "Default for email without clear pattern",
        }
    elif "personal" in path_lower:
        return {
            "note_type": "journal",
            "likely_domain_path_prefix": "Personal",
            "confidence": 0.70,
            "reason": "Personal folder",
        }
    
    # Ultimate fallback
    return {
        "note_type": "people",
        "likely_domain_path_prefix": "VAST/People",
        "confidence": 0.50,
        "reason": "No clear pattern, defaulting to people",
    }


def classify_for_profile(source_path: str, content: str | None = None) -> str:
    """
    Convenience function that returns just the note_type for profile selection.
    
    Args:
        source_path: Path to source file
        content: Optional content for analysis
        
    Returns:
        note_type string
    """
    result = classify(source_path, content)
    return result["note_type"]


if __name__ == "__main__":
    # Quick test
    import sys
    
    test_cases = [
        ("Inbox/Transcripts/2026-01-03 - Jeff 1-1.md", None),
        ("Inbox/Transcripts/2026-01-03 - Google RFP Review.md", None),
        ("Inbox/Transcripts/2026-01-03 - Team Office Hours.md", None),
        ("Inbox/Email/2026-01-03 - Microsoft Follow-up.md", None),
        ("Inbox/Transcripts/Sprint Planning.md", None),
    ]
    
    for path, content in test_cases:
        result = classify(path, content)
        print(f"{Path(path).name}:")
        print(f"  → {result['note_type']} ({result['likely_domain_path_prefix']})")
        print(f"  → confidence: {result['confidence']}, reason: {result['reason']}")
        print()

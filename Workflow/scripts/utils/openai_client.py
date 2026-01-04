#!/usr/bin/env python3
"""
OpenAI client wrapper with Structured Outputs support.

Provides:
- Environment-based client initialization
- Pydantic schema-enforced parsing via client.responses.parse()
- Privacy enforcement (store=False always)
- Retry logic with exponential backoff
- Latency and token tracking
"""

import os
import time
from pathlib import Path
from typing import TypeVar

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

from .config import load_config, workflow_root

# Load .env from workflow directory
load_dotenv(workflow_root() / ".env")


T = TypeVar("T", bound=BaseModel)


class OpenAIError(Exception):
    """Raised when OpenAI API calls fail."""
    pass


def get_client() -> OpenAI:
    """
    Create OpenAI client from environment variable.
    
    Raises:
        OpenAIError: If OPENAI_API_KEY is not set
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise OpenAIError(
            "OPENAI_API_KEY environment variable not set. "
            "Set it with: export OPENAI_API_KEY=sk-..."
        )
    return OpenAI(api_key=api_key)


def parse_structured(
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_content: str,
    response_model: type[T],
    temperature: float = 0.2,
    max_retries: int = 3,
) -> tuple[T, dict]:
    """
    Call OpenAI with Pydantic schema enforcement.
    
    Uses client.responses.parse() API for structured outputs that are
    guaranteed to match the Pydantic schema.
    
    Args:
        client: OpenAI client instance
        model: Model name (e.g., "gpt-4o", "gpt-4o-mini")
        system_prompt: System message content
        user_content: User message content
        response_model: Pydantic model class for response parsing
        temperature: Sampling temperature (lower = more deterministic)
        max_retries: Number of retry attempts on failure
        
    Returns:
        Tuple of (parsed_response, metadata)
        
        metadata includes:
        - latency_ms: Total time for successful call
        - model: Model used
        - attempt: Which attempt succeeded (1-indexed)
        - input_tokens: Tokens in prompt (if available)
        - output_tokens: Tokens in response (if available)
        
    Raises:
        OpenAIError: If all retries fail
        
    CRITICAL: Always uses store=False for privacy compliance.
    """
    config = load_config()
    
    # Enforce privacy - never store prompts/responses
    privacy_config = config.get("models", {}).get("privacy", {})
    legacy_api_config = config.get("api", {})

    # Preferred config location: models.privacy.store (Workflow/config.yaml)
    store_enabled = privacy_config.get("store", legacy_api_config.get("store", False))
    api_surface = privacy_config.get("api", legacy_api_config.get("api"))

    if store_enabled:
        raise OpenAIError(
            "models.privacy.store must be false in config.yaml for privacy. "
            "OpenAI must not store any prompts or responses."
        )

    # We standardize on the Responses API for structured outputs.
    if api_surface and api_surface != "responses":
        raise OpenAIError(
            f"models.privacy.api must be 'responses' (got {api_surface!r}). "
            "This project standardizes on the Responses API."
        )
    
    start_time = time.time()
    last_error = None
    
    for attempt in range(max_retries):
        try:
            # Use responses.parse for schema-enforced structured outputs
            # CRITICAL: store=False ensures prompts/responses are not stored by OpenAI
            response = client.responses.parse(
                model=model,
                instructions=system_prompt,
                input=user_content,
                text_format=response_model,
                temperature=temperature,
                store=False,  # Privacy: never store prompts/responses
            )
            
            latency_ms = int((time.time() - start_time) * 1000)
            
            # Extract parsed response
            parsed = response.output_parsed
            
            if parsed is None:
                # Check for refusal content
                refusal = None
                for output in getattr(response, "output", []) or []:
                    if getattr(output, "type", None) != "message":
                        continue
                    for content in getattr(output, "content", []) or []:
                        if getattr(content, "type", None) == "refusal":
                            refusal = getattr(content, "refusal", None)
                            break
                    if refusal:
                        break

                if refusal:
                    raise OpenAIError(f"Model refused: {refusal}")
                raise OpenAIError("No parsed response received")
            
            metadata = {
                "latency_ms": latency_ms,
                "model": model,
                "attempt": attempt + 1,
            }
            
            # Extract token usage if available
            if response.usage:
                metadata["input_tokens"] = response.usage.input_tokens
                metadata["output_tokens"] = response.usage.output_tokens
                metadata["total_tokens"] = response.usage.total_tokens
            
            return parsed, metadata
            
        except OpenAIError:
            # Don't retry our own errors
            raise
        except Exception as e:
            last_error = e
            if attempt < max_retries - 1:
                # Exponential backoff: 1s, 2s, 4s...
                sleep_time = 2 ** attempt
                time.sleep(sleep_time)
            continue
    
    raise OpenAIError(
        f"OpenAI call failed after {max_retries} attempts. "
        f"Last error: {last_error}"
    )


def check_api_key() -> bool:
    """
    Check if OpenAI API key is configured.
    
    Returns:
        True if OPENAI_API_KEY is set, False otherwise
    """
    return bool(os.environ.get("OPENAI_API_KEY"))


def estimate_tokens(text: str) -> int:
    """
    Rough estimate of token count for text.
    
    Uses the ~4 chars per token heuristic.
    For accurate counts, use tiktoken.
    
    Args:
        text: Text to estimate
        
    Returns:
        Estimated token count
    """
    return len(text) // 4

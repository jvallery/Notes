#!/usr/bin/env python3
"""
OpenAI client wrapper with Structured Outputs support.

Provides:
- Environment-based client initialization
- Pydantic schema-enforced parsing via responses.parse()
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
    
    Uses the responses.parse() API for structured outputs that are
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
    api_config = config.get("api", {})
    if api_config.get("store", False):
        raise OpenAIError(
            "api.store must be False in config.yaml for privacy. "
            "OpenAI must not store any prompts or responses."
        )
    
    start_time = time.time()
    last_error = None
    
    for attempt in range(max_retries):
        try:
            # Use beta.chat.completions.parse for structured outputs
            # CRITICAL: store=False ensures prompts/responses are not stored by OpenAI
            response = client.beta.chat.completions.parse(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                response_format=response_model,
                temperature=temperature,
                store=False,  # Privacy: never store prompts/responses
            )
            
            latency_ms = int((time.time() - start_time) * 1000)
            
            # Extract parsed response
            parsed = response.choices[0].message.parsed
            
            if parsed is None:
                # Check for refusal
                if response.choices[0].message.refusal:
                    raise OpenAIError(f"Model refused: {response.choices[0].message.refusal}")
                raise OpenAIError("No parsed response received")
            
            metadata = {
                "latency_ms": latency_ms,
                "model": model,
                "attempt": attempt + 1,
            }
            
            # Extract token usage if available
            if response.usage:
                metadata["input_tokens"] = response.usage.prompt_tokens
                metadata["output_tokens"] = response.usage.completion_tokens
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

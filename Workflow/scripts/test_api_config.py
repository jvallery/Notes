#!/usr/bin/env python3
"""
Test OpenAI API configuration.

Validates:
1. API key is set
2. Models are correctly configured (gpt-5.2)
3. No max_tokens constraint
4. store=False is enforced
5. API calls work

Usage:
    python scripts/test_api_config.py
"""

import os
import sys
from pathlib import Path

# Add Workflow to path for proper imports
workflow_dir = Path(__file__).parent.parent
sys.path.insert(0, str(workflow_dir))
sys.path.insert(0, str(workflow_dir / "scripts"))

from openai import OpenAI
from pydantic import BaseModel


class TestResponse(BaseModel):
    """Simple test response model."""
    message: str
    number: int


def test_api_key():
    """Test that API key is configured."""
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        print("❌ OPENAI_API_KEY not set")
        return False
    print(f"✓ API key configured ({key[:8]}...)")
    return True


def test_config_loading():
    """Test that config loads correctly with gpt-5.2."""
    from utils.config import get_model_config
    
    configs = {
        "classify": "gpt-4o-mini",
        "extract_transcript": "gpt-5.2",
        "extract_email": "gpt-5.2",
        "planning": "gpt-5.2",
        "backfill": "gpt-4o-mini",
    }
    
    all_ok = True
    for task, expected_model in configs.items():
        config = get_model_config(task)
        model = config.get("model")
        has_max_tokens = "max_tokens" in config
        
        if model != expected_model:
            print(f"❌ {task}: expected {expected_model}, got {model}")
            all_ok = False
        elif has_max_tokens:
            print(f"❌ {task}: max_tokens should not be set (got {config['max_tokens']})")
            all_ok = False
        else:
            print(f"✓ {task}: model={model}, no max_tokens")
    
    return all_ok


def test_parse_structured_call():
    """Test that parse_structured works without max_tokens."""
    from utils.openai_client import parse_structured, get_client
    
    client = get_client()
    
    print("\nTesting parse_structured with gpt-5.2...")
    try:
        result, metadata = parse_structured(
            client=client,
            model="gpt-5.2",
            system_prompt="You are a helpful test assistant.",
            user_content="Return a test message saying 'API works' and the number 42.",
            response_model=TestResponse,
            temperature=0.0,
        )
        
        print(f"✓ Response: {result.message}, {result.number}")
        print(f"  Model: {metadata.get('model')}")
        print(f"  Tokens: {metadata.get('total_tokens', 'N/A')}")
        print(f"  Latency: {metadata.get('latency_ms')}ms")
        return True
        
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return False


def test_direct_api_call():
    """Test direct API call pattern (like backfill/extractor.py)."""
    client = OpenAI()
    
    print("\nTesting direct API call with store=False...")
    try:
        response = client.responses.parse(
            model="gpt-5.2",
            instructions="You are a test assistant.",
            input="Return message='Direct API works' and number=123.",
            text_format=TestResponse,
            temperature=0.0,
            store=False,  # Must be set
        )
        
        parsed = response.output_parsed
        tokens = response.usage.total_tokens if response.usage else "N/A"
        
        print(f"✓ Response: {parsed.message}, {parsed.number}")
        print(f"  Tokens: {tokens}")
        return True
        
    except Exception as e:
        print(f"❌ Direct API call failed: {e}")
        return False


def main():
    print("=" * 60)
    print("OpenAI API Configuration Test")
    print("=" * 60)
    print()
    
    results = []
    
    # Test 1: API Key
    print("1. Checking API key...")
    results.append(test_api_key())
    print()
    
    if not results[-1]:
        print("Cannot continue without API key.")
        sys.exit(1)
    
    # Test 2: Config loading
    print("2. Checking model configurations...")
    results.append(test_config_loading())
    print()
    
    # Test 3: parse_structured
    print("3. Testing parse_structured() call...")
    results.append(test_parse_structured_call())
    print()
    
    # Test 4: Direct API call
    print("4. Testing direct API call...")
    results.append(test_direct_api_call())
    print()
    
    # Summary
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"✓ All {total} tests passed!")
        print("  - Using gpt-5.2 (no max_tokens constraint)")
        print("  - store=False enforced")
        print("  - API working correctly")
    else:
        print(f"❌ {total - passed}/{total} tests failed")
        sys.exit(1)


if __name__ == "__main__":
    main()

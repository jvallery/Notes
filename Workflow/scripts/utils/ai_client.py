#!/usr/bin/env python3
"""
Centralized AI Client with Request/Response Logging.

This module provides:
1. A single OpenAI client factory for all scripts
2. Automatic logging of all AI requests and responses
3. Token usage tracking and cost estimation
4. Request/response persistence for debugging and audit

Usage:
    from utils.ai_client import get_client, AILogger
    from utils.config import get_model_config
    
    client = get_client()  # Instrumented OpenAI client
    model_config = get_model_config("extraction")  # Always from config
    
    # All calls are automatically logged to Workflow/logs/ai/
    response = client.chat.completions.create(
        model=model_config["model"],
        messages=[...]
    )
    
    # Or use the logger directly for more control
    with AILogger() as logger:
        response = logger.log_completion(client, model=model_config["model"], messages=[...])

Log Files:
    - Workflow/logs/ai/YYYY-MM-DD/
      - requests.jsonl      # All requests (append-only)
      - responses.jsonl     # All responses (append-only)
      - summary.json        # Daily summary stats
    - Workflow/logs/ai/latest.json  # Symlink to most recent summary
"""

import json
import os
import time
import hashlib
import threading
from datetime import datetime
from pathlib import Path
from typing import Optional, Any, Dict, List
from functools import wraps
from dataclasses import dataclass, field, asdict

# Thread-local storage for request context
_local = threading.local()


@dataclass
class AIRequest:
    """Represents a single AI API request."""
    id: str
    timestamp: str
    operation: str  # "chat.completions.create", "responses.parse", etc.
    model: str
    messages: Optional[List[Dict]] = None
    input: Optional[str] = None
    instructions: Optional[str] = None
    tools: Optional[List[Dict]] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    response_format: Optional[str] = None
    store: bool = False
    caller: Optional[str] = None  # Which script/function made the call
    context: Optional[Dict] = None  # Additional context (email file, etc.)


@dataclass
class AIResponse:
    """Represents a single AI API response."""
    request_id: str
    timestamp: str
    success: bool
    model: str
    content: Optional[str] = None
    parsed: Optional[Dict] = None
    usage: Optional[Dict] = None
    finish_reason: Optional[str] = None
    latency_ms: int = 0
    error: Optional[str] = None
    
    @property
    def tokens_prompt(self) -> int:
        return self.usage.get("prompt_tokens", 0) if self.usage else 0
    
    @property
    def tokens_completion(self) -> int:
        return self.usage.get("completion_tokens", 0) if self.usage else 0
    
    @property
    def tokens_total(self) -> int:
        return self.usage.get("total_tokens", 0) if self.usage else 0


@dataclass
class DailySummary:
    """Aggregated stats for a day's API usage."""
    date: str
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_prompt_tokens: int = 0
    total_completion_tokens: int = 0
    total_tokens: int = 0
    total_latency_ms: int = 0
    by_model: Dict[str, Dict] = field(default_factory=dict)
    by_operation: Dict[str, int] = field(default_factory=dict)
    by_caller: Dict[str, int] = field(default_factory=dict)
    estimated_cost_usd: float = 0.0
    pipeline_runs: List[Dict] = field(default_factory=list)
    
    def add_response(self, request: AIRequest, response: AIResponse):
        """Add a request/response pair to the summary."""
        self.total_requests += 1
        if response.success:
            self.successful_requests += 1
        else:
            self.failed_requests += 1
        
        self.total_prompt_tokens += response.tokens_prompt
        self.total_completion_tokens += response.tokens_completion
        self.total_tokens += response.tokens_total
        self.total_latency_ms += response.latency_ms
        
        # Track by model
        model = response.model or request.model
        if model not in self.by_model:
            self.by_model[model] = {
                "requests": 0, 
                "tokens": 0, 
                "latency_ms": 0,
                "errors": 0
            }
        self.by_model[model]["requests"] += 1
        self.by_model[model]["tokens"] += response.tokens_total
        self.by_model[model]["latency_ms"] += response.latency_ms
        if not response.success:
            self.by_model[model]["errors"] += 1
        
        # Track by operation
        if request.operation not in self.by_operation:
            self.by_operation[request.operation] = 0
        self.by_operation[request.operation] += 1
        
        # Track by caller
        caller = request.caller or "unknown"
        if caller not in self.by_caller:
            self.by_caller[caller] = 0
        self.by_caller[caller] += 1
        
        # Estimate cost (rough approximation)
        self.estimated_cost_usd = self._estimate_cost()
    
    def _estimate_cost(self) -> float:
        """Estimate cost based on model pricing (as of 2026)."""
        cost = 0.0
        pricing = {
            # Model: (input_per_1k, output_per_1k)
            "gpt-5.2": (0.003, 0.012),   # GPT-5.2 primary model
            "gpt-4o": (0.005, 0.015),
            "gpt-4o-mini": (0.00015, 0.0006),
            "gpt-4-turbo": (0.01, 0.03),
            "gpt-4": (0.03, 0.06),
            "gpt-3.5-turbo": (0.0005, 0.0015),
        }
        for model, stats in self.by_model.items():
            # Find matching pricing (partial match)
            for model_key, (input_cost, output_cost) in pricing.items():
                if model_key in model.lower():
                    # Rough split: assume 70% prompt, 30% completion
                    tokens = stats.get("tokens", 0)
                    cost += (tokens * 0.7 / 1000) * input_cost
                    cost += (tokens * 0.3 / 1000) * output_cost
                    break
        return round(cost, 4)

    def add_pipeline_run(self, stats: Dict[str, Any]):
        """Append unified pipeline run metrics."""
        self.pipeline_runs.append(stats)


class AILogger:
    """
    Centralized logger for AI API requests and responses.
    
    Logs to:
    - Workflow/logs/ai/YYYY-MM-DD/requests.jsonl
    - Workflow/logs/ai/YYYY-MM-DD/responses.jsonl
    - Workflow/logs/ai/YYYY-MM-DD/summary.json
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Singleton pattern for the logger."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        # Determine log directory
        self.workflow_dir = Path(__file__).parent.parent.parent
        self.log_dir = self.workflow_dir / "logs" / "ai"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Current day's directory
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.day_dir = self.log_dir / self.today
        self.day_dir.mkdir(exist_ok=True)
        
        # File handles
        self.requests_file = self.day_dir / "requests.jsonl"
        self.responses_file = self.day_dir / "responses.jsonl"
        self.summary_file = self.day_dir / "summary.json"
        
        # Load or create summary
        self.summary = self._load_summary()
        
        self._initialized = True
    
    def _load_summary(self) -> DailySummary:
        """Load existing summary or create new one."""
        if self.summary_file.exists():
            with open(self.summary_file) as f:
                data = json.load(f)
                return DailySummary(**data)
        return DailySummary(date=self.today)
    
    def _save_summary(self):
        """Save summary to disk."""
        with open(self.summary_file, "w") as f:
            json.dump(asdict(self.summary), f, indent=2)
        
        # Update latest symlink
        latest = self.log_dir / "latest.json"
        if latest.exists() or latest.is_symlink():
            latest.unlink()
        latest.symlink_to(self.summary_file)
    
    def _generate_id(self) -> str:
        """Generate a unique request ID."""
        timestamp = datetime.now().isoformat()
        unique = hashlib.md5(f"{timestamp}{time.time_ns()}".encode()).hexdigest()[:8]
        return f"{self.today}_{unique}"
    
    def _check_day_rollover(self):
        """Check if we need to start a new day's log."""
        today = datetime.now().strftime("%Y-%m-%d")
        if today != self.today:
            self.today = today
            self.day_dir = self.log_dir / self.today
            self.day_dir.mkdir(exist_ok=True)
            self.requests_file = self.day_dir / "requests.jsonl"
            self.responses_file = self.day_dir / "responses.jsonl"
            self.summary_file = self.day_dir / "summary.json"
            self.summary = DailySummary(date=self.today)
    
    def log_request(self, request: AIRequest):
        """Log a request to disk."""
        self._check_day_rollover()
        with open(self.requests_file, "a") as f:
            f.write(json.dumps(asdict(request), default=str) + "\n")
    
    def log_response(self, request: AIRequest, response: AIResponse):
        """Log a response and update summary."""
        self._check_day_rollover()
        with open(self.responses_file, "a") as f:
            f.write(json.dumps(asdict(response), default=str) + "\n")
        
        self.summary.add_response(request, response)
        self._save_summary()

    def log_pipeline_stats(self, stats: Dict[str, Any]):
        """Persist unified pipeline metrics into the daily summary."""
        self._check_day_rollover()
        try:
            self.summary.add_pipeline_run(stats)
        except Exception:
            # Backward compatibility if summary lacks pipeline_runs
            if not hasattr(self.summary, "pipeline_runs"):
                self.summary.pipeline_runs = []
            self.summary.pipeline_runs.append(stats)
        self._save_summary()
    
    def log_completion(
        self,
        client,
        model: str,
        messages: List[Dict],
        caller: Optional[str] = None,
        context: Optional[Dict] = None,
        **kwargs
    ):
        """
        Wrap a chat.completions.create call with logging.
        
        Returns the response from the API.
        """
        request_id = self._generate_id()
        timestamp = datetime.now().isoformat()
        
        # Build request record
        request = AIRequest(
            id=request_id,
            timestamp=timestamp,
            operation="chat.completions.create",
            model=model,
            messages=messages,
            temperature=kwargs.get("temperature"),
            max_tokens=kwargs.get("max_tokens"),
            response_format=str(kwargs.get("response_format")) if kwargs.get("response_format") else None,
            store=kwargs.get("store", False),
            caller=caller,
            context=context,
        )
        self.log_request(request)
        
        # Make the API call
        start_time = time.time()
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            latency_ms = int((time.time() - start_time) * 1000)
            
            # Build response record
            response_record = AIResponse(
                request_id=request_id,
                timestamp=datetime.now().isoformat(),
                success=True,
                model=response.model,
                content=response.choices[0].message.content if response.choices else None,
                usage={
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens,
                } if response.usage else None,
                finish_reason=response.choices[0].finish_reason if response.choices else None,
                latency_ms=latency_ms,
            )
            self.log_response(request, response_record)
            
            return response
            
        except Exception as e:
            latency_ms = int((time.time() - start_time) * 1000)
            response_record = AIResponse(
                request_id=request_id,
                timestamp=datetime.now().isoformat(),
                success=False,
                model=model,
                error=str(e),
                latency_ms=latency_ms,
            )
            self.log_response(request, response_record)
            raise
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def get_stats(self) -> Dict:
        """Get current day's stats."""
        return asdict(self.summary)


class InstrumentedClient:
    """
    Wrapper around OpenAI client that logs all API calls.
    
    This is a drop-in replacement for the OpenAI client.
    """
    
    def __init__(self, client, caller: Optional[str] = None):
        self._client = client
        self._caller = caller
        self._logger = AILogger()
        self.chat = InstrumentedChat(client.chat, self._logger, caller)
        # Expose responses API (for web search and other tools)
        self.responses = InstrumentedResponses(client.responses, self._logger, caller) if hasattr(client, 'responses') else None
        # Expose other client attributes
        self.models = client.models
        self.files = client.files if hasattr(client, 'files') else None
    
    def set_caller(self, caller: str):
        """Set the caller context for subsequent requests."""
        self._caller = caller
        self.chat._caller = caller
        if self.responses:
            self.responses._caller = caller
    
    def set_context(self, context: Dict):
        """Set additional context for subsequent requests."""
        self.chat._context = context


class InstrumentedChat:
    """Instrumented wrapper for chat completions."""
    
    def __init__(self, chat, logger: AILogger, caller: Optional[str] = None):
        self._chat = chat
        self._logger = logger
        self._caller = caller
        self._context = None
        self.completions = InstrumentedCompletions(chat.completions, logger, caller)
    

class InstrumentedCompletions:
    """Instrumented wrapper for completions API."""
    
    def __init__(self, completions, logger: AILogger, caller: Optional[str] = None):
        self._completions = completions
        self._logger = logger
        self._caller = caller
        self._context = None
    
    def create(self, **kwargs):
        """Logged wrapper for chat.completions.create."""
        return self._logger.log_completion(
            client=type('obj', (object,), {'chat': type('chat', (object,), {'completions': self._completions})()})(),
            model=kwargs.pop("model"),
            messages=kwargs.pop("messages"),
            caller=self._caller,
            context=self._context,
            **kwargs
        )


class InstrumentedResponses:
    """Instrumented wrapper for OpenAI Responses API (supports web_search and other tools)."""
    
    def __init__(self, responses, logger: AILogger, caller: Optional[str] = None):
        self._responses = responses
        self._logger = logger
        self._caller = caller
    
    def create(self, **kwargs):
        """
        Logged wrapper for responses.create.
        
        Supports tools like web_search_preview for real-time web access.
        """
        import time
        start_time = time.time()
        
        # Create request record
        request_id = hashlib.md5(f"{time.time()}{kwargs}".encode()).hexdigest()[:12]
        request = AIRequest(
            id=request_id,
            timestamp=datetime.now().isoformat(),
            model=kwargs.get("model", "unknown"),
            operation="responses.create",
            caller=self._caller,
            input=str(kwargs.get("input", ""))[:500],
            instructions=kwargs.get("instructions"),
            tools=[{"type": t.get("type", "unknown")} if isinstance(t, dict) else str(t) for t in kwargs.get("tools", [])] if kwargs.get("tools") else None
        )
        
        try:
            result = self._responses.create(**kwargs)
            latency_ms = int((time.time() - start_time) * 1000)
            
            # Extract token usage if available
            usage_dict = None
            if hasattr(result, 'usage') and result.usage:
                usage_dict = {
                    "prompt_tokens": getattr(result.usage, 'input_tokens', 0),
                    "completion_tokens": getattr(result.usage, 'output_tokens', 0),
                    "total_tokens": getattr(result.usage, 'input_tokens', 0) + getattr(result.usage, 'output_tokens', 0)
                }
            
            response = AIResponse(
                request_id=request_id,
                timestamp=datetime.now().isoformat(),
                success=True,
                model=kwargs.get("model", "unknown"),
                usage=usage_dict,
                latency_ms=latency_ms,
                content="[responses.create result]"
            )
            
            self._logger.log_request(request)
            self._logger.log_response(request, response)
            
            return result
            
        except Exception as e:
            latency_ms = int((time.time() - start_time) * 1000)
            response = AIResponse(
                request_id=request_id,
                timestamp=datetime.now().isoformat(),
                success=False,
                model=kwargs.get("model", "unknown"),
                error=str(e),
                latency_ms=latency_ms
            )
            self._logger.log_request(request)
            self._logger.log_response(request, response)
            raise


# Global client instance
_client = None
_client_lock = threading.Lock()


def get_client(caller: Optional[str] = None) -> InstrumentedClient:
    """
    Get the singleton instrumented OpenAI client.
    
    Args:
        caller: Optional identifier for the calling script/function.
                This is logged with each request for debugging.
    
    Returns:
        InstrumentedClient: A wrapped OpenAI client that logs all calls.
    
    Example:
        from utils.ai_client import get_client
        from utils.config import get_model_config
        
        client = get_client("draft_responses.extract_email")
        model_config = get_model_config("extraction")
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[{"role": "user", "content": "Hello"}]
        )
    """
    global _client
    
    with _client_lock:
        if _client is None:
            from openai import OpenAI
            
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                # Try loading from .env
                workflow_dir = Path(__file__).parent.parent.parent
                env_file = workflow_dir / ".env"
                if env_file.exists():
                    from dotenv import load_dotenv
                    load_dotenv(env_file)
                    api_key = os.environ.get("OPENAI_API_KEY")
            
            if not api_key:
                raise ValueError(
                    "OPENAI_API_KEY not set. "
                    "Set it in environment or Workflow/.env"
                )
            
            raw_client = OpenAI(api_key=api_key)
            _client = InstrumentedClient(raw_client, caller)
        
        if caller:
            _client.set_caller(caller)
        
        return _client


def get_logger() -> AILogger:
    """Get the singleton AI logger instance."""
    return AILogger()


def get_daily_stats() -> Dict:
    """Get today's API usage statistics."""
    return AILogger().get_stats()


def log_pipeline_stats(stats: Dict[str, Any]):
    """Append unified pipeline metrics to the daily AI summary."""
    AILogger().log_pipeline_stats(stats)


def get_cached_system_prompt(
    task: str = "general",
    include_persona: bool = True,
    include_glossary: bool = True,
    additional_instructions: str = ""
) -> str:
    """
    Get a system prompt optimized for OpenAI prompt caching.
    
    The prompt is structured with static content FIRST (persona, glossary)
    and task-specific instructions at the end, enabling cache hits on
    repeated calls with the same prefix.
    
    Args:
        task: Task type - "email_draft", "extraction", "planning", "general"
        include_persona: Include Jason's persona (for drafting tasks)
        include_glossary: Include people/project/customer glossary
        additional_instructions: Task-specific instructions (added last)
    
    Returns:
        Complete system prompt string (~2000+ tokens for cache eligibility)
    
    Usage:
        from utils.ai_client import get_client, get_cached_system_prompt
        from utils.config import get_model_config
        
        client = get_client("my_script")
        model_config = get_model_config("extraction")
        system_prompt = get_cached_system_prompt(task="email_draft")
        
        response = client.chat.completions.create(
            model=model_config["model"],
            messages=[
                {"role": "system", "content": system_prompt},  # Cached
                {"role": "user", "content": user_content}  # Dynamic
            ],
            store=False
        )
    """
    try:
        from utils.cached_prompts import get_system_prompt
        return get_system_prompt(
            task=task,
            include_persona=include_persona,
            include_glossary=include_glossary,
            additional_instructions=additional_instructions
        )
    except ImportError:
        # Fallback if cached_prompts module not available
        return additional_instructions or "You are a helpful assistant."


def reset_client():
    """Reset the global client (for testing)."""
    global _client
    _client = None


# For backwards compatibility, also export a simple function
def get_openai_client(caller: Optional[str] = None):
    """
    Backwards-compatible function that returns an instrumented client.
    
    This can be used as a drop-in replacement for the old get_openai_client()
    functions scattered across the codebase.
    """
    return get_client(caller)

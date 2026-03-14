from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Optional
import os


@dataclass
class LLMConfig:
    """Basic configuration for LLM clients, shared across projects."""

    provider: str = os.getenv("LLM_PROVIDER", "openai")
    model: str = os.getenv("LLM_MODEL", "gpt-4.1-mini")
    api_key: Optional[str] = os.getenv("LLM_API_KEY")


@dataclass
class AppConfig:
    """Top-level configuration used by individual projects."""

    env: str = os.getenv("APP_ENV", "dev")
    llm: LLMConfig = field(default_factory=LLMConfig)


def load_config() -> AppConfig:
    """
    Lightweight config loader.

    Projects can call this to get a structured configuration object without
    depending on any specific framework.
    """

    return AppConfig()


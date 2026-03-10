"""
Shared utilities for the AgenticSuite projects.

This package is intentionally minimal and framework-agnostic so it can be
reused across CrewAI, LangGraph, AutoGen, LlamaIndex, and FastAPI-based code.
"""

from .config import AppConfig, LLMConfig, load_config

__all__ = ["AppConfig", "LLMConfig", "load_config"]


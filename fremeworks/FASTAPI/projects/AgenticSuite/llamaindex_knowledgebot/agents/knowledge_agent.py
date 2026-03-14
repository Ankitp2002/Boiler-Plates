from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class KnowledgeAgent:
    """
    LlamaIndex-inspired "knowledge" agent skeleton.

    This intentionally avoids building a real index in the skeleton so it runs
    without external services. Swap the placeholder methods with real LlamaIndex
    ingestion + query pipelines when you're ready.
    """

    index_path: str

    def ingest(self) -> str:
        return f"Ingestion stub: would build/update index at {self.index_path}"

    def answer(self, question: str) -> str:
        return (
            "Answer stub: wire up a retriever + LLM to answer questions.\n"
            f"Question: {question}\n"
            f"(Index: {self.index_path})"
        )

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import mcp_integration_notes.bootstrap  # noqa: F401

from llamaindex_knowledgebot.agents.knowledge_agent import KnowledgeAgent


@dataclass
class KnowledgeBotAdapter:
    """
    MCP-like adapter for KnowledgeBot.
    """

    agent: KnowledgeAgent

    def answer_question(self, question: str) -> str:
        return self.agent.answer(question)


def build_default_knowledgebot_adapter() -> KnowledgeBotAdapter:
    suite_root = Path(__file__).resolve().parents[2]
    index_path = str(suite_root / "llamaindex_knowledgebot" / "data" / "index_placeholder.json")
    return KnowledgeBotAdapter(agent=KnowledgeAgent(index_path=index_path))


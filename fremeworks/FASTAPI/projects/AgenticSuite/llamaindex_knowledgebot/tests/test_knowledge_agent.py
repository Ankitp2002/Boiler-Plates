from __future__ import annotations

import bootstrap  # noqa: F401

from llamaindex_knowledgebot.agents.knowledge_agent import KnowledgeAgent


def test_answer_is_returned() -> None:
    agent = KnowledgeAgent(index_path="dummy.json")
    out = agent.answer("What is an index?")
    assert "Question:" in out


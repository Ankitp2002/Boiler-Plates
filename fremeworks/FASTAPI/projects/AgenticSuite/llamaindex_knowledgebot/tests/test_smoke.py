from __future__ import annotations

from pathlib import Path

from agents.knowledge_agent import KnowledgeAgent, KnowledgeQueryRequest


def test_knowledge_agent_stub_query() -> None:
    """
    Basic smoke test to show the KnowledgeAgent skeleton works.
    """

    index_path = Path("data/index_placeholder.json")

    def _stub_retriever(query: str):
        return {"query": query, "source": "test-stub"}

    agent = KnowledgeAgent(index_path=index_path, retrieve_fn=_stub_retriever)

    request = KnowledgeQueryRequest(query="What is this project?", top_k=1)
    response = agent.query(request)

    assert "KnowledgeBot" in response.answer
    assert response.sources


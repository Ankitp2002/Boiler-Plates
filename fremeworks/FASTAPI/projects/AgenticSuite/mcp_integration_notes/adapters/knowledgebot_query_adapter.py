from __future__ import annotations

from typing import Any, Dict, List, Protocol, TypedDict


class KnowledgeSourceDict(TypedDict):
    """
    Simple JSON representation of a retrieved knowledge source.
    """

    id: str
    snippet: str
    score: float


class KnowledgeQueryInput(TypedDict, total=False):
    """
    Minimal input payload for a KnowledgeBot query.
    """

    query: str
    top_k: int
    namespace: str


class KnowledgeQueryOutput(TypedDict):
    """
    Output payload returned to an MCP-style client.
    """

    answer: str
    sources: List[KnowledgeSourceDict]


class KnowledgeBotClient(Protocol):
    """
    Protocol describing the minimal interface a KnowledgeBot client should
    implement. The concrete implementation can wrap LlamaIndex or any other
    RAG library.
    """

    async def query(
        self, *, query: str, top_k: int | None = None, namespace: str | None = None
    ) -> KnowledgeQueryOutput:
        ...


class KnowledgeBotMCPAdapter:
    """
    MCP-style adapter that wraps a `KnowledgeBotClient` and exposes it as a
    `knowledgebot.query` tool.

    This adapter deliberately does not depend on LlamaIndex directly; instead it
    expects a small client object that hides the underlying retrieval details.
    """

    tool_name: str = "knowledgebot.query"
    tool_description: str = (
        "Query a knowledge index and return a synthesized answer along with "
        "the most relevant supporting sources."
    )

    def __init__(self, client: KnowledgeBotClient) -> None:
        self._client = client

    async def run(self, payload: KnowledgeQueryInput) -> KnowledgeQueryOutput:
        """
        Execute a knowledge query using the underlying client.
        """
        query = payload["query"]
        top_k = payload.get("top_k")
        namespace = payload.get("namespace")

        return await self._client.query(
            query=query,
            top_k=top_k,
            namespace=namespace,
        )

    def tool_metadata(self) -> Dict[str, Any]:
        """
        Lightweight metadata that an MCP host could expose to clients for
        discovery and schema introspection.
        """
        return {
            "name": self.tool_name,
            "description": self.tool_description,
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "top_k": {"type": "integer", "minimum": 1},
                    "namespace": {"type": "string"},
                },
                "required": ["query"],
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "answer": {"type": "string"},
                    "sources": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "snippet": {"type": "string"},
                                "score": {"type": "number"},
                            },
                            "required": ["id", "snippet", "score"],
                        },
                    },
                },
                "required": ["answer", "sources"],
            },
        }


__all__ = [
    "KnowledgeBotMCPAdapter",
    "KnowledgeBotClient",
    "KnowledgeQueryInput",
    "KnowledgeQueryOutput",
    "KnowledgeSourceDict",
]


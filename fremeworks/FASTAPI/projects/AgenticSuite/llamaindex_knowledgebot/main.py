from __future__ import annotations

from pathlib import Path

import bootstrap  # noqa: F401

from shared import load_config
from llamaindex_knowledgebot.agents.knowledge_agent import KnowledgeAgent


def main() -> None:
    config = load_config()
    print(f"Env: {config.env} | KnowledgeBot (LlamaIndex-style skeleton)")

    project_root = Path(__file__).resolve().parent
    index_path = str(project_root / "data" / "index_placeholder.json")
    agent = KnowledgeAgent(index_path=index_path)

    print(agent.ingest())
    print()
    print(agent.answer("What is RAG?"))


if __name__ == "__main__":
    main()

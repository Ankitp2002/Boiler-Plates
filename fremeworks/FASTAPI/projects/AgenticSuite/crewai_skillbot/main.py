from __future__ import annotations

import asyncio

import bootstrap  # noqa: F401

from shared import load_config
from schemas.skill import SkillRunRequest
from orchestrator.crew_orchestrator import build_default_crew


async def main() -> None:
    """
    Simple CLI entrypoint that runs a dummy SkillBot session.
    """

    config = load_config()
    print(f"Using environment: {config.env}, LLM provider: {config.llm.provider}")

    request = SkillRunRequest(
        topic_name="Agentic Frameworks",
        goal="Prepare for interviews by understanding CrewAI, LangGraph, AutoGen, and LlamaIndex.",
    )

    crew = build_default_crew()
    result = await crew.run(request)

    print("\n=== SkillBot Plan ===")
    print(f"Topic: {result.topic.name}")
    print("\nResources:")
    for r in result.plan.resources:
        print(f"- {r}")
    print("\nPractice Tasks:")
    for t in result.plan.practice_tasks:
        print(f"- {t}")
    print("\nCode Exercises:")
    for c in result.plan.code_exercises:
        print(f"- {c}")


if __name__ == "__main__":
    asyncio.run(main())


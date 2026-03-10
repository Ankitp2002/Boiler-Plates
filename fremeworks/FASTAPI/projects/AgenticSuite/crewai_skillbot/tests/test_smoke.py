from __future__ import annotations

import asyncio

import bootstrap  # noqa: F401

from orchestrator.crew_orchestrator import build_default_crew
from schemas.skill import SkillRunRequest


def test_skillbot_crew_runs() -> None:
    crew = build_default_crew()
    request = SkillRunRequest(topic_name="Python", goal="Review core concepts.")

    async def _run():
        return await crew.run(request)

    result = asyncio.run(_run())

    assert result.topic.name == "Python"
    assert result.plan.resources


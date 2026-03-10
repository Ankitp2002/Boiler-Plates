from __future__ import annotations

import bootstrap  # noqa: F401

from autogen_mentorbot.agents.mentor_agent import MentorAgent


def test_plan_contains_sections() -> None:
    agent = MentorAgent()
    plan = agent.propose_plan(topic="LangGraph", goal="Learn basics", level="beginner", timeframe="2 days")
    assert "plan" in plan and plan["plan"]
    assert "exercise" in plan and plan["exercise"]
    assert "questions" in plan and plan["questions"]


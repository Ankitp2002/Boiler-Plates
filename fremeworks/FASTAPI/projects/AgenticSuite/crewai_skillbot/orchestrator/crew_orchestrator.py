from __future__ import annotations

from dataclasses import dataclass

from agents import TrendAgent, ResearchAgent, PracticeAgent, CodeAgent
from schemas.skill import SkillRunRequest, SkillRunResult, SkillTopic, SkillPlan


@dataclass
class SkillBotCrew:
    """
    High-level orchestration of the SkillBot crew.

    Mirrors the idea from `CrewAI.md`:
    - TrendAgent → discover trends
    - ResearchAgent → gather details
    - PracticeAgent → design practice
    - CodeAgent → propose code exercises
    """

    trend_agent: TrendAgent
    research_agent: ResearchAgent
    practice_agent: PracticeAgent
    code_agent: CodeAgent

    async def run(self, request: SkillRunRequest) -> SkillRunResult:
        topic = SkillTopic(name=request.topic_name, description=request.goal)

        trends = await self.trend_agent.find_trends(topic.name)
        notes = await self.research_agent.research(topic.name, trends)
        practice_tasks = await self.practice_agent.design_practice(topic.name, notes)
        code_exercises = await self.code_agent.propose_exercises(topic.name, practice_tasks)

        plan = SkillPlan(
            topic=topic,
            resources=trends,
            practice_tasks=practice_tasks,
            code_exercises=code_exercises,
        )

        return SkillRunResult(topic=topic, plan=plan)


def build_default_crew() -> SkillBotCrew:
    """Factory for a default in-memory crew."""

    return SkillBotCrew(
        trend_agent=TrendAgent(),
        research_agent=ResearchAgent(),
        practice_agent=PracticeAgent(),
        code_agent=CodeAgent(),
    )


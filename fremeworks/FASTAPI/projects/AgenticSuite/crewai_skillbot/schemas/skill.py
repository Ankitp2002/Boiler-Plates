from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SkillTopic:
    """Represents a single topic/skill the bot should learn."""

    name: str
    description: Optional[str] = None
    difficulty: str = "intermediate"


@dataclass
class SkillPlan:
    """Aggregate learning plan coming out of the crew."""

    topic: SkillTopic
    resources: List[str] = field(default_factory=list)
    practice_tasks: List[str] = field(default_factory=list)
    code_exercises: List[str] = field(default_factory=list)


@dataclass
class SkillRunRequest:
    """Input for a SkillBot run."""

    topic_name: str
    goal: str


@dataclass
class SkillRunResult:
    """High-level result of a SkillBot run."""

    topic: SkillTopic
    plan: SkillPlan


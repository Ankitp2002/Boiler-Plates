from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class CodeAgent:
    """
    Stub CodeAgent that would normally help write and review code exercises.
    """

    name: str = "CodeAgent"

    async def propose_exercises(self, topic: str, practice_tasks: List[str]) -> List[str]:
        """Produce lightweight code exercise prompts."""

        return [
            f"Code exercise for '{topic}': Turn this into code – {task}"
            for task in practice_tasks
        ]


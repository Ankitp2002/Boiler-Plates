from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TrendAgent:
    """
    Stub TrendAgent inspired by your CrewAI notes.

    In a full implementation this would likely wrap a `crewai.Agent` that can
    browse the web, scan docs, and identify trending subtopics and tools.
    """

    name: str = "TrendAgent"

    async def find_trends(self, topic: str) -> List[str]:
        """Return a placeholder list of trends for the given topic."""

        return [
            f"{topic} – foundational patterns",
            f"{topic} – current best practices",
            f"{topic} – common interview questions",
        ]


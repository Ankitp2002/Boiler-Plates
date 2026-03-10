from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class ResearchAgent:
    """
    Stub ResearchAgent that would normally go deeper on each trend.
    """

    name: str = "ResearchAgent"

    async def research(self, topic: str, trends: List[str]) -> List[str]:
        """Produce placeholder research notes for each trend."""

        return [f"Notes for '{trend}' under topic '{topic}'." for trend in trends]


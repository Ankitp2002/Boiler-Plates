from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class PracticeAgent:
    """
    Stub PracticeAgent that turns research into practice tasks.
    """

    name: str = "PracticeAgent"

    async def design_practice(self, topic: str, notes: List[str]) -> List[str]:
        """Return simple practice tasks derived from notes."""

        return [f"Practice: Implement an example for '{topic}' based on: {note}" for note in notes]


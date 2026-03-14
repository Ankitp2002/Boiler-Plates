from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class MentorAgent:
    """
    AutoGen-inspired conversational mentor skeleton.

    This is intentionally tool-free and LLM-free by default: it demonstrates how
    you'd separate conversation state and decision-making from side effects.
    """

    name: str = "MentorAgent"

    def propose_plan(self, topic: str, goal: str, level: str, timeframe: str) -> Dict[str, List[str]]:
        return {
            "plan": [
                f"Define what success means for: {topic}",
                "Learn core terms + one minimal example",
                "Build a small project skeleton and iterate",
            ],
            "exercise": [
                f"Write a 10-line summary of {topic} and implement one tiny demo related to your goal.",
            ],
            "questions": [
                f"What does '{goal}' mean for you in practice?",
                f"Which part feels hardest at your current level ({level})?",
                f"How much time do you have ({timeframe}) and by when?",
            ],
        }

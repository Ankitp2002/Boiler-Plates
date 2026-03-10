from __future__ import annotations

import json
from pathlib import Path

import bootstrap  # noqa: F401

from shared import load_config
from autogen_mentorbot.agents.mentor_agent import MentorAgent


def load_flow() -> dict:
    flow_path = Path(__file__).parent / "conversations" / "conversation_flow.json"
    return json.loads(flow_path.read_text(encoding="utf-8"))


def main() -> None:
    config = load_config()
    print(f"Env: {config.env} | MentorBot (AutoGen-style skeleton)")

    _ = load_flow()
    agent = MentorAgent()

    topic = input("Topic: ").strip()
    if not topic:
        topic = "Agentic systems"
    goal = input("Goal (one sentence): ").strip() or "Interview readiness"
    level = input("Level (beginner/intermediate/advanced): ").strip() or "intermediate"
    timeframe = input("Timeframe (e.g. 1 week): ").strip() or "1 week"

    plan = agent.propose_plan(topic=topic, goal=goal, level=level, timeframe=timeframe)
    print("\nPlan:")
    for item in plan["plan"]:
        print(f"- {item}")
    print("\nExercise:")
    for item in plan["exercise"]:
        print(f"- {item}")
    print("\nQuestions:")
    for item in plan["questions"]:
        print(f"- {item}")

    while True:
        msg = input("\nType a follow-up (or 'exit'): ").strip()
        if msg.lower() in {"exit", "quit"}:
            break
        print("MentorBot: Let's refine that — what outcome do you want from this follow-up?")


if __name__ == "__main__":
    main()

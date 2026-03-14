from __future__ import annotations

import asyncio
import json
from pathlib import Path

import bootstrap  # noqa: F401

from shared import load_config
from langgraph_taskflow.agents.task_agent import TaskAgent
from langgraph_taskflow.graph.workflow_graph import TaskNode, TaskStatus, WorkflowGraph


def load_sample_graph() -> WorkflowGraph:
    data_path = Path(__file__).parent / "data" / "graph_state.json"
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    tasks = [
        TaskNode(
            id=t["id"],
            title=t["title"],
            status=TaskStatus(t["status"]),
            depends_on=list(t.get("depends_on") or []),
        )
        for t in payload["tasks"]
    ]
    return WorkflowGraph(tasks)


async def run_simulation() -> None:
    config = load_config()
    print(f"Env: {config.env} | Simulating a LangGraph-like task flow")

    graph = load_sample_graph()
    agent = TaskAgent()

    while True:
        next_task = graph.next_runnable()
        if not next_task:
            break
        print(f"\nStarting task: {next_task.id} - {next_task.title}")
        graph.start(next_task.id)
        result = await agent.execute(next_task)
        graph.complete(next_task.id)
        print(f"Completed task: {result}")

    print("\nFinal statuses:")
    for t in graph.tasks():
        print(f"- {t.id}: {t.status}")


if __name__ == "__main__":
    asyncio.run(run_simulation())

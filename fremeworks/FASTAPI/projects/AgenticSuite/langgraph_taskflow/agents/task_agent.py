from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from langgraph_taskflow.graph.workflow_graph import TaskNode


@dataclass
class TaskAgent:
    """
    Placeholder "executor" for a task node.

    In a real LangGraph setup, this would be a node function that consumes and
    returns state, potentially calling tools/LLMs.
    """

    name: str = "TaskAgent"

    async def execute(self, task: TaskNode) -> Dict[str, Any]:
        return {"task_id": task.id, "result": f"Executed: {task.title}"}

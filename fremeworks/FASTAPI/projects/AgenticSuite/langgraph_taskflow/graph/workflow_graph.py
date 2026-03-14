from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


@dataclass
class TaskNode:
    id: str
    title: str
    status: TaskStatus = TaskStatus.TODO
    depends_on: List[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.depends_on is None:
            self.depends_on = []


class WorkflowGraph:
    """
    Minimal "task graph" inspired by your `LangGraph.md` notes.

    This is intentionally lightweight (no external dependencies required) but
    shaped like a stateful graph you could migrate into real `langgraph` nodes.
    """

    def __init__(self, tasks: List[TaskNode]) -> None:
        self._tasks: Dict[str, TaskNode] = {t.id: t for t in tasks}

    def get_task(self, task_id: str) -> TaskNode:
        return self._tasks[task_id]

    def tasks(self) -> List[TaskNode]:
        return list(self._tasks.values())

    def can_start(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        return all(self.get_task(dep).status == TaskStatus.DONE for dep in task.depends_on)

    def start(self, task_id: str) -> None:
        task = self.get_task(task_id)
        if not self.can_start(task_id):
            raise ValueError(f"Task '{task_id}' cannot start until dependencies are DONE.")
        task.status = TaskStatus.IN_PROGRESS

    def complete(self, task_id: str) -> None:
        task = self.get_task(task_id)
        task.status = TaskStatus.DONE

    def next_runnable(self) -> Optional[TaskNode]:
        for task in self.tasks():
            if task.status == TaskStatus.TODO and self.can_start(task.id):
                return task
        return None

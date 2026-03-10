from __future__ import annotations

import bootstrap  # noqa: F401

from langgraph_taskflow.graph.workflow_graph import TaskNode, TaskStatus, WorkflowGraph


def test_next_runnable_respects_dependencies() -> None:
    g = WorkflowGraph(
        [
            TaskNode(id="a", title="A", status=TaskStatus.DONE),
            TaskNode(id="b", title="B", status=TaskStatus.TODO, depends_on=["a"]),
        ]
    )
    nxt = g.next_runnable()
    assert nxt is not None
    assert nxt.id == "b"


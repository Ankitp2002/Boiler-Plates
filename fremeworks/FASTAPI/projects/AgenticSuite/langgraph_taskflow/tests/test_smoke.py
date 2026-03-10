from __future__ import annotations

import asyncio

from graph.workflow_graph import TaskGraph, TaskState
from agents.task_agent import TaskExecutionAgent


def test_taskflow_graph_reaches_done() -> None:
    graph = TaskGraph()
    graph.add_task("t1", description="First")
    graph.add_task("t2", description="Second", depends_on=["t1"])

    agent = TaskExecutionAgent()

    async def _run() -> None:
        await agent.run_until_complete(graph)

    asyncio.run(_run())

    assert graph.get_task("t1").state is TaskState.DONE
    assert graph.get_task("t2").state is TaskState.DONE


from __future__ import annotations

from dataclasses import dataclass

import mcp_integration_notes.bootstrap  # noqa: F401

from gp_system_agentic.schemas.consultation import ConsultationRequest, ConsultationResponse
from gp_system_agentic.orchestrator.gp_orchestrator import GPOrchestrator, build_default_gp_orchestrator


@dataclass
class GPSystemAdapter:
    """
    MCP-like adapter for the GP System.

    In a real MCP tool server, `consult_gp` would be registered as a tool
    callable by agents. The adapter keeps the surface stable and typed.
    """

    orchestrator: GPOrchestrator

    async def consult_gp(self, request: ConsultationRequest) -> ConsultationResponse:
        return await self.orchestrator.run(request)


def build_default_gp_adapter() -> GPSystemAdapter:
    return GPSystemAdapter(orchestrator=build_default_gp_orchestrator())


from __future__ import annotations

from typing import Any, Dict, TypedDict

from gp_system_agentic.orchestrator.gp_orchestrator import run_gp_consultation
from gp_system_agentic.schemas.consultation import (
    ConsultationRequest,
    ConsultationResponse,
)


class GPConsultInput(TypedDict, total=False):
    """
    Minimal JSON shape for a GP consultation request as seen by an MCP-style tool
    host. This mirrors `ConsultationRequest` but stays dict-based for transport.
    """

    patient_id: str
    symptoms: str
    history: str


class GPConsultOutput(TypedDict):
    """
    Minimal JSON shape for a GP consultation response returned to an MCP-style
    client. This mirrors `ConsultationResponse` in a JSON-friendly form.
    """

    report: str
    analysis_summary: str
    analysis_red_flags: list[str]


class GPConsultationMCPAdapter:
    """
    Thin adapter that exposes `run_gp_consultation` as an MCP-style tool.

    It accepts and returns plain dicts so it can be wired into a JSON-RPC or
    socket-based MCP server without depending on FastAPI.
    """

    tool_name: str = "gp.consult"
    tool_description: str = (
        "Run a multi-agent GP consultation (Doctor + Reporter) and return a "
        "structured analysis plus a natural-language report."
    )

    async def run(self, payload: GPConsultInput) -> GPConsultOutput:
        """
        Execute the GP consultation flow using the underlying orchestrator.

        In a full MCP implementation, `payload` would come from a decoded
        JSON-RPC request and this method would be invoked by the MCP host.
        """
        request = ConsultationRequest(**payload)  # type: ignore[arg-type]
        response: ConsultationResponse = await run_gp_consultation(request)

        return GPConsultOutput(
            report=response.report,
            analysis_summary=response.analysis.summary,
            analysis_red_flags=list(response.analysis.red_flags or []),
        )

    def tool_metadata(self) -> Dict[str, Any]:
        """
        Lightweight metadata that an MCP host could expose to clients for
        discovery and schema introspection.
        """
        return {
            "name": self.tool_name,
            "description": self.tool_description,
            "input_schema": {
                "type": "object",
                "properties": {
                    "patient_id": {"type": "string", "nullable": True},
                    "symptoms": {"type": "string"},
                    "history": {"type": "string", "nullable": True},
                },
                "required": ["symptoms"],
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "report": {"type": "string"},
                    "analysis_summary": {"type": "string"},
                    "analysis_red_flags": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["report", "analysis_summary", "analysis_red_flags"],
            },
        }


__all__ = ["GPConsultationMCPAdapter", "GPConsultInput", "GPConsultOutput"]


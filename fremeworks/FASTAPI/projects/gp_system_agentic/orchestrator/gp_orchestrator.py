from __future__ import annotations

from dataclasses import dataclass

from agents.gp_agents import DoctorAgent, DummyLLMClient, ReportAgent
from schemas.consultation import ConsultationRequest, ConsultationResponse, DoctorAnalysis


@dataclass
class GPOrchestrator:
    """
    Orchestrates the GP consultation as a simple two-node flow:

    1. Doctor agent performs analysis.
    2. Report agent generates a textual report.

    This mirrors a tiny LangGraph-style sequence while remaining framework-agnostic.
    """

    doctor_agent: DoctorAgent
    report_agent: ReportAgent

    async def run(self, request: ConsultationRequest) -> ConsultationResponse:
        analysis_dict = await self.doctor_agent.analyze(
            symptoms=request.symptoms,
            history=request.history,
        )

        report_text = await self.report_agent.write_report(analysis_dict)

        analysis = DoctorAnalysis(
            summary=analysis_dict["summary"],
            red_flags=analysis_dict.get("red_flags", []),
        )

        return ConsultationResponse(analysis=analysis, report=report_text)


def build_default_gp_orchestrator() -> GPOrchestrator:
    """
    Factory that wires together the default GP orchestrator.

    For now, this uses a dummy in-memory LLM client implementation. In a real
    deployment, this factory would be updated to construct a client using
    environment-driven configuration (see the shared config module).
    """

    llm_client = DummyLLMClient()
    doctor_agent = DoctorAgent(llm_client=llm_client)
    report_agent = ReportAgent(llm_client=llm_client)

    return GPOrchestrator(doctor_agent=doctor_agent, report_agent=report_agent)

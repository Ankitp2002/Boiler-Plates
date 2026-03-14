from __future__ import annotations

from fastapi import APIRouter, Depends

from orchestrator.gp_orchestrator import GPOrchestrator, build_default_gp_orchestrator
from schemas.consultation import ConsultationRequest, ConsultationResponse


router = APIRouter(tags=["gp_consultation"])


def get_gp_orchestrator() -> GPOrchestrator:
    """
    FastAPI dependency that provides a GP orchestrator instance.

    This is where environment-specific wiring can happen (e.g. choosing
    different LLM providers or passing in shared config objects).
    """

    return build_default_gp_orchestrator()


@router.post("/consult", response_model=ConsultationResponse)
async def consult(
    request: ConsultationRequest,
    orchestrator: GPOrchestrator = Depends(get_gp_orchestrator),
) -> ConsultationResponse:
    """
    Entry point for the GP multi-agent consultation.
    """
    return await orchestrator.run(request)

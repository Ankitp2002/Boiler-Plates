from fastapi import APIRouter

from schema import InferenceRequest, InferenceResult
from orchestrator import orchestrate_inference


router = APIRouter(prefix="/ml", tags=["ML Orchestration"])


@router.get("")
async def initiate_model_inference() -> str:
    """
    Simple ping endpoint for the ML orchestration subsystem.
    """
    return "ML orchestration is up."


@router.post("/infer", response_model=InferenceResult)
async def run_inference(request: InferenceRequest) -> InferenceResult:
    """
    Run a toy 'idealogistic' ML pipeline in an isolated interpreter/process.
    """
    return await orchestrate_inference(request)


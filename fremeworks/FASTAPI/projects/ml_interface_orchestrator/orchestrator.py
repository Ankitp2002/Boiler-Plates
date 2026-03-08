from typing import Dict, Any

from schema import InferenceRequest, InferenceResult
from parellel_execution import execute_parallel_with_interpreter_pool


def _ml_worker(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Synchronous 'ML' worker that runs in a separate interpreter/process.

    This is intentionally simple and self-contained so it can be safely
    executed in a different interpreter without sharing state.
    """
    text: str = payload["text"]
    task: str = payload["task"]
    request_id = payload.get("request_id")

    words = text.split()
    length = len(text)
    word_count = len(words)

    if task == "sentiment":
        # Very naive, purely illustrative sentiment heuristic
        positive_tokens = {"good", "great", "excellent", "love", "awesome"}
        negative_tokens = {"bad", "terrible", "awful", "hate", "horrible"}

        positives = sum(1 for w in words if w.lower() in positive_tokens)
        negatives = sum(1 for w in words if w.lower() in negative_tokens)

        raw_score = positives - negatives
        score = max(min(raw_score / 5.0, 1.0), -1.0)

        summary = (
            "Text is overall positive"
            if score > 0
            else "Text is overall negative"
            if score < 0
            else "Text is neutral"
        )
    else:
        # length_analysis
        score = float(word_count)
        summary = f"Text has {word_count} words and {length} characters."

    return {
        "request_id": request_id,
        "task": task,
        "summary": summary,
        "score": float(score),
    }


async def orchestrate_inference(request: InferenceRequest) -> InferenceResult:
    """
    Public async API: orchestrate ML inference in an isolated interpreter.
    """
    payload = request.model_dump()
    result_dict = await execute_parallel_with_interpreter_pool(_ml_worker, payload)
    return InferenceResult(**result_dict)


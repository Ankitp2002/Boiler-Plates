from pydantic import BaseModel
from typing import Literal, Optional


class InferenceRequest(BaseModel):
    """
    Simple, 'idealogistic' ML request schema.

    You can extend this later with real model names, hyperparameters, etc.
    """

    text: str
    task: Literal["sentiment", "length_analysis"] = "sentiment"
    request_id: Optional[str] = None


class InferenceResult(BaseModel):
    request_id: Optional[str]
    task: str
    summary: str
    score: float


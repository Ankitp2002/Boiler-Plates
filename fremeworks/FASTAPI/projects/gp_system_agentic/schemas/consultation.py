from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ConsultationRequest(BaseModel):
    patient_id: Optional[str] = None
    symptoms: str
    history: Optional[str] = None


class DoctorAnalysis(BaseModel):
    summary: str
    red_flags: List[str] = Field(default_factory=list)


class ConsultationResponse(BaseModel):
    analysis: DoctorAnalysis
    report: str


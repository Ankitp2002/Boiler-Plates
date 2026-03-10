from __future__ import annotations

from typing import Any, Dict, Protocol, runtime_checkable


@runtime_checkable
class LLMClientProtocol(Protocol):
    """
    Minimal async LLM client protocol.

    The concrete implementation (OpenAI, local model, etc.) is injected
    from the outside so agents stay framework-agnostic.
    """

    async def acomplete(self, prompt: str) -> str:  # pragma: no cover - skeleton only
        ...


class DoctorAgent:
    """
    Simplified stand-in for a CrewAI-style GP Medical Analyst.

    An LLM client is injected so this class can be wired to any provider.
    """

    def __init__(self, llm_client: LLMClientProtocol) -> None:
        self._llm_client = llm_client

    async def analyze(self, symptoms: str, history: str | None = None) -> Dict[str, Any]:
        # Placeholder logic; in a real project this would call self._llm_client
        red_flags: list[str] = []
        if "chest pain" in symptoms.lower():
            red_flags.append("Possible cardiac issue – needs urgent review")

        summary = f"Preliminary analysis of symptoms: {symptoms}"
        if history:
            summary += f" | History considered: {history}"

        return {
            "summary": summary,
            "red_flags": red_flags,
        }


class ReportAgent:
    """
    Simplified stand-in for a CrewAI-style Medical Report Writer.

    The LLM client is injected to keep the class decoupled from providers.
    """

    def __init__(self, llm_client: LLMClientProtocol) -> None:
        self._llm_client = llm_client

    async def write_report(self, analysis: Dict[str, Any]) -> str:
        # In a real implementation, this could assemble a prompt and call self._llm_client.
        summary = analysis.get("summary", "")
        red_flags = analysis.get("red_flags") or []

        lines: list[str] = [
            "GP Consultation Report",
            "----------------------",
            f"Analysis: {summary}",
        ]

        if red_flags:
            lines.append("")
            lines.append("Red flags:")
            for flag in red_flags:
                lines.append(f"- {flag}")

        return "\n".join(lines)


class DummyLLMClient(LLMClientProtocol):
    """
    Very small, no-op LLM client used for the interview-ready skeleton.

    It demonstrates where a real provider integration would sit without
    requiring external services or credentials.
    """

    async def acomplete(self, prompt: str) -> str:
        return f"[dummy completion] {prompt[:80]}"


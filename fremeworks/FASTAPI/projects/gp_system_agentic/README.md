# GP System Agentic Framework Project

This project is a **code template** that turns your `Agentic.MD`, `CrewAI.md`, `LangGraph.md`, `AutoGen.md`, and `MCP.MD` notes into a **working skeleton** you can extend.

It focuses on **Project 7: YOUR GP SYSTEM** from your notes:

- Multi-agent GP medical consultation
- Crew-style agents (doctor + report writer)
- Orchestrated via a backend API (FastAPI)
- Ready to extend with LangGraph, AutoGen and RAG later

## Folder Structure

```text
gp_system_agentic/
├─ app.py                 # FastAPI entrypoint
├─ requirements.txt       # Python dependencies
├─ api/
│  └─ routes.py           # HTTP routes (consult endpoint)
├─ agents/
│  └─ gp_agents.py        # DoctorAgent + ReportAgent (CrewAI-style roles)
├─ orchestrator/
│  └─ gp_orchestrator.py  # Multi-agent orchestration (idea → agents → flow)
├─ schemas/
│  └─ consultation.py      # Pydantic models for requests/responses
└─ README.md
```

This maps directly to your ideology:

- **Idea → Break into agents**: `DoctorAgent`, `ReportAgent`
- **Each agent has role + output**: encoded in `gp_agents.py`
- **Orchestrator manages flow**: `gp_orchestrator.py`
- **FastAPI exposes it as a product**: `app.py` + `api/routes.py`

## Setup

1. Create and activate virtual environment (from your Boiler-Plates.md instructions):

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   uvicorn app:app --host 127.0.0.1 --port 8001 --reload
   ```

## Usage

Send a POST request:

```http
POST /api/consult
Content-Type: application/json

{
  "patient_id": "123",
  "symptoms": "Chest pain and shortness of breath",
  "history": "Smoker, age 55"
}
```

You will receive a structured response:

```json
{
  "analysis": {
    "summary": "Preliminary analysis of symptoms: ...",
    "red_flags": [
      "Possible cardiac issue – needs urgent review"
    ]
  },
  "report": "GP Consultation Report\n----------------------\n..."
}
```

## Next Steps (Based on Your MD Notes)

- **CrewAI**: Replace `DoctorAgent` and `ReportAgent` with real `crewai.Agent` + `Task` definitions.
- **LangGraph**: Add a `graph/` folder (from `LangGraph.md`) and model this consultation as a stateful workflow graph.
- **AutoGen**: Add conversational agents in an `autogen/` module so a user can chat their way through the consultation.
- **RAG (LlamaIndex/ChromaDB)**: Plug in real medical knowledge instead of the simple placeholder logic.

This gives you a **clean starting project** that exactly reflects the patterns from your markdown notes and can be extended for interviews or real products.


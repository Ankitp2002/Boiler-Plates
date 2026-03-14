## CrewAI SkillBot

This project is a **skeleton implementation** of the SkillBot idea from `CrewAI.md`.  
It showcases a clean, interview-ready layout for a **role-based multi-agent system** built on top of CrewAI-style concepts.

### Architecture

- **`main.py`** – async CLI entrypoint that runs a sample SkillBot session.
- **`bootstrap.py`** – ensures the monorepo (`AgenticSuite/`) is on `sys.path` so the project can import shared utilities.
- **`agents/`**
  - `trend_agent.py` – discovers high-level trends for a topic.
  - `research_agent.py` – generates placeholder research notes per trend.
  - `practice_agent.py` – turns notes into practice tasks.
  - `code_agent.py` – proposes lightweight code exercises.
- **`orchestrator/crew_orchestrator.py`** – wires the agents together into a `SkillBotCrew` orchestrator.
- **`schemas/skill.py`** – typed dataclasses representing the topic, plan, and run request/result.
- **`tests/test_smoke.py`** – simple smoke test to show how the crew can be exercised.

All agents are currently **stubs**: they use simple in-memory logic and string outputs so you can focus on the architecture and control flow without needing real tools or API keys.

### Running the demo

From the repository root:

```bash
cd fremeworks/FASTAPI/projects/AgenticSuite/crewai_skillbot
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

You should see a basic learning plan printed for a hard-coded topic.

### Next steps (future work)

- Replace the stub agents with real `crewai.Agent` objects.
- Plug in web search / documentation tools for `TrendAgent` and `ResearchAgent`.
- Persist runs and logs into `data/logs.json` or an external store.
- Add FastAPI routes to expose SkillBot as an HTTP service if desired.


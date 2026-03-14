## MCP Integration Notes (Skeleton)

This folder demonstrates how you could expose the projects in `AgenticSuite/` behind an **MCP-like adapter layer**:

- Each project exposes one or more **capabilities** (e.g., `consult_gp`, `answer_question`, `run_skillbot`).
- Adapters map those capabilities to stable, typed functions.
- A real MCP server would then register these functions as tools for an agent runtime.

### Why this matters (interview framing)

- **Separation of concerns**: project internals stay independent; adapter layer defines “product API”.
- **Swappability**: you can swap implementations (CrewAI vs LangGraph) without breaking consumers.
- **Safety**: adapters are a good place for validation, rate limits, audit logs, and permissions.

### Adapters in this skeleton

- `adapters/gp_system_adapter.py`: exposes the GP consultation orchestrator.
- `adapters/knowledgebot_adapter.py`: exposes the KnowledgeBot question answering.

## MCP Integration Notes

This folder documents how to expose the projects in `AgenticSuite` behind **MCP-style adapters** so that a higher-level orchestrator (IDE plugin, central agent, or tool host) can call them in a **uniform, tool-like way**.

The goal is **not** to fully implement MCP, but to show that each project can be wrapped behind:

- **Well-defined tool metadata** (name, description, input/output schema)
- **Stable adapter classes** that convert between MCP-style JSON payloads and your internal Python types
- **Clear separation** between:
  - Transport concerns (JSON-RPC, WebSocket, HTTP)
  - Domain logic (agents, orchestrators, RAG pipelines)

---

### 1. Conceptual MCP Model for This Suite

At a high level, imagine an MCP host that can load one or more of the following **tools** from this repo:

- **`gp.consult`** – run a multi-agent GP consultation via `gp_system_agentic`
- **`knowledgebot.query`** – query a RAG-style index via `llamaindex_knowledgebot`
- **`skillbot.plan_learning`** – (future) orchestrate a learning plan via `crewai_skillbot`
- **`taskflow.simulate_project`** – (future) run a LangGraph-style project workflow simulation

Each tool:

- Declares its **name** and **description**
- Defines an **input schema** and **output schema**
- Is implemented by a small **adapter class** that:
  1. Validates or parses incoming JSON payload
  2. Calls into project-specific orchestrators or agents
  3. Returns a JSON-serializable result

This folder focuses on the first two concrete adapters:

- `gp_consultation_adapter.py` – for the GP system
- `knowledgebot_query_adapter.py` – for the LlamaIndex-style KnowledgeBot

---

### 2. Mapping Projects to MCP-Style Tools

| Project Folder               | Example MCP Tool Name     | Input (conceptual)                    | Output (conceptual)                          |
|-----------------------------|---------------------------|---------------------------------------|----------------------------------------------|
| `gp_system_agentic/`        | `gp.consult`              | Patient demographics + symptoms       | Structured GP consultation report            |
| `llamaindex_knowledgebot/`  | `knowledgebot.query`      | Natural-language question + context   | Retrieved passages + synthesized answer      |
| `crewai_skillbot/`          | `skillbot.plan_learning`  | Topic + current level                 | Suggested multi-step learning plan           |
| `langgraph_taskflow/`       | `taskflow.simulate_project`| Project outline + constraints         | Simulated task states / timeline             |

The **actual transport** (e.g., how JSON-RPC messages arrive) is intentionally left out of these stubs. Instead, you can imagine an MCP host doing something like:

1. Load adapter classes from `mcp_integration_notes/adapters/`.
2. Introspect each adapter's `tool_metadata()` method.
3. Route incoming tool calls to the adapter's `run(...)` / `__call__(...)` method.

---

### 3. Design Goals for the Adapters

**Keep adapters thin and explicit:**

- They should do **minimal translation** between:
  - Outer MCP-like JSON payloads (dicts, lists, primitives)
  - Inner domain objects (Pydantic models, orchestrators, agents)
- They should not hide heavy business logic; instead, they delegate to:
  - `gp_system_agentic.orchestrator.gp_orchestrator.GPOrchestrator`
  - Future `knowledgebot`/`crew`/`taskflow` orchestrators

**Make schemas obvious:**

- Even if you don't implement the full validation logic yet, document:
  - Required input fields
  - High-level output structure
- Use type hints and Pydantic models where appropriate so that an interviewer can quickly see how you would implement this in a real MCP deployment.

---

### 4. GP Consultation MCP Adapter (Example)

The GP system already exposes a FastAPI endpoint via `gp_system_agentic/app.py`. The MCP-style adapter adds an additional layer that can be used in:

- A headless tool-host (e.g., IDE extension, autonomous agent)
- A non-HTTP environment (e.g., pure JSON-RPC over a socket)

Conceptually, the adapter:

1. Accepts a payload shaped like your `ConsultationRequest` schema.
2. Uses `GPOrchestrator` to run the consultation flow.
3. Returns a dict shaped like `ConsultationResponse`.

The concrete stub implementation lives in:

- `adapters/gp_consultation_adapter.py`

You can wire this adapter into:

- FastAPI (reuse the same orchestrator)
- A CLI entrypoint
- An MCP server implementation

---

### 5. KnowledgeBot MCP Adapter (Example)

The KnowledgeBot project (`llamaindex_knowledgebot`) is designed as a RAG-style pipeline. An MCP-style adapter for it:

1. Accepts a payload with:
   - `query`: natural-language question
   - Optional metadata such as `top_k`, `filters`, or `namespace`
2. Delegates to a `KnowledgeBotClient` or equivalent interface that:
   - Runs retrieval over your LlamaIndex index
   - Synthesizes an answer using your configured LLM
3. Returns a dict containing:
   - `answer`: synthesized answer string
   - `sources`: list of objects with `id`, `snippet`, and `score`

The concrete stub implementation lives in:

- `adapters/knowledgebot_query_adapter.py`

This adapter is intentionally framework-agnostic. It does **not** import LlamaIndex directly; instead, it expects to be given a small client object that hides the underlying library details.

---

### 6. Folder Layout

Planned structure for this folder:

- `README.md` – this file, describing the overall MCP integration approach
- `adapters/`
  - `gp_consultation_adapter.py` – wraps the GP system as a `gp.consult` tool
  - `knowledgebot_query_adapter.py` – wraps the KnowledgeBot as a `knowledgebot.query` tool

Additional adapters can be added later (e.g., for CrewAI SkillBot and LangGraph TaskFlow) following the same pattern.

---

### 7. Next Steps / How to Extend

- **Implement real validation**:
  - Use Pydantic models in the adapters themselves or reuse existing schemas from each project.
- **Add transport**:
  - Implement a small MCP-like server that:
    - Maps incoming tool calls to adapter instances
    - Handles error propagation and logging
- **Unify configuration**:
  - Use `shared/config.py` (or a similar module) to centralize:
    - LLM provider settings
    - Index paths
    - API keys

These notes are meant to be **interview-friendly**: the code stubs are small, well-typed, and clearly show how you think about exposing heterogeneous agentic projects via a common MCP-style integration layer.


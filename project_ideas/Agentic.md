🔍 Local Web Research Agent

CONCEPTS COVERED
◆ ReAct: Reason + Act loop (how agents think)
◆ Tool use: give LLM functions it can call
◆ Memory: in-context (short) vs vector store (long)
◆ LangChain AgentExecutor with local Ollama backend

CAPSTONE PROJECT
An agent powered by Ollama (Mistral 7B) that takes a research topic, uses DuckDuckGo Search (free, no key) + Wikipedia tool, reads pages with BeautifulSoup, and writes a structured markdown report. Fully offline-capable except DuckDuckGo queries.

🏢 AI Dev Team Simulation

CONCEPTS COVERED
◆ Orchestrator-Worker pattern
◆ Agent roles, goals, and backstories (CrewAI)
◆ Agents sharing context and passing outputs
◆ Error handling and retry logic

CAPSTONE PROJECT
3 CrewAI agents: Architect (designs solution), Coder (writes Python), Reviewer (finds bugs). Give them a mini-task like 'build a to-do CLI app' — they collaborate, produce code, review it, and output a final README. Powered by Ollama locally.

💼 Resume Tailoring Agent

CONCEPTS COVERED
◆ LangGraph: stateful, graph-based agent workflows
◆ Conditional edges and looping agents
◆ Human-in-the-loop checkpoints
◆ Persisting agent state with SQLite (free)

CAPSTONE PROJECT
Paste a job description → LangGraph agent reads it (Ollama) → extracts required skills → rewrites your resume sections to match → generates a cover letter → saves outputs as .md files. All local, all free, state persisted in SQLite.

from crewai import Agent
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral:7b", temperature=0.2)

# 🏛️ Architect: Designs solution
architect = Agent(
    role="Software Architect",
    goal="Design clean, scalable Python CLI applications with proper structure",
    backstory="""15+ years designing enterprise Python systems. 
    Expert in CLI design patterns, argument parsing, file I/O, error handling.
    Always provides detailed technical specs before coding begins.""",
    verbose=True,
    llm=llm,
    allow_delegation=False,
    max_iter=10
)

# 💻 Coder: Implements code
coder = Agent(
    role="Senior Python Developer", 
    goal="Write clean, bug-free, well-documented Python code exactly per specs",
    backstory="""8 years Python development. Master of CLI apps, Click/argparse, 
    data persistence, testing. Writes production-ready code on first try.""",
    verbose=True,
    llm=llm,
    allow_delegation=False,
    max_iter=15
)

# 🔍 Reviewer: Finds bugs + improves
reviewer = Agent(
    role="Code Review Specialist",
    goal="Find bugs, security issues, improve performance and quality",
    backstory="""10 years reviewing Python code at FAANG. Catches edge cases,
    performance bottlenecks, security flaws. Provides actionable fixes.""",
    verbose=True,
    llm=llm,
    allow_delegation=False,
    max_iter=10
)

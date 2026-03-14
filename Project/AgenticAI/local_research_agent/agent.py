from langchain_ollama import OllamaLLM
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from tools import TOOLS
from memory import retrieve_memory, add_to_memory

llm = OllamaLLM(model="mistral:7b", temperature=0.1)

REACT_PROMPT = """
Answer the human's question using these tools. Think step-by-step using this format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Relevant past research: {memory}

Begin!

Question: {input}
Thought:"""

prompt = PromptTemplate.from_template(REACT_PROMPT)

def create_agent(session_id="default"):
    memory_context = "\n".join(retrieve_memory("relevant research", session_id))
    
    agent = create_react_agent(llm, TOOLS, prompt.format(
        tool_names=", ".join([t.name for t in TOOLS]),
        memory=memory_context
    ))
    
    agent_executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True, max_iterations=5)
    return agent_executor

def research_topic(topic, session_id="default"):
    """Run research agent."""
    agent = create_agent(session_id)
    result = agent.invoke({"input": f"Research '{topic}' thoroughly. Find key facts, sources, statistics."})
    
    # Store to memory
    add_to_memory(f"Research on {topic}: {result['output']}", session_id)
    
    return result['output']

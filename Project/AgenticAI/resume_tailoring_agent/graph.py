from langgraph.graph import StateGraph, END
from state import ResumeState
from nodes import extract_skills_node, tailor_resume_node, generate_cover_letter_node, human_review_node
from typing import Dict, Any

def create_workflow():
    # Define workflow graph
    workflow = StateGraph(ResumeState)
    
    # Add nodes
    workflow.add_node("extract_skills", extract_skills_node)
    workflow.add_node("tailor_resume", tailor_resume_node)
    workflow.add_node("human_review", human_review_node)
    workflow.add_node("generate_cover", generate_cover_letter_node)
    
    # Edges
    workflow.set_entry_point("extract_skills")
    workflow.add_edge("extract_skills", "tailor_resume")
    workflow.add_conditional_edges(
        "tailor_resume",
        lambda state: "human_review" if state.get('needs_human_review', False) else "generate_cover"
    )
    workflow.add_conditional_edges(
        "human_review",
        lambda state: END if not state.get('needs_human_review', False) else "tailor_resume"
    )
    workflow.add_edge("generate_cover", END)
    
    return workflow.compile()

def run_workflow(app, state_manager, initial_state: ResumeState):
    """Execute with state persistence."""
    current_state = initial_state.copy()
    current_state['timestamp'] = initial_state.get('timestamp', 'now')
    
    # Check for existing state
    existing = state_manager.load_state(current_state['session_id'])
    if existing and existing['status'] != 'complete':
        print(f"📂 Resuming session: {current_state['session_id']}")
        current_state.update(existing)
    
    # Run graph
    result = app.invoke(current_state)
    
    # Persist final state
    state_manager.save_state(result)
    return result

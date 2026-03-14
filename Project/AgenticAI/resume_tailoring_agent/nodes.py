from langchain_ollama import OllamaLLM
from typing import Dict, Any
import re

llm = OllamaLLM(model="mistral:7b", temperature=0.1)

def extract_skills_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Extract required skills from job description."""
    prompt = f"""
    Analyze this job description and extract the TOP 10 REQUIRED skills/technologies:
    
    JOB: {state['job_description']}
    
    Output ONLY a JSON list like:
    ["Python", "FastAPI", "Docker", "AWS", "PostgreSQL", ...]
    """
    
    skills = llm.invoke(prompt).strip('[]').strip('""').split(',')
    skills = [s.strip().strip('"').strip("'") for s in skills if s.strip()]
    
    return {
        "extracted_skills": skills[:10],
        "status": "skills_extracted"
    }

def tailor_resume_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Rewrite resume to match job skills."""
    skills = ", ".join(state['extracted_skills'])
    
    prompt = f"""
    Rewrite this resume to emphasize these REQUIRED job skills: {skills}
    
    ORIGINAL RESUME:
    {state['original_resume']}
    
    TAILORED VERSION (keep structure, highlight matching skills):
    """
    
    tailored = llm.invoke(prompt)
    return {
        "tailored_resume": tailored,
        "status": "resume_tailored",
        "needs_human_review": True
    }

def generate_cover_letter_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Generate matching cover letter."""
    skills = ", ".join(state['extracted_skills'])
    
    prompt = f"""
    Write a 200-word cover letter for this job:
    
    JOB REQUIRES: {skills}
    RESUME HIGHLIGHTS: {state['tailored_resume'][:500]}...
    
    Make it concise, professional, keyword-optimized.
    """
    
    cover = llm.invoke(prompt)
    return {
        "cover_letter": cover,
        "status": "complete"
    }

def human_review_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Checkpoint for human approval."""
    print("\n🧑 HUMAN REVIEW NEEDED:")
    print("Tailored Resume Preview:")
    print(state['tailored_resume'][:1000] + "...")
    print("\nApprove? (y/n): ", end="")
    response = input()
    
    if response.lower() == 'y':
        return {"needs_human_review": False}
    else:
        return {"needs_human_review": True, "status": "needs_revision"}

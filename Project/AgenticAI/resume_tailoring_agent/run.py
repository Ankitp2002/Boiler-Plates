import os
from datetime import datetime
from state import StateManager, ResumeState
from graph import create_workflow

os.makedirs("outputs", exist_ok=True)

def save_outputs(state):
    """Save tailored resume + cover letter."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Resume
    with open(f"outputs/resume_{timestamp}.md", "w") as f:
        f.write(f"# Tailored Resume\n\n{state['tailored_resume']}")
    
    # Cover letter
    with open(f"outputs/cover_letter_{timestamp}.md", "w") as f:
        f.write(f"# Cover Letter\n\n{state['cover_letter']}")
    
    print(f"\n✅ Files saved:")
    print(f"   📄 outputs/resume_{timestamp}.md")
    print(f"   📄 outputs/cover_letter_{timestamp}.md")

if __name__ == "__main__":
    print("💼 Resume Tailoring Agent")
    print("=" * 50)
    
    # Input
    job_desc = input("📋 Paste job description: \n")
    resume = input("\n📄 Paste your resume: \n")
    
    # Initialize
    state_manager = StateManager()
    app = create_workflow()
    
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    initial_state: ResumeState = {
        "job_description": job_desc,
        "original_resume": resume,
        "session_id": session_id,
        "status": "starting",
        "needs_human_review": False
    }
    
    # Run
    result = run_workflow(app, state_manager, initial_state)
    
    # Save outputs
    save_outputs(result)
    
    print("\n🎉 Tailoring complete! Check outputs/ folder.")

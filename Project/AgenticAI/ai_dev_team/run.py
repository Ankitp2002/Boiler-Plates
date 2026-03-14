import os
import sys
from datetime import datetime
from crew import DevTeamCrew

os.makedirs("outputs", exist_ok=True)

if __name__ == "__main__":
    # Get task from CLI
    task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "build a to-do CLI app"
    
    print(f"🏢 AI DEV TEAM: {task}")
    print("=" * 60)
    
    # Run development cycle
    crew = DevTeamCrew(task)
    result = crew.run_project()
    
    # Save outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Extract final code from reviewer output
    if "todo_app.py" in result:
        with open(f"outputs/todo_app_{timestamp}.py", "w") as f:
            f.write(result)
    
    # Generate README
    readme = f"""# AI Dev Team Output: {task}"""

## 🏢 Team Collaboration Log

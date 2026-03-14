from crewai import Crew, Process
from tasks import create_tasks
from agents import architect, coder, reviewer

class DevTeamCrew:
    def __init__(self, task_description="build a to-do CLI app"):
        self.task_description = task_description
        self.tasks = create_tasks(task_description)
        self.crew = Crew(
            agents=[architect, coder, reviewer],
            tasks=self.tasks,
            process=Process.sequential,  # Architect → Coder → Reviewer
            verbose=2,
            memory=True,
            max_rpm=100,
            share_crew=True
        )
    
    def run_project(self, max_retries=2):
        """Run with error handling."""
        for attempt in range(max_retries + 1):
            try:
                print(f"\n🚀 DEVELOPMENT CYCLE #{attempt + 1}")
                result = self.crew.kickoff()
                return result
            except Exception as e:
                print(f"❌ Cycle {attempt + 1} failed: {e}")
                if attempt == max_retries:
                    raise
                print("🔄 Retrying...")

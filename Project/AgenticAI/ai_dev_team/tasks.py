from crewai import Task
from agents import architect, coder, reviewer

def create_tasks(task_description="build a to-do CLI app"):
    tasks = []
    
    # Task 1: Architecture design
    tasks.append(Task(
        description=f"""
        Design a complete CLI {task_description}.
        
        Provide:
        1. Feature list with user stories
        2. Technical architecture (files/modules)
        3. CLI commands with examples  
        4. Data model (JSON file format)
        5. Error handling strategy
        6. Edge cases to consider
        
        Output as detailed TECHNICAL SPECIFICATION.
        """,
        expected_output="Technical specification document for CLI app",
        agent=architect
    ))
    
    # Task 2: Code implementation  
    tasks.append(Task(
        description="""Using the Architect's specification above, write COMPLETE working Python code.
        
        Requirements:
        - Single file: todo_app.py
        - Use Click or argparse
        - Full error handling
        - Data persistence (JSON)
        - Exactly match spec'd features
        - Include docstrings + comments
        - Test with 3 example scenarios""",
        expected_output="Complete, working todo_app.py file",
        agent=coder,
        context=[tasks[0]]  # Gets architect output
    ))
    
    # Task 3: Code review + fixes
    tasks.append(Task(
        description="""Review the Coder's implementation above. 
        
        Check for:
        1. Bugs / crashes
        2. Edge cases not handled  
        3. Performance issues
        4. Security problems
        5. Code style violations
        6. Missing features from spec
        
        Provide FIXED CODE + detailed review report.""",
        expected_output="Final production-ready todo_app.py + review report",
        agent=reviewer,
        context=[tasks[0], tasks[1]]
    ))
    
    return tasks

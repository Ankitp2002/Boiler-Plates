from typing import TypedDict, Dict, Any, Optional
from datetime import datetime
import sqlite3
import json
import os

class ResumeState(TypedDict):
    job_description: str
    original_resume: str
    extracted_skills: list
    tailored_resume: str
    cover_letter: str
    status: str  # "extracting|tailoring|generating|complete"
    needs_human_review: bool
    session_id: str
    timestamp: str

class StateManager:
    def __init__(self, db_path="resume.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS workflows (
                session_id TEXT PRIMARY KEY,
                state JSON,
                timestamp TEXT
            )
        """)
        conn.commit()
        conn.close()
    
    def save_state(self, state: ResumeState):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT OR REPLACE INTO workflows VALUES (?, ?, ?)",
            (state['session_id'], json.dumps(state), state['timestamp'])
        )
        conn.commit()
        conn.close()
    
    def load_state(self, session_id: str) -> Optional[ResumeState]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT state FROM workflows WHERE session_id=?", (session_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {**json.loads(row[0]), 'session_id': session_id}
        return None

langgraph langchain-ollama ollama sqlite3

1. pip install -r requirements.txt
2. ollama pull mistral:7b
3. python run.py

Input job desc → your resume → magic happens

Job Desc → Extract Skills
↓
Tailor Resume ─→ Human Review? ─→ [Loop if No]
↓ (Yes)
Generate Cover Letter → ✅ Save Files

Paste job desc → Paste resume → Extract skills →
Tailor resume → [Human: y/n?] → Cover letter → ✅ Save files

Client
↓
FastAPI Endpoint
↓
Pydantic Validation
↓
Dependency Injection (Executors)
↓
Parallel Fake Inference
↓
WebSocket Progress Updates
↓
Final Prediction Response

ml-inference-orchestrator/
│
├── app/
│ ├── main.py # FastAPI + Uvicorn entry
│ ├── api/
│ │ ├── v1/
│ │ │ ├── inference.py # APIRouter
│ │ │ └── websocket.py
│ │
│ ├── schemas/
│ │ └── inference.py # Pydantic models
│ │
│ ├── services/
│ │ ├── executor.py # Parallel execution
│ │ └── inference.py # Fake ML logic
│ │
│ ├── core/
│ │ ├── config.py # Settings
│ │ └── dependencies.py # Dependency Injection
│ │
│ └── utils/
│ └── metrics.py
│
└── requirements.txt

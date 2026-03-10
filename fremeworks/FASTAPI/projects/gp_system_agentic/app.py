from __future__ import annotations

from fastapi import FastAPI
import uvicorn

from api.routes import router as api_router


app = FastAPI(title="GP System Agentic Framework")


@app.get("/")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "gp_system_agentic"}


app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True)

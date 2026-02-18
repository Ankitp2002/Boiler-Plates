from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI(title="ML Interface Orchestrator")
@app.get("/")
def health_check():
    return "Good Health!!"

routers = APIRouter(prefix="/ml", tags=["ML API"])

@routers.get("")
async def initiate_model():
    return "Initiate Successfully!!"

app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
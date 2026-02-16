from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI(title="Route Base API!!")

app_router = APIRouter(prefix="/demo", tags=["demo"])

@app_router.get('')
async def health_check():
    return "Good Health!!"

app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)  
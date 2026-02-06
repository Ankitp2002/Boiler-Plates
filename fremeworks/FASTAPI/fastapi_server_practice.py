from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Perellal Execution APP")

@app.get("/initiate_execution")
async def initiate_execution():
    return "Success"

if __name__ == "__main__":
    uvicorn.run("fastapi_server_practice:app", host="127.0.0.1", port=8000, reload=True)
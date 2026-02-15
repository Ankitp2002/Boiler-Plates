from fastapi import FastAPI
import asyncio
import uvicorn
import time
from concurrent.futures import InterpreterPoolExecutor
from utils import fifty_two_week

app = FastAPI(title="Perellal Execution APP")

@app.get("/initiate_execution")
async def initiate_execution():
    _start_time = time.time()

    running_loop = asyncio.get_running_loop()
    with InterpreterPoolExecutor(max_workers=8) as _pool:
        tasks = [running_loop.run_in_executor(_pool, fifty_two_week, i) for i in range(1, 1001)]
        await asyncio.gather(*tasks)
        
    return (time.time() - _start_time) / 60  

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
from fastapi import FastAPI
import asyncio
import uvicorn
import numpy as np
import time
from concurrent.futures import ProcessPoolExecutor
from utils import async_run_as_sync, twenty_four_week
from functools import partial

app = FastAPI(title="Perellal Execution APP")

@app.get("/initiate_execution")
async def initiate_execution():
    _start_time = time.time()

    chunks = [range(i, i+100) for i in range(1, 1001, 100)]
    running_loop = asyncio.get_running_loop()
    with ProcessPoolExecutor(max_workers=2) as _pool:
        [running_loop.run_in_executor(_pool, partial(async_run_as_sync, twenty_four_week, i)) for i in chunks]
            
    return time.time() - _start_time  

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
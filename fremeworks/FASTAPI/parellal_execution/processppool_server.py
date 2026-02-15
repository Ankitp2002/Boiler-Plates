from fastapi import FastAPI 
from concurrent.futures import ProcessPoolExecutor 
import asyncio
from functools import partial
import time

app = FastAPI(title="Process Pool Executor Demo!!")


def async_run_as_sync(fun, *args, **kwargs):
    return asyncio.run(fun(*args, **kwargs))

async def individual_calculation(simulation_no, week):
    for i in range(52):
        # await asyncio.sleep(1)
        ...
    print("Process done for simulation no: ", simulation_no, "week no: ", week)

async def initiate_weeks_calculation(simulation_no):

    
    task = (individual_calculation(simulation_no, i) for i in range(1, 25, 2))
    await asyncio.gather(*task)

    return f"Complete simulaiton no :{simulation_no}"     

async def initiate_thread_calculation(start_chunk:int, end_chunk:int):
    
    thread_running_loop = asyncio.get_running_loop()
    
    async with asyncio.Semaphore(25):
        results = (thread_running_loop.run_in_executor(None, partial(async_run_as_sync, initiate_weeks_calculation, sim)) for sim in range(start_chunk, end_chunk))
        
        return await asyncio.gather(*results)
    
@app.get("/initiate_process")
async def initiate_process_pool():
    __start = time.time()
    running_loop = asyncio.get_running_loop()
    with ProcessPoolExecutor(max_workers=2) as _process_pool:
        # for process pool must submit sycn function not async
        tasks = (running_loop.run_in_executor(_process_pool, partial(async_run_as_sync, initiate_thread_calculation, i, i+100)) for i in range(1, 1000, 100))
        await asyncio.gather(*tasks)
    
    return (time.time() - __start) / 60

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_server:app", host="127.0.0.1", port=8000, reload = True) 
    
    
    
    
    
    
    
    
    
    
# 1000 > splite > 100 > splite > 1 > splite > 24
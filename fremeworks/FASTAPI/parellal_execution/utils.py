"""
Execution Idea
> 1000 * 24 * 52
"""
from concurrent.futures import InterpreterPoolExecutor  
import asyncio
import time

def async_run_as_sync(funs, *args, **kwargs):
    return asyncio.run(funs(*args, **kwargs))

async def twenty_four_week(chunks):
    running_loop = asyncio.get_running_loop() 
    with InterpreterPoolExecutor(max_workers=10) as executor:
        tasks = [running_loop.run_in_executor(executor, fifty_two_week, i) for i in chunks]
        await asyncio.gather(*tasks)
        
def fifty_two_week(sim):
    
    for i in range(52):
        time.sleep(1)
    
    print("Done Simulation No.", sim)    
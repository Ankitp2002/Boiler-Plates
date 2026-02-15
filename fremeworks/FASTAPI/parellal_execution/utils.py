"""
Execution Idea
> 1000 * 24 * 52
"""
import numpy as np

def heavy_task():
    # arr = np.arange(1, 2000)
    # return arr
    ...
         
def fifty_two_week(sim) -> None:
    for safety_week in range(2, 25, 2):    
        for i in range(52):
            heavy_task()
        print("Done Simulation No.", sim, "Safety Week No.", safety_week)    
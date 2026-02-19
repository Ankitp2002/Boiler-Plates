from concurrent.futures import InterpreterPoolExecutor
import asyncio
from functools import partial

async def execut_parellel_with_interpreter_pool(__fun__, *args, **kwargs):
    """
    Execut Fun in a separate interpreter with leverage the new feature of python 3.14.
    """
    running_loop = asyncio.get_running_loop()
    with InterpreterPoolExecutor(max_workers=1) as interpreter_executor:
        running_loop.run_in_executor(interpreter_executor, partial(__fun__, *args, **kwargs))
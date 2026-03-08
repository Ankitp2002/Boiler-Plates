import asyncio
from functools import partial
from typing import Any, Callable

try:
    # Python 3.14+ (planned) – real interpreter-level isolation
    from concurrent.futures import InterpreterPoolExecutor as _BaseExecutor  # type: ignore[attr-defined]
except ImportError:
    # Fallback for current Python versions – process-level isolation
    from concurrent.futures import ProcessPoolExecutor as _BaseExecutor  # type: ignore[assignment]


async def execute_parallel_with_interpreter_pool(
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Execute a sync function in a separate interpreter / process.

    This gives you strong isolation for heavy ML logic while exposing a simple
    `await`-able API to the FastAPI layer.
    """
    loop = asyncio.get_running_loop()
    with _BaseExecutor(max_workers=1) as executor:
        return await loop.run_in_executor(executor, partial(func, *args, **kwargs))


# Backwards-compatible alias for the original, misspelled name
execut_parellel_with_interpreter_pool = execute_parallel_with_interpreter_pool

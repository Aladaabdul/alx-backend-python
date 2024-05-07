#!/usr/bin/env python3


"""measure_runtime function"""

import asyncio
import time
func = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return total runtime
    """
    start_time = time.perf_counter()
    results = await asyncio.gather(func(), func(), func(), func())
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return runtime

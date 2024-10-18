#!/usr/bin/env python3
"""
Module to measure the runtime of async_comprehension.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing async_comprehension
    four times in parallel.

    Returns:
        float: The total time taken to execute the four
               async_comprehension calls.
    """
    start_time = time.time()  # Record the start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    total_time = time.time() - start_time  # Calculate elapsed time
    return total_time

"""
Explanation of Runtime:
When you run the measure_runtime coroutine, it will execute
async_comprehension four times in parallel. Each call to
async_comprehension asynchronously waits for 10 seconds because
it collects 10 random numbers from the async_generator,
which itself waits 1 second for each of the 10 random numbers,
resulting in a total wait time of approximately 10 seconds for each call.

Since the calls are executed in parallel:

When you call asyncio.gather(...) with four calls to async_comprehension,
all four coroutines start executing at the same time.
They each independently wait for their 10 seconds without blocking one another.
As a result, the total elapsed time will be around 10 seconds regardless of
how many times you run async_comprehension, as they all wait concurrently.
"""

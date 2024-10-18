#!/usr/bin/env python3
"""
Asynchronous routines to handle random delays using tasks.
"""

import asyncio
from typing import List

# Importing the task_wait_random function from the previously defined module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n tasks to wait for random delays
    and return them in ascending order.

    Args:
        n (int): Number of delays to wait for.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: A list of the waited delays in ascending order.
    """
    # List to hold the tasks for concurrent execution
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gather results
    results = await asyncio.gather(*tasks)

    # Sort the results in ascending order before returning
    return sorted(results)

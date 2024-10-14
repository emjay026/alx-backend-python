#!/usr/bin/env python3
"""
Asynchronous routines to handle random delays.
"""

import asyncio
import random
from typing import List

# Importing wait_random from the previously defined module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n random delays and return them in ascending order.

    Args:
        n (int): Number of delays to wait for.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: A list of the waited delays in ascending order.
    """
    delays = []  # List to store the delays
    tasks = []   # List to hold the tasks for concurrent execution

    # Create n tasks for wait_random
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    # Gather results
    results = await asyncio.gather(*tasks)

    # Insert delays into the list in ascending order
    for delay in results:
        delays.append(delay)
        # Maintain ascending order by inserting at the correct position
        delays.sort()

    return delays

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
    # List to hold the tasks for concurrent execution
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather results
    results = await asyncio.gather(*tasks)

    # Sort the results in ascending order
    return sorted(results)

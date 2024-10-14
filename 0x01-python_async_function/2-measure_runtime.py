#!/usr/bin/env python3
"""
Module to measure the runtime of the wait_n function.
"""

import asyncio
import time
from typing import Callable

# Importing wait_n from the previous module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per call of wait_n (total_time / n).
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    total_time = time.time() - start_time  # Calculate elapsed time
    return total_time / n  # Return average time per call

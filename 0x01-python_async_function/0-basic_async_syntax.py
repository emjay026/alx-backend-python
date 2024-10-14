#!/usr/bin/env python3
"""
Asynchronous coroutine for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay waited.
    """
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Asynchronously wait for the generated delay
    await asyncio.sleep(delay)
    return delay

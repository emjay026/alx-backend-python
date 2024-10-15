#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers.

This coroutine waits asynchronously for 1 second in each of 10 iterations,
yielding a random number between 0 and 10.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields a random number between 0 and 10.

    Yields:
        int: A random number between 0 and 10 after waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)  # Yield a random number between 0 and 10

#!/usr/bin/env python3
"""
Coroutine that collects random float numbers asynchronously
using an asynchronous comprehension from async_generator.
"""

import asyncio
from typing import List  # Import List for type annotation
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers from async_generator using
    asynchronous comprehension.

    Returns:
        List[float]: A list containing 10 random float numbers.
    """
    # Use asynchronous comprehension to collect values from async_generator
    return [number async for number in async_generator()]

#!/usr/bin/env python3
"""
Module to create asyncio tasks for wait_random.
"""

import asyncio

# Importing wait_random from the previously defined module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task to run wait_random.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: The asyncio Task that will execute wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

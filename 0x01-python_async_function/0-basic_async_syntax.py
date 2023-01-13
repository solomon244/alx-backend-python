#!/usr/bin/env python3

"""
waits for a random number
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random number between 0 and max_dely
    """
    task: float = random.uniform(0, max_delay)
    await asyncio.sleep(task)
    return task

#!/usr/bin/env python3
"""
collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
"""
import asyncio
import random
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Creates a list of 10 numbers from a 10-number generator.
    """
    return [n async for n in async_generator()]

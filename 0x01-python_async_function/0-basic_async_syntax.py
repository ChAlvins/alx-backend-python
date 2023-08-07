#!/usr/bin/env python3
"""wait_random method"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return wait time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

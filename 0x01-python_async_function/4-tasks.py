#!/usr/bin/env python3
"""task_wait_n function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random  # Importing from the previous Python file


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_random n times"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return delays

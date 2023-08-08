#!/usr/bin/env python3
"""async_generator corouting function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generating a loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

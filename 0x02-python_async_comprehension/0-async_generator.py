#!/usr/bin/env python3
"""async_generator corouting function"""
import asyncio
import random


async def async_generator() -> None:
    """ generating a loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

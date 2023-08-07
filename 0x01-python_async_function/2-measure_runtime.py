#!/usr/bin/env python3
""" measuring run time function"""
import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Computes the average runtime of wait_n """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_operation = total_time / n
    return average_time_per_operation

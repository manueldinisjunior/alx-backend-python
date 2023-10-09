#!/usr/bin/env python3
"""Write an asynchronous coroutine to take in an integer argument named wait_random that waits
for a random delay.
Use the random module.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for some time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
  

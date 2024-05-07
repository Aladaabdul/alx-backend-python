#!/usr/bin/env python3


"""async_comprehension"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return list of random numbers
    """
    async_gen = [i async for i in async_generator()]
    return async_gen

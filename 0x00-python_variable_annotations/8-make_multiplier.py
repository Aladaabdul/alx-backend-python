#!/usr/bin/env python3


"""make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function multiplier

    """
    return lambda x: x * multiplier

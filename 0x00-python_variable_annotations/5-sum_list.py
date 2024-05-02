#!/usr/bin/env python3


"""sum_list module"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of a list

    """
    total = 0

    for i in range(len(input_list)):
        total += input_list[i]
    return total

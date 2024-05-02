#!/usr/bin/env python3


"""sum_list module"""


def sum_list(input_list: list[float]) -> float:
    """return sum of a list

    """
    total = 0

    for i in range(len(input_list)):
        total += input_list[i]
    return total

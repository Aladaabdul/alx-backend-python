#!/usr/bin/env python3


"""sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return sum of a list

    """
    total = 0

    for i in range(len(mxd_lst)):
        total += mxd_lst[i]

    return total

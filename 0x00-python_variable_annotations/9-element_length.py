#!/usr/bin/env python3


"""function defination"""


from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function body

    """
    return [(i, len(i)) for i in lst]

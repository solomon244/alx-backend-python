#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which takes a list mxd_lst
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of the element in the list"""
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum

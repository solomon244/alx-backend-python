#!/usr/bin/env python3
'''type-annotated function sum_list which takes a list input_list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))

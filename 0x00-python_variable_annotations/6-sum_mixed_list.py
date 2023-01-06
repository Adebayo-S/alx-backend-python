#!/usr/bin/env python3
""" omplex types - mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ akes a list mxd_lst of integers and floats
    and returns their sum as a float. """
    return sum(mxd_lst)

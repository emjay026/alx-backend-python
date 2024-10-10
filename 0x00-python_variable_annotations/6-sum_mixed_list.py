#!/usr/bin/env python3
"""
Module for summing a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing integers
    and floats to sum.

    Returns:
    float: The sum of all numbers in the mxd_lst as a float.
    """
    return float(sum(mxd_lst))

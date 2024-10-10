#!/usr/bin/env python3
"""
Module for summing a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Parameters:
    input_list (List[float]): A list of float numbers to sum.

    Returns:
    float: The sum of all floats in the input_list.
    """
    return sum(input_list)

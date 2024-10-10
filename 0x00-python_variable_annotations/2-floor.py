#!/usr/bin/env python3
"""
Module for calculating the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a given float.

    Parameters:
    n (float): The float number to calculate the floor of.

    Returns:
    int: The largest integer less than or equal to n.
    """
    return math.floor(n)

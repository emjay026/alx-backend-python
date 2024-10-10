#!/usr/bin/env python3
"""
Module for creating a tuple of a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is the string k and the second 
    element is the square of the number v.

    Parameters:
    k (str): The string element of the tuple.
    v (Union[int, float]): The integer or float to be squared.

    Returns:
    Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return (k, float(v ** 2))

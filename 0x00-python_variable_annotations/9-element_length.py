#!/usr/bin/env python3
"""
Module for calculating the length of elements in a list.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences (e.g., lists, strings).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    a sequence and its length.
    """
    return [(i, len(i)) for i in lst]

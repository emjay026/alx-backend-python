#!/usr/bin/env python3
"""
Module for zooming an array by a specified factor.
"""

from typing import Tuple, List, Union


def zoom_array(lst: Tuple[Union[int, float], ...], factor: int = 2)\
      -> List[Union[int, float]]:
    """
    Zoom in on the elements of the array by the specified factor.

    Parameters:
    lst (Tuple[Union[int, float], ...]): The tuple of elements to zoom.
    factor (int): The factor by which to zoom in. Default is 2.

    Returns:
    List[Union[int, float]]: A list containing the zoomed-in elements.
    """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Test array
array = (12, 72, 91)  # Changed to a tuple as per the annotation requirement

# Zoom 2x
zoom_2x = zoom_array(array)

# Zoom 3x
zoom_3x = zoom_array(array, 3)

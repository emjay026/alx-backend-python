#!/usr/bin/env python3
"""
Module for zooming an array by a specified factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on the elements of the array by the specified factor.

    Parameters:
    lst (Tuple): The tuple of elements to zoom.
    factor (int): The factor by which to zoom in. Default is 2.

    Returns:
    List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Example usage
array = (12, 72, 91)  # Example tuple input

# Zoom 2x
zoom_2x = zoom_array(array)

# Zoom 3x
zoom_3x = zoom_array(array, 3)

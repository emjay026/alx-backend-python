#!/usr/bin/env python3
"""
Module for safely retrieving the first element of a sequence.
"""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely return the first element of a sequence.

    Parameters:
    lst (Sequence[Any]): A sequence (e.g., list, tuple) from which to
                         retrieve the first element.

    Returns:
    Optional[Any]: The first element of the sequence, or None if the
                   sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

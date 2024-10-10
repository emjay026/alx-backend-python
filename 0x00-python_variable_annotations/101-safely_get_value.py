#!/usr/bin/env python3
"""
Module for safely retrieving values from a dictionary.
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')  # This will be used for the return type


def safely_get_value(dct: Mapping[Any, T],
                     key: Any, default: Optional[T] = None)\
      -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Parameters:
    dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
    key (Any): The key to look for in the dictionary.
    default (Optional[T]): The value to return if the key is not found.
    Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key if found,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""Unit tests for the access_nested_map function in the utils module.

This module contains tests to verify that the access_nested_map function
correctly returns values from nested dictionaries based on provided paths.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected results.

        Parameters
        ----------
        nested_map: Mapping
            A nested map to test.
        path: Sequence
            A path in the nested map.
        expected: Any
            The expected return value from the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()

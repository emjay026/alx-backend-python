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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths.

        Parameters
        ----------
        nested_map: Mapping
            A nested map to test.
        path: Sequence
            A path that does not exist in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check the exception message matches the expected key
        self.assertEqual(str(context.exception), repr(path[-1]))


if __name__ == "__main__":
    unittest.main()

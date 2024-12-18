#!/usr/bin/env python3
"""Unit tests for the access_nested_map function in the utils module.

This module contains tests to verify that the access_nested_map function
correctly returns values from nested dictionaries based on provided paths.

Unit tests for the get_json function in the utils module.

This module contains tests to verify that the get_json function
correctly retrieves JSON data from a specified URL without making
actual HTTP requests.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json
from utils import memoize


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


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')  # Patch requests.get
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected JSON payload.

        Parameters
        ----------
        test_url: str
            The URL to test with.
        test_payload: dict
            The expected JSON payload to return.
        """
        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response  # Mock the return value

        # Call the get_json function
        result = get_json(test_url)

        # Verify the mocked requests.get was called with test_url
        mock_get.assert_called_once_with(test_url)

        # Test that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize works correctly with properties."""

        class TestClass:
            """A test class to demonstrate memoization."""

            def a_method(self):
                """Original method to be mocked."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property that calls a_method."""
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch a_method to mock its behavior
        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:

            # Call the memoized property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Assert that results are equal
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)

            # Assert that a_method is called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()

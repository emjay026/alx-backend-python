#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class in the client module.

This module contains tests to verify that the GithubOrgClient class
correctly retrieves organization data without making external HTTP requests.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Patch the get_json function
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value.

        Parameters
        ----------
        org_name: str
            The name of the organization to test.
        """
        # Define the expected return value for the mock
        mock_get_json.return_value = \
            {"repos_url": f'https://api.github.com/orgs/{org_name}/repos'}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

        # Assert that the result matches the expected format
        self.assertEqual(result, mock_get_json.return_value)

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property.

        This tests that the private property _public_repos_url returns the
        correct URL from the org property.
        """
        # Define a known payload for the org property
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Assert that the _public_repos_url property returns the expected value
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method.

        This tests that the public_repos method returns the correct
        list of repository names based on the mocked payload.
        """
        # Mock payload that get_json would return
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Patch the _public_repos_url property
        with patch.object(
            client,
            '_public_repos_url',
            return_value="https://api.github.com/orgs/google/repos"
        ):

            # Call the public_repos method with no license filter
            repos = client.public_repos()

            # Assert that the returned list matches expected repository names
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Assert that the mocked get_json was called once
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class in the client module.

This module contains tests to verify that the GithubOrgClient class
correctly retrieves organization data without making external HTTP requests.

Integration tests for the GithubOrgClient class in the client module.

This module tests the public_repos method by mocking only external requests
made by the requests module while using real data structures from fixtures.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

        # Patch the _public_repos_url property with a specific URL
        with patch.object(
            client,
            '_public_repos_url',
            return_value="https://api.github.com/orgs/google/repos"
        ):
            # Call the public_repos method with no license filter
            repos = client.public_repos()

            # Assert that the returned list matches expected repository names
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Assert that the mocked get_json was called once with correct URL
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method.

        Parameters
        ----------
        repo: Dict
            Repository dictionary containing license information.
        license_key: str
            The license key to check.
        expected: bool
            The expected return value of the has_license method.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(org_payload, repos_payload, expected_repos, apache2_repos)]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test case by patching requests.get."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mock the return values for the various URLs
        cls.mock_get.side_effect = lambda url: (
            cls.org_payload if 'orgs' in url else
            cls.repos_payload if 'repos' in url else
            {}
        )

    @classmethod
    def tearDownClass(cls):
        """Tear down the test case by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method for the expected outputs."""
        client = GithubOrgClient('google')

        # Call the public_repos method and check the results
        repos = client.public_repos()

        # Assert that the results match what we expect
        self.assertEqual(repos, self.expected_repos)


if __name__ == "__main__":
    unittest.main()

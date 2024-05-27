#!/usr/bin/env python3


"""GithubOrgClient class"""


import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class

    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    def test_org(self, org_name, expected):
        """test_org function

        """
        config = {"return_value.json.return_value": expected}
        patcher = patch("requests.get", **config)
        mock = patcher.start()
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, expected)
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        patcher.stop()

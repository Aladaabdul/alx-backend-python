#!/usr/bin/env python3


"""GithubOrgClient class"""


import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from typing import Dict, Any


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class

    """
    @parameterized.expand([
        ("google", "OK"),
        ("abc", "OK")
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

    def test_public_repos_url(self):
        """test_public_repos_url function

        """
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock
                ) as mock__public_repos_url:
            url = mock__public_repos_url.return_value
            result = GithubOrgClient._public_repos_url
            self.assertEqual(result, url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, licence_key, expected):
        """test_has_licence function

        """
        result = GithubOrgClient.has_license(repo, licence_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""
        # def my_side_effect(url):
        #     """ Side Effect function for test """
        #     test_url = "https://api.github.com/orgs/google"
        #     if url == test_url:
        #         return cls.org_payload
        #     return cls.repos_payload

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()

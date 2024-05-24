#!/usr/bin/env python3


"""TestAccessNestedMap Module"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class

    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any
            ):
        """test_access_nested_map function

        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), {}),
        ({"a": 1}, ("a", "b"), 1)
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any
            ):
        """test_access_nested_map_exception function

        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson Class

    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(
            self,
            url,
            test_payload
            ):
        """test_get_json function

        """
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        result = get_json(url)
        self.assertEqual(result, test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """TestMemoize Class

    """
    def test_memoize(self):
        """test_memoize function

        """
        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()

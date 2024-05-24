#!/usr/bin/env python3


"""TestAccessNestedMap Module"""


from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class
from typing import Mapping, Sequence, Any



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

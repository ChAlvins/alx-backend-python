#!/usr/bin/env python3
"""unit test for  utils.access_nested_map"""

import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """testing access_nested_map` function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_result: Union[Dict, int],
            ) -> None:
        """Testing access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception_msg: Exception,
            ) -> None:
        """Testing for exceptions"""
        with self.assertRaises(exception_msg):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class implementing the TestGetJson.test_get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self: Any, test_uri: str, test_payload: Dict) -> None:
        """testing test_get_json"""
        attributes = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attributes)) as req_get:
            self.assertEqual(get_json(test_uri), test_payload)
            req_get.assert_called_once_with(test_uri)


if __name__ == "__main__":
    unittest.main()

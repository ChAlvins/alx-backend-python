#!/usr/bin/env python3
"""unit test for  utils.access_nested_map"""

import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map


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

if __name__ == "__main__":
    unittest.main()

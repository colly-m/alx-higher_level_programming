#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunc(unittest.TestCase):
    """Defines unittests for max_integer([..])"""
    def test_empty_list(self):
        """Tests an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        """Tests a list with single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Tests a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Tests a list of negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9, -1, -3]), -1)

    def test_mixed_numbers(self):
        """Tests a list of positive and negative numbers"""
        self.assertEqual(max_integer([7, -2, 0, 12, -5]), 12)

    def test_duplicate_max(self):
        """Tests a list of similar elements"""
        self.assertEqual(max_integer([8, 8, 8, 8, 8]), 8)

if __name__ == '__main__':
    unittest.main()

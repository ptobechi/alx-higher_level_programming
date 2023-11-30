#!/usr/bin/python3

"""
a python script with unittest
"""


import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    TextMaxInteger class
    """
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 0, -3]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.8]), 2.7)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "orange", "banana"]), "orange")

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()

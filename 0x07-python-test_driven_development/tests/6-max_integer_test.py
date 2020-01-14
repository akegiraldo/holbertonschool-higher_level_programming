#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for the unitest"""

    def test_max_integer(self):
        """Test for lenght == 0"""
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1e400, 0, 5, 6]), 1e400)
        self.assertAlmostEqual(max_integer([-1, -200, -10, -1000]), -1)

    def test_max_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, "Holberton", 0])

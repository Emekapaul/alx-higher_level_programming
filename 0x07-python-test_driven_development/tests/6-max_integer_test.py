#!/usr/bin/python3
"""unittest for function max_integer(list=[]) in modul 6-max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""

    def test_dataType(self):
        """It tests the data type"""
        res = max_integer([1, 2, 3, 4])
        self.assertIsInstance(res, (int, float))

    def test_MaxIntIsEmpty(self):
        """Test if max_int returns false"""
        res = max_integer()
        self.assertIsNone(res)
        self.assertEqual(max_integer([]), None)

    def test_ProperOutout(self):
        """Test if max_int is working properly"""
        # list integers
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([3, 2, 1, 4]), 4)
        self.assertNotEqual(max_integer([3, 2, 1, 4]), 7)
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

        # lists with loops
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

        # list floats
        self.assertEqual(max_integer([1, 4.8, 3.33, 2.0]), 4.8)
        self.assertNotEqual(max_integer([1, 4.8, 3.33, 2.0]), 4.2)

        # tuple integers
        self.assertEqual(max_integer((3, 4, 3, 2)), 4)
        self.assertNotEqual(max_integer((3, 4, 3, 2)), 2)

        # tuple floats
        self.assertEqual(max_integer((1, 4.8, 3.33, 2.0)), 4.8)
        self.assertNotEqual(max_integer((1, 4.8, 3.33, 2.0)), 4.2)

        # negative integers
        self.assertEqual(max_integer([-10, -2, -3, -44]), -2)
        self.assertNotEqual(max_integer([-10, -2, -3, -44]), -3)
        self.assertEqual(max_integer([10, -2, 3, 44]), 44)

    def test_BadValues(self):
        """It tests for bas values"""
        self.assertRaises(TypeError, max_integer, 6)
        self.assertRaises(TypeError, max_integer, ["e", "y", 5])
        self.assertRaises(TypeError, max_integer, {10.6, 2.5, 3.7, 44.4})
        self.assertRaises(TypeError, max_integer, {10, 2, 3, 44})

        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

        with self.assertRaises(TypeError):
            max_integer(1)

    def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

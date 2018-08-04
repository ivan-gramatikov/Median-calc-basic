# -*- coding: utf-8 -*-
#
"""
# Unit Test script
This is a standalone script which tests the Median calculator
"""

import unittest
import median


class MedianTest(unittest.TestCase):

    def test_median(self):
        # Working cases:
        # With floating point and negative numbers:
        self.assertEqual(median.input_and_calculate('-1.33', '2', '3', '4', '5', '6', '7', '8', '9', '10'), 5.5)
        # Integers only:
        self.assertEqual(median.input_and_calculate('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), 5.5)

        # Catching fails:
        # With invalid arguments, with no arguments
        self.assertRaises(ValueError, median.input_and_calculate, 'invalid', '1', '2')
        self.assertRaises(ValueError, median.input_and_calculate, '')


if __name__ == '__main__':
    unittest.main()
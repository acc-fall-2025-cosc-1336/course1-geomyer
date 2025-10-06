##Test case for homework c_decisions.py
import unittest

from src.homework.d_repetition import get_factorial, sum_odd_numbers

class TestDecisions(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEqual(get_factorial(0), 1)
        self.assertEqual(get_factorial(1), 1)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(10), 3628800)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(1), 1)
        self.assertEqual(sum_odd_numbers(2), 1)
        self.assertEqual(sum_odd_numbers(5), 9)
        self.assertEqual(sum_odd_numbers(10), 25)
 
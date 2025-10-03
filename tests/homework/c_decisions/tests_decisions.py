#Test case for homework c_decisions.py
import unittest

from src.homework.c_decisions.decisions import get_letter_grade, number_to_letter_grade

class TestDecisions(unittest.TestCase):

    def test_number_to_letter_grade(self):
        self.assertEqual(number_to_letter_grade(95), 'A')
        self.assertEqual(number_to_letter_grade(85), 'B')
        self.assertEqual(number_to_letter_grade(75), 'C')
        self.assertEqual(number_to_letter_grade(65), 'D')
        self.assertEqual(number_to_letter_grade(55), 'F')
        self.assertEqual(number_to_letter_grade(0), 'F')
        self.assertEqual(number_to_letter_grade(100), 'A')

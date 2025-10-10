import unittest

from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax


class test_functions(unittest.TestCase):
    def test_get_gross_pay(self):
        self.assertEqual(get_gross_pay(30, 20), 600)
        self.assertEqual(get_gross_pay(45, 20), 950)
        self.assertEqual(get_gross_pay(40, 15), 600)
    
    def test_get_fica_tax(self):
        self.assertEqual(get_fica_tax(1000), 230)
        self.assertEqual(get_fica_tax(500), 115)
        self.assertEqual(get_fica_tax(0), 0)
        self.assertEqual(get_fica_tax(2000), 460)

    def test_get_federal_tax(self):
        self.assertEqual(get_federal_tax(1000), 150)
        self.assertEqual(get_federal_tax(500), 75)
        self.assertEqual(get_federal_tax(0), 0)
        self.assertEqual(get_federal_tax(2000), 300)

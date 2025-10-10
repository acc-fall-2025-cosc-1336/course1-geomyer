import unittest
'''
the file in src/tests/homework/e_functions/tests_functions.py
has the test functions
'''
from tests.homework.e_functions import tests_functions   

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)

unittest.TextTestRunner().run(suite)

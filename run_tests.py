import unittest
'''
the file in tests/homework/c_decisions/tests_decisions.py 
has the test functions
'''
from tests.homework.d_repetition import tests_repetition  

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

unittest.TextTestRunner().run(suite)

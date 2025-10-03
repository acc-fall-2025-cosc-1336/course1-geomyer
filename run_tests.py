import unittest
'''
the file in tests/homework/c_decisions/tests_decisions.py 
has the test functions
'''
from tests.homework.c_decisions import tests_decisions as main

suite = unittest.TestLoader().loadTestsFromModule(main)
unittest.TextTestRunner(verbosity=2).run(suite)
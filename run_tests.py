import unittest

from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)


unittest.TextTestRunner().run(suite)






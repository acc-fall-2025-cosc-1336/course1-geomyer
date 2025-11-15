
import unittest

from src.homework.g_lists_and_tuples.lists import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):
        
    def test_get_p_distance(self):
        # Test that get_p_distance with parameter values returns the correct p-distance
        # between ['T','T','T','C','C','A','T','T','T','A'] and
        # ['G','A','T','T','C','A','T','T','T','C'] == 0.4
        list1 = [1, 2]
        list2 = [4, 6]
        self.assertAlmostEqual(get_p_distance(list1, list2), 1.0)

        list3 = [0, 0, 0]
        list4 = [0, 0, 0]
        self.assertEqual(get_p_distance(list3, list4), 0.0)

        with self.assertRaises(ValueError):
            get_p_distance([1, 2], [1, 2, 3])

    def test_get_p_distance_matrix(self):
        # Test that get_p_distance_matrix returns the correct matrix for given lists
        lists_to_compare = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected_matrix = [
            [0.0, 0.4, 0.1, 0.3],
            [0.4, 0.0, 0.5, 0.2],
            [0.1, 0.5, 0.0, 0.4],
            [0.3, 0.2, 0.4, 0.0]
        ]


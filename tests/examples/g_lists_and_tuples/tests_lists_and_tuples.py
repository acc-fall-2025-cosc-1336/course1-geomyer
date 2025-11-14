import unittest

from src.homework.g_lists_and_tuples.lists import get_p_distance, get_p_distance_matrix

class test_config(unittest.TestCase):
    def test_identical_lists(self):
        list1 = ['A', 'C', 'G', 'T']
        list2 = ['A', 'C', 'G', 'T']
        p = 2
        self.assertEqual(get_p_distance(list1, list2, p), 0.0)

    def test_completely_different_lists(self):
        list1 = ['A', 'A', 'A', 'A']
        list2 = ['T', 'T', 'T', 'T']
        p = 2
        self.assertEqual(get_p_distance(list1, list2, p), 1.0)

    def test_partial_difference(self):
        list1 = ['A', 'C', 'G', 'T']
        list2 = ['A', 'G', 'G', 'T']
        p = 2
        self.assertAlmostEqual(get_p_distance(list1, list2, p), (1/4)**0.5)

    def test_different_lengths(self):
        list1 = ['A', 'C', 'G']
        list2 = ['A', 'C', 'G', 'T']
        p = 2
        with self.assertRaises(ValueError):
            get_p_distance(list1, list2, p)

    def test_identical_matrices(self):
        matrix1 = [['A', 'C'], ['G', 'T']]
        matrix2 = [['A', 'C'], ['G', 'T']]
        p = 2
        self.assertEqual(get_p_distance_matrix(matrix1, matrix2, p), 0.0)
        

if __name__ == '__main__':
    unittest.main()



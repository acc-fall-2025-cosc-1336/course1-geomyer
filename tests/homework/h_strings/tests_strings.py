import unittest

# Tests for strings homework go here.
from src.homework.h_strings.strings import hamming_distance, get_dna_complement
class TestHammingDistance(unittest.TestCase):
    def test_equal_length_strings(self):
        self.assertEqual(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)

    def test_get_dna_complement(self):
        self.assertEqual(get_dna_complement("AAAACCCGGT"), "TTTTGGGCCA")
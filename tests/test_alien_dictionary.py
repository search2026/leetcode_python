import unittest
from solutions.alien_dictionary import Solution


class TestAlienDictionary(unittest.TestCase):
    def test_alien_dictionary(self):
        solution = Solution()
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertEqual("wertf", solution.alienOrder(words))

        words = ["z", "x"]
        self.assertEqual("zx", solution.alienOrder(words))

        words = ["z", "x", "z"]
        self.assertEqual("", solution.alienOrder(words))

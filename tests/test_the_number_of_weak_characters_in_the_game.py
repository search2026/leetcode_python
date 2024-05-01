import unittest
from solutions.the_number_of_weak_characters_in_the_game import Solution


class TestTheNumberOfWeakCharactersInTheGame(unittest.TestCase):
    def test_the_number_of_weak_characters_in_the_game(self):
        solution = Solution()
        properties = [[5, 5], [6, 3], [3, 6]]
        expected = 0
        self.assertEqual(solution.numberOfWeakCharacters(properties), expected)

        properties = [[2, 2], [3, 3]]
        expected = 1
        self.assertEqual(solution.numberOfWeakCharacters(properties), expected)

        properties = [[1, 5], [10, 4], [4, 3]]
        expected = 1
        self.assertEqual(solution.numberOfWeakCharacters(properties), expected)

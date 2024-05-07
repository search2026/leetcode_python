import unittest
from solutions.game_of_life import Solution


class TestGameOfLife(unittest.TestCase):
    def test_game_of_life(self):
        solution = Solution()
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expect = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        solution.game_of_life(board)
        self.assertEqual(expect, board)

        board = [[1, 1], [1, 0]]
        expect = [[1, 1], [1, 1]]
        solution.game_of_life(board)
        self.assertEqual(expect, board)

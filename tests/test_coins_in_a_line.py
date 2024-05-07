import unittest
from solutions.coins_in_a_line import Solution


class TestCoinsInALine(unittest.TestCase):
    def test_coins_in_a_line(self):
        solution = Solution()
        self.assertEqual(solution.is_first_player_win(5), True)
        self.assertEqual(solution.is_first_player_win(6), False)
        self.assertEqual(solution.is_first_player_win(7), True)
        self.assertEqual(solution.is_first_player_win(8), True)
        self.assertEqual(solution.is_first_player_win(9), False)
        self.assertEqual(solution.is_first_player_win(10), True)

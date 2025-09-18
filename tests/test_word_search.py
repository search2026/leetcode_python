import unittest
from solutions.word_search import Solution


class TestWordSearch(unittest.TestCase):
    def test_exist(self):
        solution = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(solution.exist(board, word))

        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        self.assertTrue(solution.exist(board, word))

        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        self.assertFalse(solution.exist(board, word))

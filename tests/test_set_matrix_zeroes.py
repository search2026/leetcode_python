import unittest
from solutions.blank import Solution


class TestSetMatrixZeroes(unittest.TestCase):
    def test_set_zeroes(self):
        solution = Solution()
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expect = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        solution.setZeroes(matrix)
        self.assertEqual(expect, matrix)

        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expect = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        solution.setZeroes(matrix)
        self.assertEqual(expect, matrix)

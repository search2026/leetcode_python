import unittest
from solutions.spiral_matrix import Solution


class TestSpiralMatrix(unittest.TestCase):
    def test_spiral_matrix(self):
        solution = Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(solution.spiralOrder(matrix), expected)

        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(solution.spiralOrder(matrix), expected)

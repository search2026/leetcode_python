import unittest
from solutions.rotate_image import Solution


class TestReverseWords(unittest.TestCase):
    def test_rotate(self):
        solution = Solution()
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expect = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        actual = solution.rotate(matrix)
        self.assertEqual(actual, expect)


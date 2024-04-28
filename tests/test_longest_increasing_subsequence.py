import unittest
from solutions.longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        solution = Solution()
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expect = 4
        actual = solution.length_of_lis(nums)
        self.assertEqual(expect, actual)

        nums = [0, 1, 0, 3, 2, 3]
        expect = 4
        actual = solution.length_of_lis(nums)
        self.assertEqual(expect, actual)

        nums = [7, 7, 7, 7, 7, 7, ]
        expect = 1
        actual = solution.length_of_lis(nums)
        self.assertEqual(expect, actual)

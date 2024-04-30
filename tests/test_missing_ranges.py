import unittest
from solutions.missing_ranges import Solution


class TestMissingRanges(unittest.TestCase):
    def test_missing_ranges(self):
        solution = Solution()
        nums = [0, 1, 3, 50, 75]
        lower = 0
        upper = 99
        expect = [[2, 2], [4, 49], [51, 74], [76, 99]]
        actual = solution.find_missing_ranges(nums, lower, upper)
        self.assertCountEqual(expect, actual)

        nums = [-1]
        lower = -1
        upper = -1
        expect = []
        actual = solution.find_missing_ranges(nums, lower, upper)
        self.assertCountEqual(expect, actual)

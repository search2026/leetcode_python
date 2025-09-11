import unittest
from solutions.three_sum import Solution


class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        solution = Solution()
        nums = [-1, 0, 1, 2, -1, -4]
        expect = [[-1, -1, 2], [-1, 0, 1]]
        actual = solution.threeSum(nums)
        assert actual == expect

        nums = [0, 1, 1]
        expect = []
        actual = solution.threeSum(nums)
        assert actual == expect

        nums = [0, 0, 0]
        expect = [[0, 0, 0]]
        actual = solution.two_sum(nums)
        assert actual == expect



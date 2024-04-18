import unittest
from solutions.two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expect = [0, 1]
        actual = solution.two_sum(nums, target)
        assert actual == expect

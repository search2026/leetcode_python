import unittest
from solutions.maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    def test_maximum_subarray(self):
        solution = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(solution.max_sub_array(nums), 6)

        nums = [1]
        self.assertEqual(solution.max_sub_array(nums), 1)

        nums = [5, 4, -1, 7, 8]
        self.assertEqual(solution.max_sub_array(nums), 23)

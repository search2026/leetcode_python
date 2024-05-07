import unittest
from solutions.maximum_product_subarray import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def test_maximum_product_subarray(self):
        solution = Solution()
        nums = [2, 3, -2, 4]
        self.assertEqual(solution.max_product(nums), 6)

        nums = [-2, 0, -1]
        self.assertEqual(solution.max_product(nums), 0)

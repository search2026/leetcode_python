import unittest
from solutions.maximum_product_of_three_numbers import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def test_maximum_product_subarray(self):
        solution = Solution()
        nums = [1,2,3]
        self.assertEqual(solution.maximumProduct(nums), 6)

        nums = [1,2,3,4]
        self.assertEqual(solution.maximumProduct(nums), 24)

        nums = [-1,-2,-3]
        self.assertEqual(solution.maximumProduct(nums), -6)

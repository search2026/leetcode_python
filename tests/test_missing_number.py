import unittest
from solutions.missing_number import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def test_maximum_product_subarray(self):
        solution = Solution()
        nums = [3,0,1]
        self.assertEqual(solution.missingNumber(nums), 2)

        nums = [0,1]
        self.assertEqual(solution.missingNumber(nums), 2)

        nums = [9,6,4,2,3,5,7,0,1]
        self.assertEqual(solution.missingNumber(nums), 8)

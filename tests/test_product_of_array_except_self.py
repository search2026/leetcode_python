import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def test_product_except_self(self):
        solution = Solution()
        nums = [1, 2, 3, 4]
        expect = [24, 12, 8, 6]
        actual = solution.productExceptSelf(nums)
        self.assertEqual(expect, actual)

        nums = [-1, 1, 0, -3, 3]
        expect = [0, 0, 9, 0, 0]
        actual = solution.productExceptSelf(nums)
        self.assertEqual(expect, actual)

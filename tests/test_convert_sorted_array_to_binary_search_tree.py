import unittest
from solutions.convert_sorted_array_to_binary_search_tree import Solution
from utils.TreeNode import serialize, deserialize


class TestConvertSortedArrayToBinarySearchTree(unittest.TestCase):
    def test_convert_sorted_array_to_binary_search_tree(self):
        solution = Solution()
        nums = [-10, -3, 0, 5, 9]
        expect = ['0', '-3', '9', '-10', None, '5', None, None, None, None, None]
        actual = solution.sortedArrayToBST(nums)
        self.assertEqual(expect, serialize(actual))

        nums = [1, 3]
        expect = ['3', '1', None, None, None]
        actual = solution.sortedArrayToBST(nums)
        self.assertEqual(expect, serialize(actual))

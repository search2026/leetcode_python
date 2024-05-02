import unittest
from solutions.convert_sorted_list_to_binary_search_tree import Solution
from utils.ListNode import ListNode
from utils.TreeNode import serialize


class TestConvertSortedListToBinarySearchTree(unittest.TestCase):
    def test_convert_sorted_list_to_binary_search_tree(self):
        solution = Solution()
        nums = [-10, -3, 0, 5, 9]
        expect = ['0', '-3', '9', '-10', None, '5', None, None, None, None, None]
        actual = solution.sortedListToBST(ListNode.arrayToListNode(nums))
        self.assertEqual(expect, serialize(actual))

        nums = []
        expect = [None]
        actual = solution.sortedListToBST(ListNode.arrayToListNode(nums))
        self.assertEqual(expect, serialize(actual))

import unittest
from solutions.merge_k_sorted_lists import Solution
from utils.ListNode import ListNode


class TestMergeKSortedLists(unittest.TestCase):
    def test_merge_k_sorted_lists(self):
        solution = Solution()
        lists = [ListNode.arrayToListNode([1, 4, 5]), ListNode.arrayToListNode([1, 3, 4]),
                 ListNode.arrayToListNode([2, 6])]
        expect = ListNode.arrayToListNode([1, 1, 2, 3, 4, 4, 5, 6])
        actual = solution.merge_k_lists(lists)
        self.assertEqual(expect, actual)

        lists = []
        expect = None
        actual = solution.merge_k_lists(lists)
        self.assertEqual(expect, actual)

        lists = [[]]
        expect = None
        actual = solution.merge_k_lists(lists)
        self.assertEqual(expect, actual)

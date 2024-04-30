import unittest
from solutions.merge_two_sorted_lists import Solution
from utils.ListNode import ListNode


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        solution = Solution()
        l1 = ListNode.arrayToListNode([1, 2, 4])
        l2 = ListNode.arrayToListNode([1, 3, 4])
        expect = ListNode.arrayToListNode([1, 1, 2, 3, 4, 4])
        actual = solution.merge_two_lists(l1, l2)
        while expect and actual:
            self.assertEqual(expect.val, actual.val)
            expect = expect.next
            actual = actual.next

        l1 = None
        l2 = None
        expect = None
        actual = solution.merge_two_lists(l1, l2)
        self.assertEqual(actual, expect)

        l1 = None
        l2 = ListNode(0)
        expect = ListNode(0)
        actual = solution.merge_two_lists(l1, l2)

        while expect and actual:
            self.assertEqual(expect.val, actual.val)
            expect = expect.next
            actual = actual.next

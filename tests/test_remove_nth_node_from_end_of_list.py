import unittest
from solutions.remove_nth_node_from_end_of_list import Solution
from utils.ListNode import ListNode


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        solution = Solution()
        l = ListNode.arrayToListNode([1, 2, 3, 4, 5])
        n = 2
        expect = ListNode.arrayToListNode([1, 2, 3, 5])
        actual = solution.removeNthFromEnd(l, n)
        self.assertEqual(
            ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect)
        )

        l = ListNode.arrayToListNode([1])
        n = 1
        expect = ListNode.arrayToListNode([])
        actual = solution.removeNthFromEnd(l, n)
        self.assertEqual(
            ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect)
        )

        l = ListNode.arrayToListNode([1,2])
        n = 1
        expect = ListNode.arrayToListNode([1])
        actual = solution.removeNthFromEnd(l, n)
        self.assertEqual(
            ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect)
        )

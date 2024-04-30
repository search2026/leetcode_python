import unittest
from solutions.add_two_numbers import Solution
from utils.ListNode import ListNode


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        solution = Solution()
        l1 = ListNode.arrayToListNode([2, 4, 3])
        l2 = ListNode.arrayToListNode([5, 6, 4])
        expect = ListNode.arrayToListNode([7, 0, 8])
        actual = solution.add_two_numbers(l1, l2)
        self.assertEqual(ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect))

        l1 = ListNode.arrayToListNode([0])
        l2 = ListNode.arrayToListNode([0])
        expect = ListNode.arrayToListNode([0])
        actual = solution.add_two_numbers(l1, l2)
        self.assertEqual(ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect))

        l1 = ListNode.arrayToListNode([9, 9, 9, 9, 9, 9, 9])
        l2 = ListNode.arrayToListNode([9, 9, 9, 9])
        expect = ListNode.arrayToListNode([8, 9, 9, 9, 0, 0, 0, 1])
        actual = solution.add_two_numbers(l1, l2)
        self.assertEqual(ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect))

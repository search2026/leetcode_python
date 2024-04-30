import unittest
from solutions.swap_nodes_in_pairs import Solution
from utils.ListNode import ListNode


class TestSwapNodesInPairs(unittest.TestCase):
    def test_swap_nodes_in_pairs(self):
        solution = Solution()
        head = ListNode.arrayToListNode([1, 2, 3, 4])
        expect = ListNode.arrayToListNode([2, 1, 4, 3])
        actual = solution.swap_pairs(head)
        self.assertEqual(ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect))

        head = None
        expect = None
        actual = solution.swap_pairs(head)
        self.assertEqual(ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect))

        head = ListNode.arrayToListNode([1])
        expect = ListNode.arrayToListNode([1])
        actual = solution.swap_pairs(head)
        self.assertEqual(ListNode.listNodeToArray(actual), ListNode.listNodeToArray(expect))

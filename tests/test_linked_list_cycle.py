import unittest
from solutions.linked_list_cycle import Solution
from utils.ListNode import ListNode


class TestLinkedListCycle(unittest.TestCase):
    def test_has_cycle(self):
        solution = Solution()
        head = ListNode.arrayToListNode([3, 2, 0, -4])
        pos = 1
        self.assertTrue(solution.hasCycle(head))

        head = ListNode.arrayToListNode([1, 2])
        pos = 0
        self.assertTrue(solution.hasCycle(head))

        head = ListNode.arrayToListNode([1])
        pos = -1
        self.assertFalse(solution.hasCycle(head))

import unittest
from solutions.copy_list_with_random_pointer import Solution, Node


class TestCopyListWithRandomPointer(unittest.TestCase):
    def test_copy_list_with_random_pointer(self):
        solution = Solution()
        # head = Node.arrayToListNode([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        # expect = Node.arrayToListNode([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        # actual = solution.copy_random_list(head)
        # self.assertEqual(Node.listNodeToArray(actual), Node.listNodeToArray(expect))
        #
        # head = Node.arrayToListNode([[1, 1], [2, 1]])
        # expect = Node.arrayToListNode([[1, 1], [2, 1]])
        # actual = solution.copy_random_list(head)
        # self.assertEqual(Node.listNodeToArray(actual), Node.listNodeToArray(expect))
        #
        # head = Node.arrayToListNode([[3, None], [3, 0], [3, None]])
        # expect = Node.arrayToListNode([[3, None], [3, 0], [3, None]])
        # actual = solution.copy_random_list(head)
        # self.assertEqual(Node.listNodeToArray(actual), Node.listNodeToArray(expect))

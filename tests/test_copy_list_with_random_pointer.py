import unittest
from solutions.copy_list_with_random_pointer import Solution, Node


class TestCopyListWithRandomPointer(unittest.TestCase):
    def test_copy_list_with_random_pointer(self):
        solution = Solution()
        node_0 = Node(7, None)
        node_1 = Node(13, None)
        node_2 = Node(11, None)
        node_3 = Node(10, None)
        node_4 = Node(1, None)
        node_0.next = node_1
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_1.random = node_0
        node_2.random = node_4
        node_3.random = node_2
        node_4.random = node_0
        expect = node_0
        actual = solution.copy_random_list(node_0)

        while expect and actual:
            self.assertEqual(expect.val, actual.val)
            self.assertEqual(expect.random.val if expect.random else None, actual.random.val if actual.random else None)
            expect = expect.next
            actual = actual.next
            expect = expect.next if expect else None
            actual = actual.next if actual else None

        node_0 = Node(1, None)
        node_1 = Node(2, None)
        node_0.next = node_1
        node_0.random = node_1
        node_1.random = node_1
        expect = node_0
        actual = solution.copy_random_list(node_0)
        while expect and actual:
            self.assertEqual(expect.val, actual.val)
            self.assertEqual(expect.random.val if expect.random else None, actual.random.val if actual.random else None)
            expect = expect.next if expect else None
            actual = actual.next if actual else None

        node_0 = Node(3, None)
        node_1 = Node(3, None)
        node_2 = Node(3, None)
        node_0.next = node_1
        node_1.next = node_2
        node_1.random = node_0
        expect = node_0
        actual = solution.copy_random_list(node_0)
        while expect and actual:
            self.assertEqual(expect.val, actual.val)
            self.assertEqual(expect.random.val if expect.random else None, actual.random.val if actual.random else None)
            expect = expect.next if expect else None
            actual = actual.next if actual else None

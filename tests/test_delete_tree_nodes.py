import unittest
from solutions.delete_tree_nodes import Solution


class TestDeleteTreeNodes(unittest.TestCase):
    def test_delete_tree_nodes(self):
        solution = Solution()
        nodes = 7
        parent = [-1, 0, 0, 1, 2, 2, 2]
        value = [1, -2, 4, 0, -2, -1, -1]
        expect = 2
        actual = solution.deleteTreeNodes(nodes, parent, value)
        self.assertEqual(actual, expect)

        nodes = 7
        parent = [-1, 0, 0, 1, 2, 2, 2]
        value = [1, -2, 4, 0, -2, -1, -2]
        expect = 6
        actual = solution.deleteTreeNodes(nodes, parent, value)
        self.assertEqual(actual, expect)

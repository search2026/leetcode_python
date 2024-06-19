import unittest
from solutions.delete_node_in_a_bst import Solution
from utils.TreeNode import TreeNode, arrayToTreeNode, serialize


class TestDeleteNodeInABST(unittest.TestCase):
    def test_delete_node_in_a_bst(self):
        solution = Solution()

        root = arrayToTreeNode([5, 3, 6, 2, 4, None, 7])
        key = 3
        expected = ['5', '4', '6', '2', None, None, '7', None, None, None, None]
        actual = serialize(solution.deleteNode(root, key))
        self.assertCountEqual(actual, expected)

        root = arrayToTreeNode([5, 3, 6, 2, 4, None, 7])
        key = 0
        expected = ['5', '3', '6', '2', '4', None, '7', None, None, None, None, None, None]
        actual = serialize(solution.deleteNode(root, key))
        self.assertCountEqual(actual, expected)

        root = arrayToTreeNode([])
        key = 0
        expected = [None]
        actual = serialize(solution.deleteNode(root, key))
        self.assertCountEqual(actual, expected)

        root = arrayToTreeNode([1])
        key = 1
        expected = [None]
        actual = serialize(solution.deleteNode(root, key))
        self.assertCountEqual(actual, expected)

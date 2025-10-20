import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.invert_binary_tree import Solution


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_tree(self):
        solution = Solution()
        root = [2, 1, 3]
        expect = arrayToTreeNode([2, 3, 1])
        actual = solution.invertTree(arrayToTreeNode(root))
        self.assertEqual(expect, actual)

        root = []
        expect = arrayToTreeNode([])
        actual = solution.invertTree(arrayToTreeNode(root))
        self.assertEqual(expect, actual)

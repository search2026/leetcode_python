import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.construct_binary_tree_from_preorder_and_inorder_traversal import Solution


class TestBlank(unittest.TestCase):
    def test_buil_tree(self):
        solution = Solution()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expect = arrayToTreeNode([3, 9, 20, None, None, 15, 7])
        actual = solution.buildTree(preorder, inorder)
        self.assertEqual(expect, actual)

        preorder = [-1]
        inorder = [-1]
        expect = arrayToTreeNode([-1])
        actual = solution.buildTree(preorder, inorder)
        self.assertEqual(expect, actual)

import unittest
from solutions.binary_tree_level_order_traversal import Solution
from utils.TreeNode import deserialize, arrayToTreeNode
from utils.TreeNode import TreeNode


class TestBlank(unittest.TestCase):
    def test_level_order(self):
        solution = Solution()
        root = [3, 9, 20, None, None, 15, 7]
        expect = [[3], [9, 20], [15, 7]]
        actual = solution.levelOrder(arrayToTreeNode(root))
        self.assertEqual(expect, actual)

        root = [1]
        expect = [[1]]
        actual = solution.levelOrder(arrayToTreeNode(root))
        self.assertEqual(expect, actual)

        root = []
        expect = []
        actual = solution.levelOrder(arrayToTreeNode(root))
        self.assertEqual(expect, actual)

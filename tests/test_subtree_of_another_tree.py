import unittest

from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.subtree_of_another_tree import Solution


class TestBlank(unittest.TestCase):
    def test_is_subtree(self):
        solution = Solution()
        root = arrayToTreeNode([3, 4, 5, 1, 2])
        subRoot = arrayToTreeNode([4, 1, 2])
        self.assertTrue(solution.isSubtree(root, subRoot))

        root = arrayToTreeNode([3, 4, 5, 1, 2, None, None, None, None, 0])
        subRoot = arrayToTreeNode([4, 1, 2])
        self.assertTrue(solution.isSubtree(root, subRoot))

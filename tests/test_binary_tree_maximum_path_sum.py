import unittest
from solutions.binary_tree_maximum_path_sum import Solution
from utils.TreeNode import deserialize, arrayToTreeNode


class TestBinaryTreeMaximumPathSum(unittest.TestCase):
    def test_binary_tree_maximum_path_sum(self):
        solution = Solution()
        root = [1, 2, 3]
        expect = 6
        self.assertEqual(solution.maxPathSum(arrayToTreeNode(root)), expect)

        root = [-10, 9, 20, None, None, 15, 7]
        expect = 42
        self.assertEqual(solution.maxPathSum(arrayToTreeNode(root)), expect)

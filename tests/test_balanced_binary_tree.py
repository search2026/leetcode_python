import unittest
from solutions.balanced_binary_tree import Solution
from utils.TreeNode import deserialize


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced_binary_tree(self):
        solution = Solution()
        root = deserialize('[3,9,20,null,null,15,7]')
        self.assertTrue(solution.isBalanced(root))

        root = deserialize('[1,2,2,3,3,null,null,4,4]')
        self.assertFalse(solution.isBalanced(root))

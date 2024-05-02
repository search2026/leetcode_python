import unittest
from solutions.maximum_depth_of_binary_tree import Solution
from utils.TreeNode import TreeNode, deserialize


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_maximum_depth_of_binary_tree(self):
        solution = Solution()
        root = deserialize("[3,9,20,null,null,15,7]")
        expect = 3
        self.assertEqual(solution.maxDepth(root), expect)

        root = deserialize("[1,null,2]")
        expect = 2
        self.assertEqual(solution.maxDepth(root), expect)

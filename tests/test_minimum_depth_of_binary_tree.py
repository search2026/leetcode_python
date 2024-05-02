import unittest
from solutions.minimum_depth_of_binary_tree import Solution
from utils.TreeNode import TreeNode, deserialize


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    def test_minimum_depth_of_binary_tree(self):
        solution = Solution()
        root = deserialize('[3,9,20,null,null,15,7]')
        expect = 2
        self.assertEqual(solution.minDepth(root), expect)

        root = deserialize('[2,null,3,null,4,null,5,null,6]')
        expect = 5
        self.assertEqual(solution.minDepth(root), expect)

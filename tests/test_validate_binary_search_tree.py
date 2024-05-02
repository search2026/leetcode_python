import unittest
from solutions.validate_binary_search_tree import Solution
from utils.TreeNode import TreeNode, deserialize


class TestValidateBinarySearchTree(unittest.TestCase):
    def test_validate_binary_search_tree(self):
        solution = Solution()
        root = deserialize("[2, 1,3]")
        self.assertTrue(solution.is_valid_bst(root))

        root = deserialize("[5,1,4,null,null,3,6]")
        self.assertFalse(solution.is_valid_bst(root))

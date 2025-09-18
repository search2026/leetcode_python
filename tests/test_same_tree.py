from typing import List, Optional
from solutions.same_tree import Solution
from utils.TreeNode import TreeNode, deserialize


class TestSameTree(unittest.TestCase):
    def test_is_same_tree(self):
        solution = Solution()
        p = [1, 2, 3]
        q = [1, 2, 3]
        self.assertTrue(solution.isSameTree(p, q))

        p = [1, 2]
        q = [1, None, 2]
        self.assertFalse(solution.isSameTree(p, q))

        p = [1, 2, 1]
        q = [1, 1, 2]
        self.assertFalse(solution.isSameTree(p, q))

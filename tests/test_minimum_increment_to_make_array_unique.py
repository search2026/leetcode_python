import unittest
from solutions.minimum_increment_to_make_array_unique import Solution


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    def test_minimum_depth_of_binary_tree(self):
        solution = Solution()
        self.assertEqual(solution.minIncrementForUnique([1, 2, 2]), 1)
        self.assertEqual(solution.minIncrementForUnique([3, 2, 1, 2, 1, 7]), 6)

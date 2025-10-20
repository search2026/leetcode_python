import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.contains_duplicate import Solution, Solution2


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = Solution()
        nums = [1, 2, 3, 1]
        self.assertTrue(solution.containsDuplicate(nums))

        nums = [1, 2, 3, 4]
        self.assertFalse(solution.containsDuplicate(nums))

        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(solution.containsDuplicate(nums))

    def test_contains_duplicate(self):
        solution = Solution2()
        nums = [1, 2, 3, 1]
        self.assertTrue(solution.containsDuplicate(nums))

        nums = [1, 2, 3, 4]
        self.assertFalse(solution.containsDuplicate(nums))

        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(solution.containsDuplicate(nums))

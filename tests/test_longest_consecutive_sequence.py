import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.blank import Solution


class TestBlank(unittest.TestCase):
    def test_longest_consecutive(self):
        solution = Solution()
        nums = [100, 4, 200, 1, 3, 2]
        expect = 4
        actual = solution.longestConsecutive(nums)
        self.assertEqual(expect, actual)

        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expect = 9
        actual = solution.longestConsecutive(nums)
        self.assertEqual(expect, actual)

        nums = [1, 0, 1, 2]
        expect = 3
        actual = solution.longestConsecutive(nums)
        self.assertEqual(expect, actual)

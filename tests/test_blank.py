import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.blank import Solution


class TestBlank(unittest.TestCase):
    def test_method1(self):
        solution = Solution()
        expect = 0
        actual = solution.method()
        self.assertEqual(expect, actual)

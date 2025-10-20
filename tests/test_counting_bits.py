import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.counting_bits import Solution


class TestCountingBits(unittest.TestCase):
    def test_count_bits(self):
        solution = Solution()
        n = 2
        expect = [0, 1, 1]
        actual = solution.countBits(n)
        self.assertEqual(expect, actual)

        n = 5
        expect = [0, 1, 1, 2, 1, 2]
        actual = solution.countBits(n)
        self.assertEqual(expect, actual)

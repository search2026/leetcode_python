import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.sum_of_two_integers import Solution


class TestSumOfTwoIntegers(unittest.TestCase):
    def test_get_sum(self):
        solution = Solution()
        a = 1
        b = 2
        expect = 3
        actual = solution.getSum(a, b)
        self.assertEqual(expect, actual)

        a = 2
        b = 3
        expect = 5
        actual = solution.getSum(a, b)
        self.assertEqual(expect, actual)

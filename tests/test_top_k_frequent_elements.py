import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.top_k_frequent_elements import Solution


class TestTopKFrequentElements(unittest.TestCase):
    def test_top_k_frequent(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expect = [1, 2]
        actual = solution.topKFrequent(nums, k)
        self.assertEqual(expect, actual)

        nums = [1]
        k = 1
        expect = [1]
        actual = solution.topKFrequent(nums, k)
        self.assertEqual(expect, actual)

        nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
        k = 2
        expect = [1, 2]
        actual = solution.topKFrequent(nums, k)
        self.assertEqual(expect, actual)

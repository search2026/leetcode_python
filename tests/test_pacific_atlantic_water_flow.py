import unittest

from utils.ListNode import ListNode
from utils.TreeNode import deserialize, arrayToTreeNode, TreeNode

from solutions.pacific_atlantic_water_flow import Solution


class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def test_pacific_atlantic(self):
        solution = Solution()
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expect = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        actual = solution.pacificAtlantic(heights)
        self.assertEqual(expect, actual)

        heights = [[1]]
        expect = [[0, 0]]
        actual = solution.pacificAtlantic(heights)
        self.assertEqual(expect, actual)

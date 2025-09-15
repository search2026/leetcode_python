import unittest
from solutions.merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def test_merge(self):
        solution = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expect = [[1, 6], [8, 10], [15, 18]]
        actual = solution.merge(intervals)
        self.assertEqual(expect, actual)

        intervals = [[1, 4], [4, 5]]
        expect = [[1, 5]]
        actual = solution.merge(intervals)
        self.assertEqual(expect, actual)

        intervals = [[4, 7], [1, 4]]
        expect = [[1, 7]]
        actual = solution.merge(intervals)
        self.assertEqual(expect, actual)

import unittest
from solutions.non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def test_non_overlapping_intervals(self):
        solution = Solution()
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(1, solution.erase_overlap_intervals(intervals))

        intervals = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(2, solution.erase_overlap_intervals(intervals))

        intervals = [[1, 2], [2, 3]]
        self.assertEqual(0, solution.erase_overlap_intervals(intervals))

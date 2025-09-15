import unittest
from solutions.insert_intervals import Solution, Solution2


class TestInsertIntervals(unittest.TestCase):
    def test_merge(self):
        solution = Solution()
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expect = [[1, 5], [6, 9]]
        actual = solution.insert(intervals)
        self.assertEqual(expect, actual)

        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expect = [[1, 2], [3, 10], [12, 16]]
        actual = solution.insert(intervals)
        self.assertEqual(expect, actual)

    def test_merge2(self):
        solution = Solution2()
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expect = [[1, 5], [6, 9]]
        actual = solution.insert(intervals)
        self.assertEqual(expect, actual)

        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expect = [[1, 2], [3, 10], [12, 16]]
        actual = solution.insert(intervals)
        self.assertEqual(expect, actual)

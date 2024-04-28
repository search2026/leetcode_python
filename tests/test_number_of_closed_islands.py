import unittest
from solutions.number_of_closed_islands import Solution


class TestNumberOfClosedIslands(unittest.TestCase):
    def test_number_of_closed_islands(self):
        solution = Solution()
        grid = [[1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0]]
        expect = 2
        actual = solution.closed_island(grid)
        self.assertEqual(actual, expect)

        grid = [[0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0]]
        expect = 1
        actual = solution.closed_island(grid)
        self.assertEqual(actual, expect)

        grid = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1]]
        expect = 2
        actual = solution.closed_island(grid)
        self.assertEqual(actual, expect)

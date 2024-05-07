import unittest
from solutions.unique_paths import Solution, Solution2, Solution3


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths(self):
        solution = Solution()
        m = 3
        n = 7
        self.assertEqual(solution.unique_paths(m, n), 28)

        m = 3
        n = 2
        self.assertEqual(solution.unique_paths(m, n), 3)

    def test_unique_paths2(self):
        solution = Solution2()
        obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(solution.unique_paths_with_obstacles(obstacle_grid), 2)

        obstacle_grid = [[0, 1], [0, 0]]
        self.assertEqual(solution.unique_paths_with_obstacles(obstacle_grid), 1)

    def test_unique_paths3(self):
        solution = Solution3()
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
        self.assertEqual(solution.uniquePathsIII(grid), 2)

        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
        self.assertEqual(solution.uniquePathsIII(grid), 4)

        grid = [[0,1],[2,0]]
        self.assertEqual(solution.uniquePathsIII(grid), 0)



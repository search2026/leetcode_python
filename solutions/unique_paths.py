# -*- coding: utf-8 -*-

################################################
#
# Leetcode 62. Unique Paths
# URL: https://leetcode.com/problems/unique-paths/description/
# Difficulty: Medium
#
################################################

class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


################################################
#
# Leetcode 63. Unique Paths II
# URL: https://leetcode.com/problems/unique-paths-ii/description/
# Difficulty: Medium
#
################################################


class Solution2(object):
    def unique_paths_with_obstacles(self, grid):
        n = len(grid)
        m = len(grid[0])

        path_matrix = [[0] * m for i in range(n)]

        if grid[0][0] == 1:
            path_matrix[0][0] = 0
        else:
            path_matrix[0][0] = 1

        for i in range(1, m):
            if grid[0][i] == 1:
                path_matrix[0][i] = 0
            else:
                path_matrix[0][i] = path_matrix[0][i - 1]
        for i in range(1, n):
            if grid[i][0] == 1:
                path_matrix[i][0] = 0
            else:
                path_matrix[i][0] = path_matrix[i - 1][0]
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    path_matrix[i][j] = 0
                else:
                    path_matrix[i][j] = path_matrix[i][j - 1] + path_matrix[i - 1][j]
        return path_matrix[n - 1][m - 1]


################################################
#
# Leetcode 980. Unique Paths III
# URL: https://leetcode.com/problems/unique-paths-iii/description/
# Difficulty: Hard
#
################################################

class Solution3:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = range(len(grid)), range(len(grid[0]))

        zeros = sum(row.count(0) for row in grid)  # count the zeros to ensure all cells visited
        start = tuple((r, c) for r in m for c in n  # find start in grid
                      if grid[r][c] == 1)[0]

        self.res = 0

        def dfs(row, col, zeros):
            grid[row][col] = 3  # change 0 to 3 to avoid returning

            for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):  # explore the grid recursively
                r, c = row + dr, col + dc
                if r in m and c in n:
                    if grid[r][c] == 0:
                        dfs(r, c, zeros - 1)
                    if grid[r][c] == 2 and zeros == 0:
                        self.res += 1

            grid[row][col] = 0  # change back
            return

        res = 0
        dfs(*start, zeros)
        return self.res

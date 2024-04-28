# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 1254. Number of Closed Islands
# URL: https://leetcode.com/problems/number-of-closed-islands/description/
# Difficulty: Medium
#
################################################


class Solution:
    def closed_island(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0

        def dfs(i, j):
            # nonlocal grid
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            elif grid[i][j] == 1:
                return True
            grid[i][j] = 1
            ans = True
            ans = dfs(i + 1, j) and ans
            ans = dfs(i - 1, j) and ans
            ans = dfs(i, j + 1) and ans
            ans = dfs(i, j - 1) and ans
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1 and dfs(i, j):
                    res += 1
        return res

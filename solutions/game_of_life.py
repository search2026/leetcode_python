from typing import List


# -*- coding: utf-8 -*-

################################################
#
# Leetcode 289. Game of Life
# URL: https://leetcode.com/problems/game-of-life/description/
# Difficulty: Medium
#
################################################


class Solution:
    def game_of_life(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                ones = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        ones += board[x][y] & 1
                # Any live cell with 2 or 3 live neighbors
                # lives on to the next generation
                if board[i][j] == 1 and (ones == 3 or ones == 4):
                    board[i][j] |= 2
                # Any dead cell with exactly 3 live neighbors
                # becomes a live cell, as if by reproduction
                if board[i][j] == 0 and ones == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

# -*- coding: utf-8 -*-
from typing import List, Optional


################################################
#
# Leetcode: 1143. Longest Common Subsequence
# URL: https://leetcode.com/problems/longest-common-subsequence/description/
# Difficulty: Medium
#
################################################


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = (
                    1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
                )
        return dp[-1][-1]


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            tex1, tex2 = text2, text1
        dp = [[0] * (n + 1) for _ in range(2)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[1 - i % 2][j + 1] = (
                    1 + dp[i % 2][j]
                    if c == d
                    else max(dp[i % 2][j + 1], dp[1 - i % 2][j])
                )
        return dp[m % 2][-1]


class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        if m < n:
            tex1, tex2 = text2, text1
        dp = [0] * (n + 1)
        for c in text1:
            prevRow, prevRowPrevCol = 0, 0
            for j, d in enumerate(text2):
                prevRow, prevRowPrevCol = dp[j + 1], prevRow
                dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
        return dp[-1]

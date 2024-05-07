# -*- coding: utf-8 -*-

################################################
#
# Leetcode 70. Climbing Stairs
# URL: https://leetcode.com/problems/climbing-stairs/description/
# Difficulty: Easy
#
################################################

class Solution:
    def climb_stairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

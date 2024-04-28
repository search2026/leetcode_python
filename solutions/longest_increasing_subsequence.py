# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 300. Longest Increasing Subsequence
# URL: https://leetcode.com/problems/longest-increasing-subsequence/description/
# Difficulty: Medium
#
################################################


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

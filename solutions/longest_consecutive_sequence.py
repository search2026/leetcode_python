# -*- coding: utf-8 -*-
from typing import List, Optional


################################################
#
# Leetcode 128. Longest Consecutive Sequence
# URL: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Difficulty: Medium
#
################################################


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest

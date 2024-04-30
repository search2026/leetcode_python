# -*- coding: utf-8 -*-
from itertools import pairwise
from typing import List


################################################
#
# Leetcode 163. Missing Ranges
# URL: https://leetcode.com/problems/missing-ranges/description/
# Difficulty: Easy
#
################################################

class Solution:
    def find_missing_ranges(
            self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        res = []
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])
        for a, b in pairwise(nums):
            if b - a > 1:
                res.append([a + 1, b - 1])
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        return res

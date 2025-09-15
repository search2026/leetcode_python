# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 56. Merge Intervals
# URL: https://leetcode.com/problems/merge-intervals/description/
# Difficulty: Medium
#
################################################


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                res.append(prev)
                prev = interval

        res.append(prev)

        return res

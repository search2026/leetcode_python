# -*- coding: utf-8 -*-
import heapq
from collections import Counter
from heapq import heapify, heappush, heappop
from typing import List


################################################
#
# Leetcode 435. Non-overlapping Intervals
# URL: https://leetcode.com/problems/non-overlapping-intervals/description/
# Difficulty: Medium
#
################################################

class Solution:
    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count

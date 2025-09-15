# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 57. Insert Interval
# URL: https://leetcode.com/problems/insert-interval/description/
# Difficulty: Medium
#
################################################


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res


class Solution2:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        res = []

        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        res.extend(intervals[i:])

        return res

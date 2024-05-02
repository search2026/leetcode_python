# -*- coding: utf-8 -*-
from heapq import heapify, heappush, heappop
from typing import List


################################################
#
# Leetcode 252. Meeting Rooms
# URL: https://leetcode.com/problems/meeting-rooms/description/
# Difficulty: Easy
#
################################################
class Solution(object):
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


################################################
#
# Leetcode 253. Meeting Rooms II
# URL: https://leetcode.com/problems/meeting-rooms-ii/description/
# Difficulty: Medium
#
################################################
class Solution2(object):
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        meetings = []
        for i in intervals:
            meetings.append((i[0], 1))
            meetings.append((i[1], 0))
        meetings.sort()
        res = 0
        count = 0
        for meeting in meetings:
            if meeting[1] == 1:
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res


################################################
#
# Leetcode 2402. Meeting Rooms III
# URL: https://leetcode.com/problems/meeting-rooms-iii/description/
# Difficulty: Hard
#
################################################
class Solution3:
    def most_booked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        busy = []
        idle = list(range(n))
        heapify(idle)
        cnt = [0] * n
        for s, e in meetings:
            while busy and busy[0][0] <= s:
                heappush(idle, heappop(busy)[1])
            if idle:
                i = heappop(idle)
                cnt[i] += 1
                heappush(busy, (e, i))
            else:
                a, i = heappop(busy)
                cnt[i] += 1
                heappush(busy, (a + e - s, i))
        res = 0
        for i, v in enumerate(cnt):
            if cnt[res] < v:
                res = i
        return res

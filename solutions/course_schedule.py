# -*- coding: utf-8 -*-
import collections
import heapq
from collections import deque
from typing import List


################################################
#
# Leetcode 207. Course Schedule
# URL: https://leetcode.com/problems/course-schedule/description/
# Difficulty: Medium
#
################################################
class Solution:

    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort
        alist = collections.defaultdict(list)
        order = [0] * num_courses
        for i, j in prerequisites:
            alist[j].append(i)
            order[i] += 1
        q = collections.deque()
        for i in range(len(order)):
            if order[i] == 0:
                q.append(i)

        count = 0
        while q:
            current = q.popleft()
            count += 1
            for i in alist[current]:
                order[i] -= 1
                if order[i] == 0:
                    q.append(i)

        return count == num_courses


################################################
#
# Leetcode 210. Course Schedule II
# URL: https://leetcode.com/problems/course-schedule-ii/description/
# Difficulty: Medium
#
################################################

class Solution2:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(num_courses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        stack = []
        valid, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False  # impossible
            if crs in valid:
                return True

            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False  # propagate the impossibility
            cycle.remove(crs)

            valid.add(crs)
            stack.append(crs)
            return True

        for crs in range(num_courses):
            if not dfs(crs):
                return []
        return stack


################################################
#
# Leetcode 630. Course Schedule III
# URL: https://leetcode.com/problems/course-schedule-iii/description/
# Difficulty: Hard
#
################################################
class Solution3:
    def schedule_course(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        A, curr = [], 0
        for dur, ld in courses:
            heapq.heappush(A, -dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(A)
        return len(A)


################################################
#
# Leetcode 1462. Course Schedule IV
# URL: https://leetcode.com/problems/course-schedule-iv/description/
# Difficulty: Medium
#
################################################
class Solution4(object):
    def check_if_prerequisite(self, num_courses, prerequisites, queries):
        adj = {i: [] for i in range(num_courses)}

        for x, y in prerequisites:
            adj[y].append(x)
        res = []

        def dfs(crs):
            if crs not in premap:
                premap[crs] = set()
                for nei in adj[crs]:
                    premap[crs] |= dfs(nei)
            premap[crs].add(crs)
            return premap[crs]

        premap = {}
        for i in range(num_courses):
            dfs(i)
        for x, y in queries:
            res.append(x in premap[y])
        return res
# please upvote if found helpful

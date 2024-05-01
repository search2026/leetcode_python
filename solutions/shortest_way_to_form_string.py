# -*- coding: utf-8 -*-

################################################
#
# Leetcode 1055. Shortest Way to Form String
# URL: https://leetcode.com/problems/shortest-way-to-form-string/description/
# Difficulty: Medium
#
################################################

class Solution:
    def shortest_way(self, source: str, target: str) -> int:
        def f(i, j):
            while i < m and j < n:
                if source[i] == target[j]:
                    j += 1
                i += 1
            return j

        m, n = len(source), len(target)
        res = j = 0
        while j < n:
            k = f(0, j)
            if k == j:
                return -1
            j = k
            res += 1
        return res

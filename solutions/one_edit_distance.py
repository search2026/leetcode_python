# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 161. One Edit Distance
# URL: https://leetcode.com/problems/one-edit-distance/description/
# Difficulty: Medium
#
################################################

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):  # goal is to ensure t is always the shorter one
            return self.isOneEditDistance(t, s)
        m, n = len(s), len(t)
        if m - n > 1:
            return False
        for i, c in enumerate(t):
            if c != s[i]:
                return s[i + 1:] == t[i + 1:] if m == n else s[i + 1:] == t[i:]
        # case: abc, abcd. return true
        # case: abc, abc. the same 2 strings should return false
        # case: abc, abcdefg, return false
        return m == n + 1

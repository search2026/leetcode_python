# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 131. Palindrome Partitioning
# URL: https://leetcode.com/problems/palindrome-partitioning/description/
# Difficulty: Medium
#
################################################

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        if n == 0:
            return [[]]
        for i in range(1, n + 1):
            if s[:i] != s[:i][::-1]:
                continue
            curr = self.partition(s[i:])
            for j in range(len(curr)):
                res.append([s[:i]] + curr[j])
        return res

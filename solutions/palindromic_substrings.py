# -*- coding: utf-8 -*-
from typing import List, Optional


################################################
#
# Leetcode: 647. Palindromic Substrings
# URL: https://leetcode.com/problems/palindromic-substrings/description/
# Difficulty: Medium
#
################################################


class Solution:
    def countSubstrings(self, s: str) -> int:
        L, r = len(s), 0
        for i in range(L):
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < L and s[a] == s[b]:
                    a -= 1
                    b += 1
                r += (b - a) // 2
        return r

# -*- coding: utf-8 -*-
import math
from typing import List


################################################
#
# Leetcode 1. Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
################################################


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = {}
        left, right = 0, 0
        res = 1
        while right < len(s):
            if s[right] in seen:
                left = seen[s[right]] + 1
            res = max(res, right - left + 1)
            seen[s[right]] = right
            right += 1
        return res

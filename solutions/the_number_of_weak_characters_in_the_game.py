# -*- coding: utf-8 -*-
from heapq import heapify, heappush, heappop
from typing import List


################################################
#
# Leetcode 1996. The Number of Weak Characters in the Game
# URL: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/
# Difficulty: Medium
#
################################################
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        res = 0
        curr_max_d = 0
        for _, d in properties:
            if d < curr_max_d:
                res += 1
            else:
                curr_max_d = d
        return res

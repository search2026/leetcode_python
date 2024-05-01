# -*- coding: utf-8 -*-
from collections import defaultdict, deque
from typing import Dict, List, Set


################################################
#
# Leetcode 277. Find the Celebrity
# URL: https://leetcode.com/problems/alien-dictionary/description/
# Difficulty: Hard
#
################################################
class Solution:
    def find_celebrity(self, n: int) -> int:
        res = 0
        for i in range(1, n):
            if self.knows(res, i):
                res = i
        for i in range(n):
            if res != i:
                if self.knows(res, i) or not self.knows(i, res):
                    return -1
        return res

    def knows(a: int, b: int) -> bool:
        return False

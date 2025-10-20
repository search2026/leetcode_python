# -*- coding: utf-8 -*-
from typing import List, Optional


################################################
#
# Leetcode 338. Counting Bits
# URL: https://leetcode.com/problems/counting-bits/description/
# Difficulty: Easy
#
################################################


class Solution:
    def countBits(self, n: int) -> List[int]:
        nextOrder = 2
        tracker = 0
        counter = [0] * (num + 1)

        for i in range(1, num + 1):
            if i == nextOrder:
                nextOrder *= 2
                tracker = 0
            counter[i] = counter[tracker] + 1
            tracker += 1
        return counter

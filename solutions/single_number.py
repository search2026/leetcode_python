# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


################################################
#
# Leetcode 136. Single Number
# URL: https://leetcode.com/problems/single-number/description/
# Difficulty: Easy
#
################################################

class Solution:
    def single_number(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


################################################
#
# Leetcode 137. Single Number II
# URL: https://leetcode.com/problems/single-number-ii/description/
# Difficulty: Medium
#
################################################

class Solution2:
    def single_number(self, nums):
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones


################################################
#
# Leetcode 260. Single Number III
# URL: https://leetcode.com/problems/single-number-iii/description/
# Difficulty: Medium
#
################################################

class Solution3:
    def single_number(self, nums: List[int]) -> List[int]:
        p = 0
        q = 0
        for i in nums:
            p ^= i;
        for i in nums:
            if ((p & (-p)) & i) == 0:
                q ^= i
        return [p ^ q, q];

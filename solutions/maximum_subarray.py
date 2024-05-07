# -*- coding: utf-8 -*-
from math import inf
from typing import List


################################################
#
# Leetcode 53. Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/description/
# Difficulty: Medium
#
################################################

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        local_max = 0
        global_max = -inf
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)
        return global_max

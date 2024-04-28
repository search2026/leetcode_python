# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 1. Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
################################################


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in dic:
                return [dic[pair], index]
            else:
                dic[num] = index

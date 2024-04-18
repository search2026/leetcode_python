# -*- coding: utf-8 -*-

################################################
#
# Leetcode 1
# URL: https://leetcode.com/problems/two-sum/
#
################################################

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in dic:
                return [dic[pair], index]
            else:
                dic[num] = index

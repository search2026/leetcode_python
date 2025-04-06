# -*- coding: utf-8 -*-
from typing import Optional
from utils.ListNode import ListNode


################################################
#
# Leetcode 628. Maximum Product of Three Numbers
# URL: https://leetcode.com/problems/maximum-product-of-three-numbers/
# Difficulty: Easy
#
################################################

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) ==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0] * nums[1], nums[0], nums[1])
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, min1 * min2 * max1)




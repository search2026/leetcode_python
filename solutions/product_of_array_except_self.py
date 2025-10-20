# -*- coding: utf-8 -*-
from typing import List, Optional


################################################
#
# Leetcode: 238 Product of Array Except Self
# URL: https://leetcode.com/problems/product-of-array-except-self/description/
# Difficulty: Medium
#
################################################


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output

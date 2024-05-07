# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 152. Maximum Product Subarray
# URL: https://leetcode.com/problems/maximum-product-subarray/description/
# Difficulty: Medium
#
################################################

class Solution:
    def max_product(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                current_max, current_min = current_min, current_max

            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])

            max_product = max(max_product, current_max)

        return max_product

# -*- coding: utf-8 -*-
import math
from typing import List, Optional
from utils.TreeNode import TreeNode
import sys


################################################
#
# Leetcode 945. Minimum Increment to Make Array Unique
# URL: https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
# Difficulty: Medium
#
################################################

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                res += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return res
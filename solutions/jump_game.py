# -*- coding: utf-8 -*-
from typing import List

################################################
#
# Leetcode 55. Jump Game
# URL: https://leetcode.com/problems/jump-game/description/
# Difficulty: Medium
#
################################################


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True

# -*- coding: utf-8 -*-
from typing import Optional
from utils.ListNode import ListNode

################################################
#
# Leetcode 268. Missing Number
# URL: https://leetcode.com/problems/missing-number/description/
# Difficulty: Easy
#
################################################

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans


class Solution_2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        v = [-1] * (n + 1)
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] == -1:
                return i
        return 0


class Solution_3:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        sum_all_nums = (len(nums) * (len(nums) + 1))//2
        sum_nums = sum(nums)
        return sum_all_nums - sum_nums

# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 153. Find Minimum in Rotated Sorted Array
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Difficulty: Medium
#
################################################

class Solution:
    def find_min(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


################################################
#
# Leetcode 154. Find Minimum in Rotated Sorted Array II
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
# Difficulty: Hard
#
################################################

class Solution2:
    def find_min(self, a: List[int]) -> int:
        left = 0
        right = len(a) - 1
        while left < right:
            middle = (right + left) // 2
            if a[middle] > a[right]:
                left = middle + 1
            elif a[middle] < a[right]:
                right = middle
            else:
                right -= 1
        return a[left]

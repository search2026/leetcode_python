# -*- coding: utf-8 -*-

################################################
#
# Leetcode 0 Blank template
# URL: https://leetcode.com/problems/PROBLEM_TITLE/
# Difficulty: Medium
#
################################################

class Solution(object):
    def search_insert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

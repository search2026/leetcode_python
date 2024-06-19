# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 33. Search in Rotated Sorted Array
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: Medium
#
################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


################################################
#
# Leetcode 81. Search in Rotated Sorted Array II
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# Difficulty: Medium
#
################################################

class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True

            if nums[low] == nums[mid]:
                low += 1
                continue

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False

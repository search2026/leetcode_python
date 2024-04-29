# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 1. Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
################################################


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in dic:
                return [dic[pair], index]
            else:
                dic[num] = index


################################################
#
# Leetcode 167. Two Sum II - Input Array Is Sorted
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Difficulty: Medium
#
################################################


class Solution2:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1


################################################
#
# Leetcode 170. Two Sum III - Data Structure design
# URL: https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
# Difficulty: Easy
#
################################################

class TwoSum:
    def __init__(self):
        self.structure = []

    def add(self, input):
        self.structure.append(input)

    def find(self, value):
        return self.twoSum(self.structure, value)

    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return True  # [hash_map[complement], i]
            else:
                hash_map[nums[i]] = i
        return False

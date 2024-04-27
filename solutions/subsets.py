# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 78. Subsets
# URL: https://leetcode.com/problems/subsets/description/
# Difficulty: Medium
#
################################################

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        # Helper function
        def backtrack(curr, start):
            # base case
            if start == n:
                res.append(list(curr))
                return

            # recursive case
            # choice 1: include the current element
            curr.append(nums[start])
            backtrack(curr, start + 1)

            # backtracking step
            curr.pop()

            # choice 2: exclude the current element
            backtrack(curr, start + 1)

        backtrack([], 0)
        return res


################################################
#
# Leetcode 90. Subsets II
# URL: https://leetcode.com/problems/subsets-ii/description/
# Difficulty: Medium
#
################################################

class Solution2:
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, curr = [], []

        def backtrack(i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1)

            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1)

        backtrack(0)
        return res

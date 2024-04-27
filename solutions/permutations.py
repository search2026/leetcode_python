# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 46. Permutations
# URL: https://leetcode.com/problems/permutations/description/
# Difficulty: Medium
#
################################################

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res


################################################
#
# Leetcode 47. Permutations II
# URL: https://leetcode.com/problems/permutations-ii/description/
# Difficulty: Medium
#
################################################
class Solution2:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        visited = [False] * len(nums)

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            used = set()
            for i in range(len(nums)):
                if not visited[i] and nums[i] not in used:
                    visited[i] = True
                    curr.append(nums[i])
                    used.add(nums[i])
                    backtrack()
                    visited[i] = False
                    curr.pop()

        backtrack()
        return res

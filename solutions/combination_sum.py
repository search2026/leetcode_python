# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 39. Combination Sum
# URL: https://leetcode.com/problems/combination-sum/description/
# Difficulty: Medium
#
################################################

class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res


################################################
#
# Leetcode 40. Combination Sum II
# URL: https://leetcode.com/problems/combination-sum-ii/description/
# Difficulty: Medium
#
################################################

class Solution2:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, comb, tot):
            if tot == target:
                ans.append(comb[:])
                return
            if i >= len(candidates) or tot > target:
                return
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                comb.append(candidates[idx])
                backtrack(idx + 1, comb, tot + candidates[idx])
                comb.pop()

        candidates.sort()
        backtrack(0, [], 0)
        return ans

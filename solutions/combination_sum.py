# -*- coding: utf-8 -*-
from functools import lru_cache
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


################################################
#
# Leetcode 216. Combination Sum III
# URL: https://leetcode.com/problems/combination-sum-iii/description/
# Difficulty: Medium
#
################################################

class Solution3:
    def combination_sum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(start, path, curr):
            if len(path) == k and curr == n:
                res.append(path)
                return
            elif len(path) == k and curr != n:
                return
            # Will always starts on a number that hasn't been used before,
            # So don't need to record what number has been visited
            for i in range(start, 10):
                dfs(i + 1, path + [i], curr + i)

        dfs(1, [], 0)
        return res


################################################
#
# Leetcode 377. Combination Sum IV
# URL: https://leetcode.com/problems/combination-sum-iv/description/
# Difficulty: Medium
#
################################################
class Solution4:
    def combination_sum4(self, nums: list[int], target: int) -> int:

        @lru_cache(None)
        def dp(target: int, res=0) -> int:

            for n in nums:

                if n == target:
                    res += 1
                if n < target:
                    res += dp(target - n)

            return res

        return dp(target)

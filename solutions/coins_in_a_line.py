# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode ???? Coins in a Line
# URL: https://leetcode.com/discuss/general-discussion/136614/coins-problem-set-c-solution
# Difficulty: Medium
#
################################################

class Solution(object):
    def is_first_player_win(self, n: int) -> bool:
        if n <= 0:
            return False
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = True
        for i in range(2, n + 1):
            dp[i] = not dp[i - 1] or not dp[i - 2]
        return dp[-1]

################################################
#
# Leetcode ???? Coins in a Line II
# URL: https://leetcode.com/discuss/general-discussion/136614/coins-problem-set-c-solution
# Difficulty: Medium
#
################################################

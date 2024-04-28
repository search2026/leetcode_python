# -*- coding: utf-8 -*-
import math
from typing import List


################################################
#
# Leetcode 787. Cheapest Flights Within K Stops
# URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# Difficulty: Medium
#
################################################


class Solution:
    def find_cheapest_price(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [math.inf] * n
        dp[src] = 0
        for _ in range(k + 1):
            new_dp = dp[:]
            for f, t, price in flights:
                new_dp[t] = min(new_dp[t], dp[f] + price)
            dp = new_dp
        return -1 if dp[dst] == math.inf else dp[dst]

# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 121. Best Time to Buy and Sell Stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Difficulty: Easy
################################################


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


################################################
#
# Leetcode 122. Best Time to Buy and Sell Stock II
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Difficulty: Medium
#
################################################


class Solution2:
    def max_profit(self, prices: List[int]) -> int:
        # Use constant literal to help reader understand source code below.

        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0

        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            # either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)

            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)

        # maximum profit must be in not-hold state
        return cur_not_hold


################################################
#
# Leetcode 123. Best Time to Buy and Sell Stock III
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# Difficulty: hard
#
################################################


class Solution3:
    def max_profit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # initialize variables for first buy, first sell, second buy, and second sell
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0

        # iterate over prices to update buy and sell values
        for price in prices:
            # update first buy and sell values
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            # update second buy and sell values
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2


################################################
#
# Leetcode 188. Best Time to Buy and Sell Stock IV
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
# Difficulty: Hard
#
################################################


class DoubleLinkListNode:
    def __init__(self, ind, pre=None, next=None):
        self.ind = ind
        self.pre = pre if pre else self
        self.next = next if next else self


class Solution4:
    def max_profit(self, k: int, prices: List[int]) -> int:
        # no transaction, no profit
        if k == 0:
            return 0
        # dp[k][0] = min cost you need to spend at most k transactions
        # dp[k][1] = max profit you can achieve at most k transactions
        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                # price - dp[i - 1][1] is how much you need to spend,
                # i.e. use the profit you earned from previous transaction to buy the stock
                # we want to minimize it
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                # price - dp[i][0] is how much you can achieve from previous min cost
                # we want to maximize it
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        # return max profit at most k transactions, or you can write `return dp[-1][1]`
        return dp[k][1]


################################################
#
# Leetcode 309. Best Time to Buy and Sell Stock with Cooldown
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# Difficulty: Medium
#
################################################


class Solution5:
    def max_profit(self, prices: List[int]) -> int:

        """
        We have three states:
            - s0: starting state, no stock, can rest or buy
            - s1: just bought stock, can rest or sell
            - s2: just sold stock, must rest

        The reason state s2 exists is that we want to force a rest between leaving s1 (previous sell) and s0 (next buy).

        Each state has the following actions:
            - s0:
                - s0 -> s0: no stock, rest
                - s0 -> s1: buy new stock
            - s1:
                - s1 -> s1: hold stock, rest
                - s1 -> s2: sell stock
            - s2:
                - s2 -> s0: forced rest

        Let sk[j], k = {0, 1, 2}, j = {0, 1, ..., n}, denote the profit at state sk on day j
        (e.g., s1[2] is the profit on day 2 if we happened to be there).

        We have the following ways to enter each state:
            - Entering s0[i]:
                - From s0[i-1]: rest on day i, so profit remains the same as s0[i-1]
                - From s2[i-1]: forced rest on day i, so profit remains the same as s2[i-1]
            - Entering s1[i]:
                - From s1[i-1]: rest on day i, so profit remains the same as s1[i-1]
                - From s0[i-1]: bought stocks on day i, so profit is updated to (s0[i-1]-profits[i])
            - Entering s2[i]:
                - From s1[i-1]: sold stock on day i, so profit is updated to (s1[i-1]+profits[i])

        Initial states:
            - s[0] = 0: you start with 0 profit on day 0
            - s1[0] = -prices[0]: if you bought stock on day 0, ur profit is -prices[0]
            - s2[0] = X: dummy state as you need two days to buy and sell
        """

        n = len(prices)
        if not n:
            return 0

        s0, s1, s2 = [0] * n, [0] * n, [0] * n

        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = 0  # dummy

        for i in range(1, n):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[-1], s2[-1])


################################################
#
# Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
# Difficulty: Medium
#
################################################


class Solution6:
    def max_profit(self, prices: List[int], fee: int) -> int:
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell

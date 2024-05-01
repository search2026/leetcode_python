# -*- coding: utf-8 -*-
from collections import defaultdict, deque
from typing import Dict, List, Set


################################################
#
# Leetcode 139. Word Break
# URL: https://leetcode.com/problems/word-break/description/
# Difficulty: Medium
#
################################################


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, word_dict))  # The maximum length of a word in the dictionary

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):  # Only consider words that could fit
                if dp[j] and s[j:i] in word_dict:
                    dp[i] = True
                    break

        return dp[n]


################################################
#
# Leetcode 140. Word Break II
# URL: https://leetcode.com/problems/word-break-ii/description/
# Difficulty: Hard
#
################################################
class Solution2:
    def word_break(self, s: str, word_dict: List[str]) -> List[str]:
        cache = {}

        def breaker(s):
            if s not in cache:
                result = []
                for w in word_dict:
                    if s[:len(w)] == w:
                        if len(s) == len(w):
                            result.append(w)
                        else:
                            for word in breaker(s[len(w):]):
                                result.append(w + " " + word)
                cache[s] = result
            return cache[s]

        return breaker(s)

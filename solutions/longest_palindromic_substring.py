# -*- coding: utf-8 -*-


################################################
#
# Leetcode 5. Longest Palindromic Substring
# URL: https://leetcode.com/problems/longest-palindromic-substring/description/
# Difficulty: Medium
#
################################################


class Solution:
    def longest_palindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j + 1] == s[i:j + 1][::-1]:
                    max_len = j - i + 1
                    max_str = s[i:j + 1]

        return max_str


class Solution2(object):
    def longest_palindrome(self, s):
        longest = ''
        dp = [[0] * len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest = s[i]

        # filling the dp table
        for i in range(len(s) - 1, -1, -1):
            # j starts from the i location : to only work on the upper side of the diagonal
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:  # if the chars mathces
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        if len(longest) < len(s[i:j + 1]):
                            longest = s[i:j + 1]

        return longest

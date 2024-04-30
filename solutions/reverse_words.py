# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 151. Reverse Words in a String
# URL: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium
#
################################################


class Solution:
    def reverse_words(self, s: str) -> str:
        res = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                res.append(temp)
                temp = ""
        if temp != "":
            res.append(temp)
        return " ".join(res[::-1])


################################################
#
# Leetcode 186. Reverse Words in a String II
# URL: https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
# Difficulty: Medium
#
################################################


class Solution2:
    def reverse_words(self, s: List[str]) -> None:
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        i, j, n = 0, 0, len(s)
        while j < n:
            if s[j] == ' ':
                reverse(s, i, j - 1)
                i = j + 1
            elif j == n - 1:
                reverse(s, i, j)
            j += 1
        reverse(s, 0, n - 1)

# -*- coding: utf-8 -*-
from typing import List
import re


################################################
#
# Leetcode 125. Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/description/
# Difficulty: Easy
#
################################################


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True

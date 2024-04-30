# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 9. Palindrome Number
# URL: https://leetcode.com/problems/palindrome-number/description/
# Difficulty: Easy
#
################################################

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        input_num = x
        new_num = 0
        while x > 0:
            new_num = new_num * 10 + x % 10
            x = x // 10
        return new_num == input_num

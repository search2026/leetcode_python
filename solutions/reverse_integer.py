# -*- coding: utf-8 -*-


################################################
#
# Leetcode 7. Reverse Integer
# URL: https://leetcode.com/problems/reverse-integer/description/
# Difficulty: Medium
#
################################################


class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2, 31) - 1
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if res > max_int:
            return 0
        return res * sign

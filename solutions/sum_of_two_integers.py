# -*- coding: utf-8 -*-
from typing import List, Optional


################################################
#
# Leetcode 371. Sum of Two Integers
# URL: https://leetcode.com/problems/sum-of-two-integers/description/
# Difficulty: Medium
#
################################################


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32 bit mask
        maxInt = 2**31 - 1

        while b != 0:
            sum = (a ^ b) & mask  # contain to 32 bits
            carry = (a & b) & mask  # contain to 32 bits
            a = sum
            b = carry << 1

        return a if a <= maxInt else ~(a ^ mask)

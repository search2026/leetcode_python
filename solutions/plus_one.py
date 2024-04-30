# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 1. Two Sum
# URL: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
#
################################################
class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plus_one(digits[0:-1])
            return digits


class Solution2:
    def plus_one(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


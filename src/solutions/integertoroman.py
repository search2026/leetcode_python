# -*- coding: utf-8 -*-

################################################
#
# Leetcode 12
# URL: https://leetcode.com/problems/integer-to-roman/
#
################################################


class Solution:
    def int_to_roman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "XL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM",
        }

        # Result Variable
        res = ''

        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                res += num_map[n]
                num -= n
        return res

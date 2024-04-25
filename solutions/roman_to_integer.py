# -*- coding: utf-8 -*-

################################################
#
# Leetcode 13 Roman to Integer
# URL: https://leetcode.com/problems/roman-to-integer/description/
# Difficulty: Easy
#
################################################


class Solution:
    def roman_to_int(self, s: str) -> int:
        translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

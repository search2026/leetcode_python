# -*- coding: utf-8 -*-

################################################
#
# Leetcode 20. Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses/description/
# Difficulty: Easy
#
################################################

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack

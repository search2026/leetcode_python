# -*- coding: utf-8 -*-


################################################
#
# 1249. Minimum Remove to Make Valid Parentheses
# URL: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
# Difficulty: Medium
#
################################################


class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        # Initialize variables
        open_parentheses_count = 0
        arr = list(s)

        # First pass: mark excess closing parentheses with '*'
        for i in range(len(arr)):
            if arr[i] == '(':
                open_parentheses_count += 1
            elif arr[i] == ')':
                if open_parentheses_count == 0:
                    arr[i] = '*'  # Mark excess closing parentheses
                else:
                    open_parentheses_count -= 1

        # Second pass: mark excess opening parentheses from the end
        for i in range(len(arr) - 1, -1, -1):
            if open_parentheses_count > 0 and arr[i] == '(':
                arr[i] = '*'  # Mark excess opening parentheses
                open_parentheses_count -= 1

        # Filter out marked characters and construct the result string
        res = ''.join(c for c in arr if c != '*')

        return res

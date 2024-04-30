# -*- coding: utf-8 -*-
import math
from typing import List


################################################
#
# Leetcode 8. String to Integer (atoi)
# URL: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium
#
################################################

class Solution:
    def a_to_i(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value


class Solution2:
    def a_to_i(self, s: str) -> int:
        length, i, sign, res = len(s), 0, +1, ''

        while i < length and s[i] == ' ':
            i = i + 1

        if i < length and s[i] in ('-', '+'):
            sign, i = -1 if s[i] == '-' else +1, i + 1
            # sign = -1 if s[i] == '-' else +1
            # i = i + 1

        while i < length and s[i].isdigit():
            res, i = res + s[i], i + 1
            # i = res + s[i]
            # i = i + 1

        return max(-2 ** 31, min(sign * int(res or 0), 2 ** 31 - 1))

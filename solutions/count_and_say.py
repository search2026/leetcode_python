# -*- coding: utf-8 -*-

################################################
#
# Leetcode 38. Count and Say
# URL: https://leetcode.com/problems/count-and-say/description/
# Difficulty: Medium
#
################################################

class Solution:
    def count_and_say(self, n: int) -> str:
        if n == 0: return ''
        if n == 1: return '1'
        res = '1'

        for _ in range(n - 1):
            prev, count = res[0], 0
            new_str = ''

            for l in res:
                if prev != l:
                    new_str += str(count) + prev
                    prev, count = l, 1
                else:
                    count += 1

            new_str += str(count) + prev
            res = new_str

        return res
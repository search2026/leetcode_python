# -*- coding: utf-8 -*-


################################################
#
# Leetcode 68. Text Justification
# URL: https://leetcode.com/problems/text-justification/description/
# Difficulty: Hard
#
################################################


class Solution:
    def full_justify(self, words, max_width):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > max_width:
                for i in range(max_width - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(max_width)]

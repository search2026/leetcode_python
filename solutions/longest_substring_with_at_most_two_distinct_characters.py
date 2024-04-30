# -*- coding: utf-8 -*-
from typing import List
from collections import Counter


################################################
#
# Leetcode 159. Longest Substring with At Most Two Distinct Characters
# URL: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
# Difficulty: Medium
#
################################################


class Solution:
    def length_of_longest_substring_two_distinct(self, s):
        cnt = Counter()  # or, cnt = defaultdict(int)
        ans = i = 0
        for j, c in enumerate(s):
            cnt[c] += 1
            while len(cnt) > 2:  # shrink
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])
                i += 1
            ans = max(ans, j - i + 1)
        return ans

# -*- coding: utf-8 -*-
from typing import List
from collections import defaultdict


################################################
#
# Leetcode 49. Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/description/
# Difficulty: Medium
#
################################################


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)

        return list(res.values())


################################################
#
# Leetcode 49. Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/description/
# Difficulty: Medium
#
################################################


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())

# -*- coding: utf-8 -*-
import heapq
from collections import Counter


################################################
#
# Leetcode 767. Reorganize String
# URL: https://leetcode.com/problems/reorganize-string/description/
# Difficulty: Medium
#
################################################


class Solution:
    def reorganize_string(self, s: str) -> str:
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)

        if freq_map[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""

        res = [""] * len(s)
        i = 0
        for c in sorted_chars:
            for _ in range(freq_map[c]):
                if i >= len(s):
                    i = 1
                res[i] = c
                i += 2

        return "".join(res)


################################################
#
# Leetcode 767. Reorganize String
# URL: https://leetcode.com/problems/reorganize-string/description/
# Difficulty: Medium
#
################################################

class Solution2:
    def reorganize_string(self, s: str) -> str:
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1
        count = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(max_heap)

        prev = None
        res = ""
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res

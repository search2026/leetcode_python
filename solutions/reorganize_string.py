# -*- coding: utf-8 -*-
import heapq


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

        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)

        res = []
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            res.extend([char1, char2])

            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            freq, c = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            res.append(c)

        return "".join(res)

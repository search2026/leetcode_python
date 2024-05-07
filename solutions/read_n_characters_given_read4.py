# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 157. Read N Characters Given Read4
# URL: https://leetcode.com/problems/read-n-characters-given-read4/description/
# Difficulty: Easy
#
################################################


def read4(buf4: List[int]) -> int:
    pass


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        buf4: list[int] = [0] * 4
        v = 5
        while v >= 4:
            v = read4(buf4)
            for j in range(v):
                buf[i] = buf4[j]
                i += 1
                if i >= n:
                    return n
        return i


################################################
#
# Leetcode 158. Read N Characters Given Read4 II - Call Multiple Times
# URL: https://leetcode.com/problems/read-n-characters-given-read4-ii/description/
# Difficulty: Hard
#
################################################

class Solution2:
    buf4: list[int]

    def __init__(self):
        self.buf4 = [None] * 4
        self.i = self.size = 0

    def read(self, buf: List[str], n: int) -> int:
        j = 0
        while j < n:
            if self.i == self.size:
                self.size = read4(self.buf4)
                self.i = 0
                if self.size == 0:
                    break
            while j < n and self.i < self.size:
                buf[j] = self.buf4[self.i]
                self.i += 1
                j += 1
        return j

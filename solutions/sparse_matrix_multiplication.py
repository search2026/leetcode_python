# -*- coding: utf-8 -*-
from typing import List


################################################
#
# Leetcode 311. Sparse Matrix Multiplication
# URL: https://leetcode.com/problems/sparse-matrix-multiplication/description/
# Difficulty: Medium
#
################################################

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def f(mat: List[List[int]]) -> List[List[int]]:
            g = [[] for _ in range(len(mat))]
            for i, row in enumerate(mat):
                for j, x in enumerate(row):
                    if x:
                        g[i].append((j, x))
            return g

        g1 = f(mat1)
        g2 = f(mat2)
        m, n = len(mat1), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for k, x in g1[i]:
                for j, y in g2[k]:
                    res[i][j] += x * y
        return res

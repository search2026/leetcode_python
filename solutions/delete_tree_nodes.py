# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


################################################
#
# Leetcode 1273. Delete Tree Nodes
# URL: https://leetcode.com/problems/delete-tree-nodes
# Difficulty: Medium
#
################################################
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        def dfs(i):
            s, m = value[i], 1
            for j in g[i]:
                t, n = dfs(j)
                s += t
                m += n
            if s == 0:
                m = 0
            return s, m

        g = defaultdict(list)
        for i in range(1, nodes):
            g[parent[i]].append(i)
        return dfs(0)[1]

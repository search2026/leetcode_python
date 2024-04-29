# -*- coding: utf-8 -*-
from collections import deque
from typing import List


################################################
#
# Leetcode 785. Is Graph Bipartite?
# URL: https://leetcode.com/problems/is-graph-bipartite/description/
# Difficulty: Medium
#
################################################

class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def bfs(start, graph, color):
            q = deque()
            color[start] = 0
            q.append(start)
            while len(q) != 0:
                element = q.popleft()
                for e in graph[element]:
                    if color[e] == -1:
                        if color[element] == 0:
                            color[e] = 1
                            q.append(e)
                        else:
                            color[e] = 0
                            q.append(e)
                    else:
                        if color[e] == color[element]:
                            return False
            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not bfs(i, graph, color):
                    return False
        return True

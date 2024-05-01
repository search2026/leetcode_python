# -*- coding: utf-8 -*-
from collections import defaultdict, deque
from typing import Dict, List, Set


################################################
#
# Leetcode 269. Alien Dictionary
# URL: https://leetcode.com/problems/alien-dictionary/description/
# Difficulty: Hard
#
################################################

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        self._build_graph(graph, words, in_degree)
        return self._topology_sort(graph, in_degree)

    def _build_graph(self, graph: Dict[str, Set[str]], words: List[str], in_degree: Dict[str, int]) -> None:
        # Create a node for each character in each word
        for word in words:
            for c in word:
                in_degree[c] = 0  # necessary for final char counting

        for first, second in zip(words, words[1:]):  # or pairwise(words)
            length = min(len(first), len(second))
            for j in range(length):
                u = first[j]
                v = second[j]
                if u != v:
                    if v not in graph[u]:
                        graph[u].add(v)
                        in_degree[v] += 1
                    break  # Later characters' order is meaningless
                if j == length - 1 and len(first) > len(second):
                    # If 'ab' comes before 'a', it's an invalid order
                    graph.clear()
                    return

    def _topology_sort(self, graph: Dict[str, Set[str]], in_degree: Dict[str, int]) -> str:
        res = ''
        q = deque([c for c in in_degree if in_degree[c] == 0])

        while q:
            u = q.popleft()
            res += u
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        # If there are remaining characters in inDegree, it means there's a cycle
        if any(in_degree.values()):
            return ''

        # Words = ['z', 'x', 'y', 'x']
        return res if len(res) == len(in_degree) else ''

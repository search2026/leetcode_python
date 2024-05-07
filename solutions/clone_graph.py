# -*- coding: utf-8 -*-

from utils.GraphNode import Node

################################################
#
# Leetcode 133. Clone Graph
# URL: https://leetcode.com/problems/clone-graph/description/
# Difficulty: Medium
#
################################################

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:

            if node in mapping:
                return mapping[node]

            cloned = Node(node.val)
            mapping[node] = cloned

            for child in node.neighbors:
                cloned.neighbors.append(dfs(child))

            return cloned

        return dfs(node) if node else None

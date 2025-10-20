# -*- coding: utf-8 -*-
from collections import deque
from typing import List, Optional

from utils.TreeNode import TreeNode

################################################
#
# Leetcode 102. Binary Tree Level Order Traversal
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Difficulty: Medium
#
################################################


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels

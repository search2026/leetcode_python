# -*- coding: utf-8 -*-
import math
from typing import Optional
from utils.TreeNode import TreeNode
import sys


################################################
#
# Leetcode 104. Maximum Depth of Binary Tree
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Difficulty: Easy
#
################################################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

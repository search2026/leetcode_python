# -*- coding: utf-8 -*-
import math
from typing import Optional
from utils.TreeNode import TreeNode
import sys


################################################
#
# Leetcode 111. Minimum Depth of Binary Tree
# URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Difficulty: Easy
#
################################################

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + right_depth

        if root.right is None:
            return 1 + left_depth

        return min(left_depth, right_depth) + 1

# -*- coding: utf-8 -*-

from typing import Optional
from utils.TreeNode import TreeNode


################################################
#
# Leetcode 110. Balanced Binary Tree
# URL: https://leetcode.com/problems/balanced-binary-tree/description/
# Difficulty: Medium
#
################################################

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) != -1

    def Height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lef_height, right_height = self.Height(root.left), self.Height(root.right)
        if lef_height < 0 or right_height < 0 or abs(lef_height - right_height) > 1:
            return -1
        return max(lef_height, right_height) + 1

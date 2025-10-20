# -*- coding: utf-8 -*-
from typing import List, Optional


from utils.TreeNode import TreeNode

################################################
#
# Leetcode: 572. Subtree of Another Tree
# URL: https://leetcode.com/problems/subtree-of-another-tree/description/
# Difficulty: Easy
#
################################################


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is q

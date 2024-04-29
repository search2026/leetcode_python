# -*- coding: utf-8 -*-
from typing import Optional
from utils.TreeNode import TreeNode

################################################
#
# Leetcode 230. Kth Smallest Element in a BST
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Difficulty: Medium
#
################################################


class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0
        t = root

        # Perform in-order traversal
        while t or stack:
            while t:
                stack.append(t)
                t = t.left
            t = stack.pop()
            n += 1
            if n == k:
                return t.val
            t = t.right

        return 0

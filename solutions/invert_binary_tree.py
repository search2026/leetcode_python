# -*- coding: utf-8 -*-
from typing import List, Optional


from utils.TreeNode import TreeNode

################################################
#
# Leetcode 226. Invert Binary Tree
# URL: https://leetcode.com/problems/invert-binary-tree/description/
# Difficulty: Easy
#
################################################


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # Base Case
            return root
        self.invertTree(root.left)  # Call the left substree
        self.invertTree(root.right)  # Call the right substree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root  # Return the root

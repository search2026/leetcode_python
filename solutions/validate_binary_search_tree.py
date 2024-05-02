# -*- coding: utf-8 -*-
import math
from typing import Optional
from utils.TreeNode import TreeNode
import sys


################################################
#
# Leetcode 98. Validate Binary Search Tree
# URL: https://leetcode.com/problems/validate-binary-search-tree/description/
# Difficulty: Medium
#
################################################


class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        def in_order_traverse(node, lower, upper):
            if not node:
                return True

            if lower < node.val < upper:
                return in_order_traverse(node.left, lower, node.val) and in_order_traverse(node.right, node.val, upper)
            else:
                return False

        return in_order_traverse(node=root, lower=-math.inf, upper=math.inf)

# -*- coding: utf-8 -*-

from typing import Optional

from utils.ListNode import ListNode
from utils.TreeNode import TreeNode


################################################
#
# Leetcode 109. Convert Sorted List to Binary Search Tree
# URL: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Difficulty: Medium
#
################################################

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        middle = self.getMiddle(head)
        root = TreeNode(middle.val)
        root.right = self.sortedListToBST(middle.next)
        middle.next = None
        root.left = self.sortedListToBST(head)
        return root

    def getMiddle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
        return slow

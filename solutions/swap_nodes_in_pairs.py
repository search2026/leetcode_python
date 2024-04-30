# -*- coding: utf-8 -*-
from typing import Optional
from utils.ListNode import ListNode


################################################
#
# Leetcode 24. Swap Nodes in Pairs
# URL: https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Difficulty: Medium
#
################################################


class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next

        return dummy.next

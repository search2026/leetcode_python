# -*- coding: utf-8 -*-
from typing import Optional
from utils.ListNode import ListNode


################################################
#
# Leetcode 19. Remove Nth Node From End of List
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Difficulty: Medium
#
################################################

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

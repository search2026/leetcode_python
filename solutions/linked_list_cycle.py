# -*- coding: utf-8 -*-
from typing import List, Optional
from utils.ListNode import ListNode

################################################
#
# Leetcode 141. Linked List Cycle
# URL: https://leetcode.com/problems/linked-list-cycle/description/
# Difficulty: Easy
#
################################################


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
